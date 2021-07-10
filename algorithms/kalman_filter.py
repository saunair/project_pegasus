import numpy as np
import plotly.graph_objects as go
import pandas as pd


def get_state_matrices_for_2d(dt):
    # Just the control matrices.
    # dt must come from the sensor readings. 
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
    a = 2  # Acceleration
    v = 280
    dt = 1  # Difference in time

    # Process / Estimation Errors
    # Why is this constant? Shouldn't it vary constantly? 
    error_est_x = 20
    error_est_v = 5

    return a, v, dt,  error_est_x, error_est_v


def get_sensor_properties():
    # Both are variances in each dimension of the sensor reading.
    # Why is this constant? 
    error_obs_x = 20
    error_obs_v = 5
    return error_obs_x, error_obs_v


def get_sensor_measurements():
    x_observations = np.array([4000, 4260, 4550, 4860, 5110])
    v_observations = np.array([280, 282, 285, 286, 290])
    sensor_readings = np.c_[x_observations, v_observations]
    return sensor_readings 


def plot_the_data(
    estimated_states, 
    estimation_covariances
):
    estimated_values = pd.DataFrame(columns=["position", "velocity", "position_variance", "velocity_variance"])
    for data_entry_index in range(len(estimated_states)):
        estimated_values = estimated_values.append(
            {
                "position": estimated_states[data_entry_index][0], 
                "velocity":estimated_states[data_entry_index][1], 
                "position_variance": estimation_covariances[data_entry_index][0][0], 
                "velocity_variance": estimation_covariances[data_entry_index][1][1],
                "time": data_entry_index,
            },
            ignore_index=True,
        )

    # The following code isn't functional. I'm trying to animate the gaussians here.
    px.scatter(
        estimated_values, 
        x="position", y="probability", 
        animation_frame="time", animation_group="position",
        size="pop", 
        range_x=[100,100000], range_y=[25,90]
    )
    


    
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


def get_ground_truth_measurements(num_measurements=100, dt=1e-2, initial_speed=0.0, initial_position=100):
    """Get the ground truth states of the object.
    
    Args:
        num_measurements: Number of total measurements done.
        dt: Time difference between two consecutive measurements.
        initial_speed: The starting velocity of the body.
        initial_position: The starting position of the body.

    Returns:
        [(position, velocity)]
    """
    g = -9.81
    states = []
    A, B = get_state_matrices_for_2d(dt)
    current_state = [initial_position, initial_speed]

    while len(states) < num_measurements:
        current_state = forward_kinetics(
            current_position=current_state[0], 
            current_velocity=current_state[1],
            input_acceleration=g,
            state_matrix=A, input_matrix=B
        )
        states.append(current_state)
    return states


def forward_kinetics(current_position, current_velocity, input_acceleration, state_matrix, input_matrix):
    """Forward rollout of the state just based on the previous state and the action input
    
    Args:
        current_position: 
        current_velocity:
        input_acceleration:
        state_matrix: "A" 
        input_matrix: "B" 
    
    """
    current_state = np.array([current_position, current_velocity])
    return state_matrix.dot(current_state) + input_matrix.dot(input_acceleration)


def run_kalman_step(
    dt, 
    previous_state, 
    previous_state_covariance, 
    observation_matrix, 
    input_acceleration, 
    measurement=None, 
    measurement_covariance=None
):
    # Variance

    A, B = get_state_matrices_for_2d(dt)

    # Covariance after a forward rollout.
    P = np.diag(np.diag(A.dot(previous_state_covariance).dot(A.T)))
    state_prediction_rollout = forward_kinetics(
        current_position=previous_state[0], 
        current_velocity=previous_state[1], 
        input_acceleration=input_acceleration, 
        state_matrix=A, input_matrix=B
    )

    # If there is no measurement, just return the rollout state and the increased covariance.
    if measurement is None:
        assert measurement_covariance is None, "measurement convariance cannot be None if measurement doesn't exist"
        return state_prediction_rollout, P

    measurement_prediction = observation_matrix.dot(state_prediction_rollout) 
    # Finally something that looks right to me. I haven't done 
    measurement_prediction_covariance = observation_matrix.dot(P).dot(observation_matrix.T)
    S = measurement_prediction_covariance + measurement_covariance
    kalman_gain = measurement_prediction_covariance.dot(np.linalg.inv(S))

    # Update the covariance matrix based on the new kalman gain.
    # As we now use the measurements, we'll get a new covariance with the state estimation.
    P = (np.identity(len(kalman_gain)) - kalman_gain.dot(observation_matrix)).dot(P)
    estimated_state = state_prediction_rollout + kalman_gain.dot(measurement - measurement_prediction)
    return estimated_state, P


def run_kalman_demo():
    # sensor variances.
    error_obs_x, error_obs_v = get_sensor_properties()

    # So R remains the same for all the cycles??
    measurement_covariance = covariance2d(error_obs_x, error_obs_v)

    # We are assuming a constant acceleration for now as the data is a flight moving at a constant speed.
    a, v, dt, error_est_x, error_est_v = get_motion_properties()
    measurements = get_sensor_measurements()

    # Observation * state gives us the variables visible 
    # Observation matrix is a direct pass? Reasonable for now. Let's assume a sensor will give this information.
    # Maybe meausred via experiments etc.
    observation_matrix = np.identity(2)
    
    # Initial covariance matrix.
    # Shouldn't position variance be a function of the state's velocity?
    current_state_covariance = covariance2d(error_est_x, error_est_v)
    current_state = [measurements[0][0], measurements[0][1]]

    # Now run through the sensor measurements.
    # Initial State Matrix
    estimated_states = []
    estimation_covariances = []
    for measurement in measurements:
        current_state, current_state_covariance = run_kalman_step(
            dt=dt, 
            previous_state=current_state, 
            previous_state_covariance=current_state_covariance, 
            observation_matrix=observation_matrix,
            input_acceleration=a,
            measurement_covariance=measurement_covariance,
            measurement=measurement,
        )
        estimated_states.append(current_state)
        estimation_covariances.append(current_state_covariance)
    return estimated_states, estimation_covariances


if __name__ == "__main__":
    ground_truth_states = get_ground_truth_measurements()
    estimated_states, estimation_covariances = run_kalman_demo()
    plot_the_data(estimated_states, estimation_covariances)

