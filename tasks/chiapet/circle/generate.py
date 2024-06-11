from structuregenerator.generator import random_walk
from points_io import save_points_as_pdb

structure = random_walk(2000)
save_points_as_pdb(structure, 'initial_structure.pdb')