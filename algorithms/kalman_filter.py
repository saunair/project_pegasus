import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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


def get_ground_truth_measurements(num_measurements=1000, dt=1e-2, initial_speed=0.0, initial_position=100):
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
    time = 0.0

    while len(states) < num_measurements:
        states.append([current_state, time])
        current_state = forward_kinetics(
            current_position=current_state[0], 
            current_velocity=current_state[1],
            input_acceleration=g,
            state_matrix=A, input_matrix=B
        )
        time += dt
    return states


def get_noisy_measurements(ground_truth_measurements, noise_level):
    noisy_states = []
    for ground_truth_measurement in ground_truth_measurements:
        ground_truth_state, time = ground_truth_measurement
        covariance_matrix = covariance2d(noise_level[0], noise_level[1])
        noisy_state = np.random.multivariate_normal(ground_truth_state, covariance_matrix, 1)
        noisy_states.append([noisy_state[0], time])

    return noisy_states


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


def run_kalman_demo(
    sigma_position_measurements, 
    sigma_velocity_measurements, 
    measurements, 
    sigma_position_process, 
    sigma_velocity_process,
    input_acceleration=-9.81,
):
    """Run a single kalman step"""
    # So R remains the same for all the cycles??
    # The covariance looks the same throught the cycles
    measurement_covariance = covariance2d(sigma_position_measurements, sigma_velocity_measurements)

    # Observation * state gives us the variables visible 
    # Observation matrix is a direct pass? Reasonable for now. Let's assume a sensor will give this information.
    # Maybe meausred via experiments etc.
    observation_matrix = np.identity(2)
    
    # Initial covariance matrix.
    # Shouldn't position variance be a function of the state's velocity?
    current_state_covariance = covariance2d(
        sigma_position_process, 
        sigma_velocity_process
    )
    current_state = measurements[0][0]

    # Now run through the sensor measurements.
    # Initial State Matrix
    estimated_states = []
    estimation_covariances = []
    previous_time = measurements[0][1]
    for measurement_number, measurement in enumerate(measurements):
        if measurement_number > 10 and measurement_number < 200:
            measurement_passed = None
        else:
            measurement_passed = measurement[0]
        current_state, current_state_covariance = run_kalman_step(
            dt=measurement[1] -  previous_time, 
            previous_state=current_state, 
            previous_state_covariance=current_state_covariance, 
            observation_matrix=observation_matrix,
            input_acceleration=input_acceleration,
            measurement_covariance=measurement_covariance,
            measurement=measurement_passed,
        )
        previous_time = measurement[1]
        estimated_states.append([current_state, previous_time])
        estimation_covariances.append(current_state_covariance)
    return estimated_states, estimation_covariances


def plot_states(states_with_times, title_name):
    """A plotting utility to show the states of the body
    
    Args:
        states_with_times: list of states with their corresponding time-stamps
        title_name: The name of the plot.

    """
    positions = []
    velocities = []
    times = []
    for data_num in range(len(states_with_times)):
        positions.append(states_with_times[data_num][0][0])
        velocities.append(states_with_times[data_num][0][1])
        times.append(states_with_times[data_num][1])
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Position", "Velocity"))
    fig.add_trace(go.Scatter(x=times, y=positions, mode='lines', showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=times, y=velocities, mode='lines', showlegend=False), row=1, col=2)
    fig.update_layout(title_text=title_name)
    fig.show()


if __name__ == "__main__":
    ground_truth_states = get_ground_truth_measurements()

    # Just setting the noise in sensors and process noise
    sigma_position_measurements = 5.0
    sigma_velocity_measurements = 6.0
    sigma_position_process = 2.0
    sigma_velocity_process = 3.0

    plot_states(ground_truth_states, title_name="Ground truth states")
    noisy_measurements = get_noisy_measurements(
        ground_truth_states, 
        noise_level=[sigma_position_measurements, sigma_velocity_measurements]
    )
    plot_states(noisy_measurements, title_name="Measurements")
    estimated_states, estimation_covariances = run_kalman_demo(
        sigma_position_measurements=sigma_position_measurements, 
        sigma_velocity_measurements=sigma_velocity_measurements, 
        sigma_position_process=sigma_position_process,
        sigma_velocity_process=sigma_velocity_process,
        measurements=noisy_measurements
    )

    plot_states(estimated_states, title_name="Predictions")
