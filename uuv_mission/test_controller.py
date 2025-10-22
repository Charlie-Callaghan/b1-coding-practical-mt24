"""Test the PDController implementation."""
import os
import sys
import numpy as np

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from uuv_mission.control import PDController
    from uuv_mission.dynamic import Submarine, ClosedLoop, Mission
except ImportError:
    # If running from within the uuv_mission directory
    from control import PDController
    from dynamic import Submarine, ClosedLoop, Mission

def test_controller():
    # Create a simple reference trajectory
    reference = np.array([0, 1, 2, 1, 0])
    cave_height = reference + 2
    cave_depth = reference - 2
    
    # Create test mission
    mission = Mission(reference, cave_height, cave_depth)
    
    # Create submarine and controller
    sub = Submarine()
    controller = PDController()
    
    # Create closed loop system
    closed_loop = ClosedLoop(sub, controller)
    
    # Run simulation with no disturbances
    disturbances = np.zeros(len(reference))
    trajectory = closed_loop.simulate(mission, disturbances)
    
    print("\nController Test Results:")
    print("------------------------")
    print(f"Reference trajectory: {reference}")
    print(f"Final submarine position: {trajectory.position[-1]}")
    print(f"Final depth: {sub.get_depth()}")
    
    return trajectory

if __name__ == "__main__":
    test_controller()