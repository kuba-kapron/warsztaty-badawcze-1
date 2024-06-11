from structuregenerator.generator import *
from points_io import save_points_as_pdb

initial_structures = ['line', 'random_walk', 'self_avoiding_random_walk']

structures = []

# structures.append(baseball(2000))
# structures.append(circle(2000))
# structures.append(constant_angle(2000))
# structures.append(gas(2000))
# structures.append(img_ds(2000))
# structures.append(img_gas(2000))
# structures.append(img_tsp(2000))
structures.append(line(2000))
structures.append(random_walk(2000))
structures.append(self_avoiding_random_walk(2000))
# structures.append(spiral_sphere(2000))

for initial_structure, structure in zip(initial_structures, structures):
    save_points_as_pdb(structure, f'{initial_structure}/initial_structure.pdb')