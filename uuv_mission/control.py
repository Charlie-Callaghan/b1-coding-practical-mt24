# Module for designing the controller
from typing import Protocol
import numpy as np
from numpy import ndarray

class Controller(Protocol):
    def compute_control(self, t: int, observation_t: float, reference: ndarray) -> float:
        ...

class PDController:
    """PD Controller implementation for the submarine depth control."""
    
    def __init__(self):
        self.prev_error = 0.0
        self.Kp = 0.15  # Proportional gain
        self.Kd = 0.5   # Derivative gain

    def compute_control(self, t: int, observation_t: float, reference: np.ndarray) -> float:
        """
        Compute the control input using PD control law
        u(t) = 0.15 e(t) + 0.5[e(t) - e(t-1)]

        Args:
            t (int): Current time step
            observation_t (float): Current system output (depth)
            reference (np.ndarray): Reference trajectory

        Returns:
            float: Control input
        """
        # Calculate current error
        error = reference[t] - observation_t
        
        # Calculate control input using PD control law
        control_input = self.Kp * error + self.Kd * (error - self.prev_error)
        
        # Store current error for next iteration
        self.prev_error = error
        
        return control_input
