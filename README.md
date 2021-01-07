
# PYSUM
This Tool calculates the BLOSUM Matrix (log-odds ratios) given arbitrary Sequences (can be anything, not only DNA or Amino-Acid). This is accomplished by following mathematical foundation:

$$
c_{i, j}^{k}=\left\{\begin{array}{ll}
\left(\begin{array}{c}
\left.n_{i}^{k}\right) \\
2
\end{array}\right) & \text { for } i=j \\
n_{i}^{k} n_{j}^{k} & \text { for } i>j
\end{array}\right.
$$
<img src="https://latex.codecogs.com/svg.latex?c_{i,%20j}^{k}"/>

# Usage
Packages required:

Python 3.6 or higher
numpy
tkinter

tkinter can be installed on Ubuntu 18.04 'sudo apt install python3-tk'
