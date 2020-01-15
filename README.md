Here you may find an implementation of non-relativistic electrostatic 1D code which solves Vlasov-Poisson system equations for an arbitrary number of charged particle population.
The method of solution is a so-called "particle-in-cell" algorithm: https://en.wikipedia.org/wiki/Particle-in-cell

Code uses the Anaconda3 package to operate

To run the code, type "python3 maxwell.py"

To generate plots for the particular run, type "python3 maxwell.py plot"

Raw output data and figures are saved in ./maxwell\_out/

Simulation configure file with parameters is named as "conf\_maxwell.py"

All source code may be found in "pic" folder, all tests are in "pic/tests"

Doxygen file is stored in "docs" folder
