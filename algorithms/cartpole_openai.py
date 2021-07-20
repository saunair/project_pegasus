"""
Run a cart-pole simulation; choose actions to keep the pendulum upright.

observation[0]: Cart position.
observation[1]: Cart velocity.
observation[2]: Pendulum angle.
observation[3]: Pendulum angular velocity.

action == 1: Apply an impulse towards the right.
action == 0: Apply an impulse towards the left.
"""

import gym
import numpy as np
import time


env = gym.make('CartPole-v0')
observation = env.reset()

action_space = [0, 1]

desired_angular_velocity = 0.0
desired_angle = 0.0 # verify this!

desired_cart_pos = 0.1
desired_cart_vel = 0.0


for t in range(1000):
    env.render()
    x, xd, theta, thetad = observation


    angle_loss = desired_angle - theta
    angle_d_loss = desired_angular_velocity - thetad
    cart_pos_loss = desired_cart_pos - x
    cart_vel_loss = desired_cart_vel - xd
    
    position_k1 = 1.0
    position_k2 = 0.024
    threshold = 0

    cart_pos_k1 = 4e-2
    cart_vel_k = -2e-2

    loss = position_k1 * angle_loss + position_k2 * angle_d_loss + (cart_pos_k1 * cart_pos_loss) + (cart_vel_loss * cart_vel_k)

    if loss < threshold:
        action = 1
    else:
        action = 0

    # The sample method is a placeholder.
    # Replace the following line to choose the action.

    time.sleep(2e-2)
    observation, reward, done, info = env.step(action)
