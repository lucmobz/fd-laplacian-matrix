# Finite difference laplacian

* Like the MATLAB functions (see their doc)
* Not platform independent

`./numgrid.py <nodes-per-direction>` generates a binary matrix `G.bin` (2 * `int32` containing the size of the matrix + `<nodes-per-direction>` * `int32`) that contains a numbering of the finite difference grid nodes.

`./delsq.py G.bin` generate a binary matrix `D.bin` (2 * `int32` + (`<nodes-per-direction>` - 1)^2 * `float64`) that contains the weights of the 5-point stencil finite difference scheme for the laplace equation.

Solve the system somehow by `u = numpy.linalg.inv(D) @ rhs` and get the dof values on a grid to plot in 2D `U[G > 0] = u[G[G > 0]]`
