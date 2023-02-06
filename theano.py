# -*- coding: utf-8 -*-
"""Theano.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QwpCdJSsPErSzMB4soGawuIgxZN3tbtR
"""

!pip install Theano

import theano

import theano.tensor as T

# Define two scalar variables
a = T.scalar('a')
b = T.scalar('b')

# Define a simple expression involving the two scalars
c = a + b

# Compile the expression into a callable function
f = theano.function([a, b], c)

# Evaluate the function with some sample inputs
result = f(2, 3)
print("Result:", result)

"""In this example, two scalar variables a and b are defined using T.scalar(). The expression c = a + b defines a simple addition operation between the two scalars. Finally, the expression is compiled into a callable function f using theano.function(). You can evaluate the function by passing in values for a and b. In this case, the result of f(2, 3) would be 5."""

import numpy as np
import theano.tensor as T

# Define two matrix variables
x = T.matrix('x')
y = T.matrix('y')

# Define a simple expression involving the two matrices
z = T.dot(x, y)

# Compile the expression into a callable function
f = theano.function([x, y], z)

# Evaluate the function with some sample inputs
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = f(matrix1, matrix2)
print("Result:")
print(result)

"""In this example, two matrix variables x and y are defined using T.matrix(). The expression z = T.dot(x, y) defines a dot product operation between the two matrices. Finally, the expression is compiled into a callable function f using theano.function(). You can evaluate the function by passing in matrices x and y. In this case, the result of f(matrix1, matrix2) would be array([[19, 22], [43, 50]])."""

import numpy as np
import theano.tensor as T

# Define two vector variables
x = T.vector('x')
y = T.vector('y')

# Define a simple expression involving the two vectors
z = x + y

# Compile the expression into a callable function
f = theano.function([x, y], z)

# Evaluate the function with some sample inputs
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
result = f(vector1, vector2)
print("Result:")
print(result)

"""In this example, two vector variables x and y are defined using T.vector(). The expression z = x + y defines a vector addition operation between the two vectors. Finally, the expression is compiled into a callable function f using theano.function(). You can evaluate the function by passing in vectors x and y. In this case, the result of f(vector1, vector2) would be array([5, 7, 9])."""