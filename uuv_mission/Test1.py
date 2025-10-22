import csv
import numpy as np
import sys
from dataclasses import dataclass

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

m1 = Mission.from_csv('b1-coding-practical-mt24/data/mission.csv')

print(m1)