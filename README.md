# :blossom: PYSUM :blossom:
This Tool calculates a **BLOSUM** Matrix (log-odds ratios) given arbitrary Sequences (can be anything, not only DNA or Amino-Acid) by **elimination**. This is accomplished by following mathematical foundation:

1. Given Sequences with at least p% identity to each other are clustered. The other sequences are **eliminated** (The degree decides, how similar they must be).

2. The sequences are now compared to each other, where the sequence letters (eg. DNA-Bases) are counted according to their frequency. Looking at this example:\
`ATGTACGT`\
`TAGCTAGA`\
`GTACGACC`\
The columns k are observed, such that
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20k_1)
would be then `ATG` and so on.  By computing the **C values** a matrix is obtained:\
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20c_%7Bi%2C%20j%7D%5E%7Bk%7D%3D%5Cleft%5C%7B%5Cbegin%7Barray%7D%7Bll%7D%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20n_%7Bi%7D%5E%7Bk%7D%20%5C%5C%202%20%5Cend%7Barray%7D%5Cright%29%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Dj%20%5C%5C%20n_%7Bi%7D%5E%7Bk%7D%20n_%7Bj%7D%5E%7Bk%7D%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Ej%20%5Cend%7Barray%7D%5Cright.)
Note that this matrix is Symmetric.

3. The sum of all entry's in the Matrix and Z (normalization factor) is given by:  
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20c_%7Bi%2C%20j%7D%3D%5Csum_%7Bk%7D%20c_%7Bi%2C%20j%7D%5E%7Bk%7D%20%5Ctext%7B%20and%20%7D%20Z%3D%5Csum_%7Bi%20%5Cgeq%20j%7D%20c_%7Bi%2C%20j%7D%3D%5Cfrac%7BL%20N%28N-1%29%7D%7B2%7D)\
where *L* is the sequence length (column number, i.e. for `ATGTACGT`: L = 8) and N the number of sequences.

4. Then,
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20c_{i,j})
is normalized to obtain the **Q-Matrix**:\
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20q_%7Bi%2C%20j%7D%3D%5Cfrac%7Bc_%7Bi%2C%20j%7D%7D%7BZ%7D)

5. To obtain the probability of the occurrence of one sequence letter **i** use:\
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20q_%7Bi%7D%3Dq_%7Bi%2C%20i%7D&plus;%5Csum_%7Bj%20%5Cneq%20i%7D%20%5Cfrac%7Bq_%7Bi%2C%20j%7D%7D%7B2%7D)

6. Finally the **log-odds ratios** are computed with:\
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B300%7D%20c_%7Bi%2C%20j%7D%5E%7Bk%7D%3D%5Cleft%5C%7B%5Cbegin%7Barray%7D%7Bll%7D%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20n_%7Bi%7D%5E%7Bk%7D%20%5C%5C%202%20%5Cend%7Barray%7D%5Cright%29%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Dj%20%5C%5C%20n_%7Bi%7D%5E%7Bk%7D%20n_%7Bj%7D%5E%7Bk%7D%20%26%20%5Ctext%20%7B%20for%20%7D%20i%3Ej%20%5Cend%7Barray%7D%5Cright.)\
The result (every entry) is rounded to integers.

This calculation is based on Dr. Sepp Hochreiters Script `Bioinformatics I` .

## Usage
To execute this application, `python3` is required. \
Also, following python packages are required:

| package  | version |
| -------  | ------- |
| numpy    | <= 1.18 |
| tkinter  | <= 8.6  |


Note that `tkinter` is installed by default on `Windows10`, but not on `Linux`.

To run this application, go to the folder where the `main.py` is located and open the command prompt in it. Then run the application by typing:
`python3 main.py`

You can also run this application without a GUI, by typing:
`python3 main.py --nogui --path path_to_sequnce_file --degree [0,100]`


## Input Files
The Input file can end with any extension.
The sequences in the input file should fulfill following propertys:
* Be all the same length.
* Every sequence is separated by a newline.
* At least two sequences are given.
* Any input line starting with `-` will be ignored.

Examples:
**Valid** ✅
```
-This is a valid input file, this line is ignored.
TACGTAGCTAGC
TGCATGCTAGCC
TGCTGCTGCCCA
TGTGTACACCCC
-This line is also ignored.
```
**Not Valid** ⛔️
```
-This is a invalid input file, because sequences differ in length.
TACGTAGCTAGC
TGCATGCT
TGCTGCTGCCCA
TGTGTACACCC
```
