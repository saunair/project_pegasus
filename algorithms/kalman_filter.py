import numpy as np
import plotly.graph_objects as go
import pandas as pd


def gaussian(mu, x, sigma):
    """Return the gaussian probability of the variable `x` from distribution specified by `mu` and `sigma`.
    
    Args:
        mu: The mean of the gaussian distribution.
        x: The variable of the gaussian at which the probability is calculated. 
        sigma: The variance of the gaussian distribution.

    Returns:
        probability: The probability of the value `x`.

    """
    c = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent_term = (-0.5) * ((x - mu) / sigma) ** 2
    return c * np.exp(exponent_term)


def test_gaussian():
    # Test the gaussian probability at the mean.
    probability = gaussian(
        mu=0, x=0, sigma=1.0
    )
    assert np.isclose(
        probability, 0.3989, atol=1e-3
    ), f"estimated probability {probability} needs to be 1.0"

    # Test the gaussian probability at sigma=0.5 
    probability = gaussian(
        mu=0, x=0.5, sigma=1.0
    )
    assert np.isclose(probability, 0.2419, atol=1e-3), f"{probability} should be 0.606"


def visualize_gaussian(mu, sigma, coarseness=1e-3, lower_x=-5, upper_x=5, gaussian_name="Gaussian distribution"):
    """Plot the gaussian
    
    Args:
        mu: mean of the gaussian distribution.
        sigma: The variance of the gaussian distribution.
        coarseness: The sampling distance between two adjacent gaussian samples. 
        lower_x: The lower value of the samples of the distribution. 
        upper_x: The upper value of the samples of the distribution. 
        gaussian_name: Name of the plot.

    """
    x_vars = []
    probabilities = []
    for x_value in np.arange(lower_x, upper_x, coarseness):
        x_vars.append(x_value)
        probabilities.append(gaussian(mu=mu, sigma=sigma, x=x_value))
    fig = go.Figure(layout=dict(paper_bgcolor='rgb(233,233,233)'))
    fig.add_trace(go.Scatter(x=x_vars, y=probabilities, mode='lines'))
    fig.update_layout(title_text=gaussian_name)
    fig.show()


def get_updated_mean(r, sigma, mu, v):
    return ((r ** 2) * mu) + ((sigma ** 2) * v) / ((r ** 2) + (sigma ** 2))


def get_updated_variance(r, variance):
    return np.sqrt(1 / (((1 / (r ** 2)) + (1 / (sigma ** 2)))))


def update_values(mu1, mu2, var1, var2):
    return (mu1 + mu2), (var1 + var2)

def kalman_gain(sigma_0, sigma_1):
    return sigma_0 /  (sigma_0 + sigma_1)


def get_state_and_variance(sigma_0, sigma_1, measured_state, estimated_state):
    current_kalman_gain =  kalman_gain(sigma_0, sigma_1)
    predicted_state = estimated_state + current_kalman_gain * (measured_state - estimated_state)
    predicted_variance = sigma_0 - current_kalman_gain * sigma_0 
    return predicted_state 


def get_state_matrices_for_2d(dt):
    A = np.array([[1, dt],
                  [0, 1]])
    B = np.array([[0.5 * dt ** 2],
                  [dt]])

    return A, B


def covariance2d(sigma1, sigma2):
    cov1_2 = sigma1 * sigma2
    cov2_1 = sigma2 * sigma1
    cov_matrix = np.array([[sigma1 ** 2, cov1_2],
                           [cov2_1, sigma2 ** 2]])
    return np.diag(np.diag(cov_matrix))


def get_motion_properties():
    x_observations = np.array([4000, 4260, 4550, 4860, 5110])
    v_observations = np.array([280, 282, 285, 286, 290])

    sensor_readings = np.c_[x_observations, v_observations]

    # Initial Conditions
    a = 2  # Acceleration
    v = 280
    dt = 1  # Difference in time

    # Process / Estimation Errors
    error_est_x = 20
    error_est_v = 5

    return sensor_readings, a, v, dt,  error_est_x, error_est_v


def get_sensor_properties():
    # Both are variances in each dimension of the sensor reading.
    error_obs_x = 20
    error_obs_v = 5
    return error_obs_x, error_obs_v


if __name__ == "__main__":
    #test_gaussian()
    #visualize_gaussian(mu=0, sigma=1.0)

    # Why is this constant? 

    # sensor variances.
    error_obs_x, error_obs_v = get_sensor_properties()

    # So R remains the same for all the cycles??
    measurement_covariance = covariance2d(error_obs_x, error_obs_v)

    # We are assuming a constant acceleration for now as the data is a flight moving at a constant speed.
    measurements, a, v, dt, error_est_x, error_est_v = get_motion_properties()

    # Observation * state gives us the variables visible 
    # Observation matrix is a direct pass? Reasonable for now. Let's assume a sensor will give this information.
    # Maybe meausred via experiments etc.
    observation_matrix = np.identity(2)
    
    # Initial covariance matrix.
    # Shouldn't position variance be a function of the state's velocity?
    P = covariance2d(error_est_x, error_est_v)
    estimated_state = [measurements[0][0], measurements[0][1]]
    # Now run through the sensor measurements.
    # Initial State Matrix
    estimated_states = []
    estimation_covariances = []
    for measurement in measurements:
        # Variance
        def get_state_matrices_for_2d(dt):
            """Predict state using the state space model. 
            Here we assume a newtown's motion's model for a 2d rigid object"""
            A = np.array([[1, dt],  # s2 = s1 + u*dt 
                          [0, 1]])  # u = u
            B = np.array(
                [
                    0.5 * dt ** 2,  # s = 1/2 * a * dt**2
                    dt              # v = u + a * dt
                ]
            )
            return A, B

        def _forward_kinetics(current_position, current_velocity, input_acceleration, A, B):
            """Forward rollout of the state just based on the previous state and the action input"""
            current_state = np.array([current_position, current_velocity])
            return A.dot(current_state) + B.dot(input_acceleration)

        A, B = get_state_matrices_for_2d(dt)

        # Covariance after a forward rollout.
        P = np.diag(np.diag(A.dot(P).dot(A.T)))
        state_prediction_rollout = _forward_kinetics(current_position=estimated_state[0], current_velocity=estimated_state[0], input_acceleration=a, A=A, B=B)
        measurement_prediction = observation_matrix.dot(state_prediction_rollout) 
        # Finally something that looks right to me. I haven't done 
        measurement_prediction_covariance = observation_matrix.dot(P).dot(observation_matrix.T)
        S = measurement_prediction_covariance + measurement_covariance
        kalman_gain = measurement_prediction_covariance.dot(np.linalg.inv(S))

        # Update the covariance matrix based on the new kalman gain.
        # As we now use the measurements, we'll get a new covariance with the state estimation.
        P = (np.identity(len(kalman_gain)) - kalman_gain.dot(observation_matrix)).dot(P)
        estimated_state = state_prediction_rollout + kalman_gain.dot(measurement - measurement_prediction)
        print(estimated_state, measurement)
        estimated_states.append(estimated_state)
        estimation_covariances.append(P)
    
    estimated_values = pd.DataFrame(columns=["position", "velocity", "position_variance", "velocity_variance"])
    for data_entry_index in range(len(estimated_states)):
        estimated_values = estimated_values.append(
            {
                "position": estimated_states[data_entry_index][0], 
                "velocity":estimated_states[data_entry_index][1], 
                "position_variance": estimation_covariances[data_entry_index][0][0], 
                "velocity_variance": estimation_covariances[data_entry_index][1][1]
            },
            ignore_index=True,
        )
    # visualize_gaussian(estimated_states[0][0], np.sqrt(estimation_covariances[0][0][0]), coarseness=1, lower_x=estimated_states[0][0] - 1000, upper_x=estimated_states[0][0] + 1000, gaussian_name="position distribution")
    # visualize_gaussian(estimated_states[0][1], np.sqrt(estimation_covariances[0][1][1]), coarseness=1, lower_x=estimated_states[0][1] - 1000, upper_x=estimated_states[0][1] + 1000, gaussian_name="velocity distribution")

    import IPython; IPython.embed()
    px.scatter(estimated_values, x="position", y="probability", animation_frame="time", animation_group="position",
               size="pop", range_x=[100,100000], range_y=[25,90])
