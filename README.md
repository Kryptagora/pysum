
# PYSUM
This Tool calculates a **BLOSUM** Matrix (log-odds ratios) given arbitrary Sequences (can be anything, not only DNA or Amino-Acid) by **elimination**. This is accomplished by following mathematical foundation:
1. Given Sequences with at least p% identity to each other are clustered. The other sequences are **eliminated** (The degree decides, how similar they must be).

2. The sequences are now compared to each other, where the sequence letters (eg. DNA-Bases) are counted according to their frequency:
`ACTGTACG`

`TAGCTAGC`

`GTACGACC`

The columns k are observed, such that ![equation](https://latex.codecogs.com/svg.latex?k_1 ) would be then `ATG` and so on.  By computing the **C values** a matrix is obtained:
![equation](https://latex.codecogs.com/svg.latex?c_%7Bi%2C%20j%7D%5E%7Bk%7D%3D%5Cleft%5C%7B%5Cbegin%7Barray%7D%7Bll%7D%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20n_%7Bi%7D%5E%7Bk%7D%20%5C%5C%202%20%5Cend%7Barray%7D%5Cright%29%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Dj%20%5C%5C%20n_%7Bi%7D%5E%7Bk%7D%20n_%7Bj%7D%5E%7Bk%7D%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Ej%20%5Cend%7Barray%7D%5Cright.)
Note that this matrix is Symmetric.

3. The sum of all entry's in the Matrix is given by:  
![equation](https://latex.codecogs.com/svg.latex?c_%7Bi%2C%20j%7D%3D%5Csum_%7Bk%7D%20c_%7Bi%2C%20j%7D%5E%7Bk%7D)
and the factor for normalization:
![equation](https://latex.codecogs.com/svg.latex?Z%3D%5Csum_%7Bi%20%5Cgeq%20j%7D%20c_%7Bi%2C%20j%7D%3D%5Cfrac%7BL%20N%28N-1%29%7D%7B2%7D)
where *L* is the sequence length (column number, i.e. for `ACTGTACG`: L = 8) and *N* the number of sequences.

4. Then    ![equation](https://latex.codecogs.com/svg.latex?c_{i,j} ) is normalized to obtain the **Q-Matrix**:
![equation](https://latex.codecogs.com/svg.latex?q_%7Bi%2C%20j%7D%3D%5Cfrac%7Bc_%7Bi%2C%20j%7D%7D%7BZ%7D)

5. To obtain the probability of the occurrence of one sequence letter **i** use:
![equation](https://latex.codecogs.com/svg.latex?q_%7Bi%7D%3Dq_%7Bi%2C%20i%7D&plus;%5Csum_%7Bj%20%5Cneq%20i%7D%20%5Cfrac%7Bq_%7Bi%2C%20j%7D%7D%7B2%7D)

6. Finally the **log-odds ratios** are computed with:
![equation](https://latex.codecogs.com/svg.latex?%5Coperatorname%7BBLOSUM%7D_%7Bi%2C%20j%7D%3D%5Cleft%5C%7B%5Cbegin%7Barray%7D%7Bll%7D%202%20%5Clog%20_%7B2%7D%20%5Cfrac%7Bq_%7Bi%2C%20i%7D%7D%7Bq_%7Bi%7D%5E%7B2%7D%7D%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Dj%20%5C%5C%202%20%5Clog%20_%7B2%7D%20%5Cfrac%7Bq_%7Bi%2C%20j%7D%7D%7B2%20q_%7Bi%7D%20q_%7Bj%7D%7D%20%26%20%5Ctext%20%7B%20for%20%7D%20i%20%5Cneq%20j%20%5Cend%7Barray%7D%5Cright.)
The result (every entry) is rounded to integers.

# Usage
Packages required:

Python 3.6 or higher
numpy
tkinter

tkinter can be installed on Ubuntu 18.04 'sudo apt install python3-tk'
