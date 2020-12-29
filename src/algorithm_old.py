import difflib
import numpy as np
from tqdm import tqdm
import itertools
from utils import matrix_repr

print('PYSUM - BLOSUM CALCULATION TOOL')
print('#'*20)

# xx_matrix = int(input('Enter the BLOSUMxx grade as number between [0,100]: '))
# xx_matrix = xx_matrix/100

# if xx_matrix < 0 or xx_matrix > 100:
#     raise ValueError('Invalid Value for BLOSUMxx grade!')
#
# seq_array = []
# i = 0
# while True:
#     input_user = str(input(f'Enter {i+1}. Sequence or type "end" to proceed.\n'))
#
#     if input_user.lower() == 'end':
#         break
#     else:
#         seq_array.append(input_user)
#         i += 1

xx_matrix = 0.85
#seq_array = ['ATGGAATCCC', 'ATGGAATCCA', 'ATAAATTCCA', 'ATTGACACCA', 'GATGAATCCT', 'GAGTTATCGA']
seq_array = ['ATGGAATCCA', 'ATAAATTCCA', 'ATTGACACCA', 'GATGAATCCT', 'GAGTTATCGA']

# elimination of similar sequnces
for ignore_index, seq_1 in enumerate(tqdm(seq_array)):
    for i, seq_2 in enumerate(seq_array, 0):
        if ignore_index == i:
            continue

        similarity = difflib.SequenceMatcher(None, seq_1, seq_2).ratio()
        if similarity > xx_matrix:
            seq_array.pop(i)

# array with len(seq_arrays) entrys and these entries are long as one arbitrary sequnce.
array = np.empty(shape=(len(seq_array), len(seq_array[1])), dtype=np.str)

#pack sequences in numpy array
for i in range(len(array)):
    array[i] = list(seq_array[i])

# flatten the array and get all combinations from the sequences
seq_combinations = list(itertools.permutations(''.join(array.flatten(order='C')),2))
seq_letters = []
for x in ''.join(array.flatten(order='C')):
    if not x in seq_letters:
        seq_letters.append(x)
seq_letters = sorted(seq_letters)

counts = {}
for c in seq_combinations:
    c = ''.join(c)
    counts[c] = 0

for i in range(len(array[0])):
    #print(len(list(itertools.combinations(''.join(array[:, 0]),2))))
    #print(array[:, i])
    for p in itertools.combinations(array[:, i], 2):
        combination = ''.join(p)
        if combination != combination[::-1]:
            counts[combination] += 1
            counts[combination[::-1]] += 1
        else:
            counts[combination] += 1

c_values = dict(sorted(counts.items()))

# create counting matrix
c_matrix = np.zeros(shape=(len(seq_letters)**2), dtype=np.int64)
for i, val in enumerate(c_values.values()):
    c_matrix[i] = val
c_matrix = c_matrix.reshape((len(seq_letters), len(seq_letters)))

# compute the q values
total = np.sum(np.triu(c_matrix)) # np.triu gives us upper triangle of matrix
q_matrix = c_matrix / total

p_values = []
idx = 0
# compute p values
for column in q_matrix.T:
    p_values.append(column[idx] + 1/2*(sum(column[np.arange(len(column)) != idx])))
    idx += 1

log_odds = np.zeros(shape=(c_matrix.shape), dtype=np.float64)
print(p_values)

for i, j in np.ndindex(q_matrix.shape):
    if i == j:
        log_odds[i, j] = 2*np.log2((q_matrix[i, i])/(p_values[i]**2))
    else:
        log_odds[i, j] = 2*np.log2((q_matrix[i, j])/(2*p_values[i]*p_values[j]))

print(log_odds.round())
