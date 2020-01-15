# AST506 / APC524 Plasma PiC


Authors: Nijaid Arredondo (nijaid@princeton.edu),
         Kirill Lezhnin (klezhnin@princeton.edu),
         Sirawich Pipatprathanporn (sirawich@princeton.edu).

Here you may find an implementation of non-relativistic electrostatic 1D code which solves Vlasov-Poisson system equations for an arbitrary number of charged particle population.
The method of solution is a so-called "particle-in-cell" algorithm, which is described in https://en.wikipedia.org/wiki/Particle-in-cell.

# Requirements

For running simulations:
  * **Python 3**
    * **numpy**
    * **scipy**

To use the included post-processing (plotting), **matplotlib** is required.
For running tests, **pytest** is required.
For compiling the documentation, **Doxygen** is required.

# Installation

The code itself needs no compiling.
Hooray for interpreted languages!

# Documentation

To obtain documentation, run in the command line:
```
cd docs/
doxygen
```
This will produce an [HTML](docs/html/index.html) and a [LaTeX](docs/latex/refman.tex).
The latter can be made into a PDF if **LaTeX** is installed.
Enter in the command line:
```
cd docs/latex/
make
```

# Tests

Tests can be run easily having installed **pytest**.
In this directory, simply run
```
pytest
```

# Running Simulations

Simulations can be ran by providing a driver code in this directory and then
utilizing the modules in `pic/`.
It is intended to be ran as
```
python [driver]
```
An example is provided below.

## 1D Maxwell Model

The included model is a 1D electrostatic model that distributes particle energies
with a Maxwellian distribution.
Its parameters are initialized in `conf_maxwell.py`, then ran by the driver `maxwell.py`.
Once the parameters have been set, the simulation is run:
```
python maxwell.py
```
The output positions and momenta of ions and electrons will then be saved in `ion_#.out`
and `elec_#.out`, respectively.
The values of the electric field will be saved as `ex_#.out`.
The `#` is the iteration number of the simulation.
The grid is saved in `grid.out`.
All output is under the directory name specified in `conf_maxwell.py`.

# Post-Processing

While the output data can be gathered and analyzed by the user, we provide a
rough plotting routine with **matplotlib**.
At each data output iteration, a plot of the following is provided:
  * phase space
  * phase space histogram
  * electric field over the grid
  * Fourier transform of the field

These are made by entering:
```
python [driver] plot
```
