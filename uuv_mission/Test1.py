import csv
import numpy as np
import sys
import os
from dataclasses import dataclass

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from uuv_mission.terrain import generate_reference_and_limits
except ImportError:
    # If running from within the uuv_mission directory
    from terrain import generate_reference_and_limits

@dataclass
class Mission:

    reference: np.ndarray
    cave_height: np.ndarray
    cave_depth: np.ndarray

    @classmethod
    def random_mission(cls, duration: int, scale: float):
        (reference, cave_height, cave_depth) = generate_reference_and_limits(duration, scale)
        return cls(reference, cave_height, cave_depth)

    @classmethod
    def from_csv(cls, file_name: str):

        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            ref_vals, h_vals, d_vals = [], [], []

            for row in reader:
                ref_vals.append(float(row[0]))
                h_vals.append(float(row[1]))
                d_vals.append(float(row[2]))

        return cls(np.array(ref_vals, dtype=float),
                   np.array(h_vals, dtype=float),
                   np.array(d_vals, dtype=float))

import os

# Get the absolute path to the data directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_path = os.path.join(project_root, 'data', 'mission.csv')

try:
    m1 = Mission.from_csv(data_path)
    print("Mission data loaded successfully:")
    print(f"Reference points: {len(m1.reference)}")
    print(f"Height points: {len(m1.cave_height)}")
    print(f"Depth points: {len(m1.cave_depth)}")
    print("\nFirst few values:")
    print(f"Reference: {m1.reference[:5]}")
    print(f"Heights: {m1.cave_height[:5]}")
    print(f"Depths: {m1.cave_depth[:5]}")
except Exception as e:
    print(f"Error loading mission data: {e}")