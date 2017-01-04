## Notebooks for the CMWR 2016 pySOT talk
The directory contains the following files:

* Example1.ipynb: Introductory example on serial + threaded
* Example2.ipynb: Animation that shows the 1D sample pattern
* Example3.ipynb: Example on how to implement our own optimization problem
* Example4.ipynb: Example that shows how to use pySOT with an external MATLAB objective function. You need to have MATLAB installed to run this notebook.
* Example5.ipynb: Example of an optimization problem with non-bound constraints
* Example6.ipynb: Example of an optimization problem with an equality constraint that is easy to project on
* Example7.ipynb: Example with a C++ objective function that crashes with probability 10%. You need a C++ compiler. The following should be enough in order to compile the source code (g++ -std=c++11 sphere\_ext.cpp -o sphere\_ext)

The following help files are also in the directory:

* Ackley.py: The Ackley function, to be used with the GUI
* Keane.py: The Keane function, to be used with the GUI
* matlab_ackley.m: The Ackley function, using in Example4
* sphere\_ext.cpp: Used in Example7

David Eriksson, June 20, 2016
