import numpy as np
from datetime import datetime
startTime = datetime.now()

ring0  = np.array([15, 16,  4,  7,  0, 16,  8,  4, 15,  7, 10,  1, 10,  4,  5,  3])
ring1a = np.array([18,  0,  9,  0, 13,  0, 13,  0, 18,  0, 10,  0, 10,  0,  7,  0])
ring1b = np.array([ 1,  8, 12,  8,  0,  9,  8,  6,  1, 10,  8,  8, 20, 10, 20,  9])
ring2a = np.array([ 0, 11,  0, 10,  0,  0,  0, 11,  0,  8,  0,  8,  0,  8,  0, 10])
ring2b = np.array([ 0, 19,  0,  0,  0, 20,  0, 19,  0, 15,  0, 12,  0, 13,  0,  0])
ring3  = np.array([10, 18, 14, 17, 11, 20,  8, 14, 12,  5, 11, 14,  3, 17,  8,  5])
ring4  = np.array([17,  0,  6,  0,  6,  0,  8,  0,  8,  0, 16,  0, 19,  0,  8,  0])

M = ring0.size

for shift_1b in np.arange(0, M, 2):
    for shift_2a in np.arange(0, M, 2):
        for shift_3 in np.arange(0, M, 2):
            for shift_4 in np.arange(0, M, 2):
                F = np.vstack([ring0, ring1a, np.roll(ring1b, shift_1b), 
                    np.roll(ring2a, shift_2a), np.roll(ring2b, shift_2a), 
                    np.roll(ring3, shift_3), np.roll(ring4, shift_4)])
                if np.unique(F.sum(axis=0)).size == 1:
                    print("found solution\n" + str(F))
                    print(datetime.now() - startTime)
                    exit()
