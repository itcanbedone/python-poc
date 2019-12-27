#!/usr/bin/env python

from matrix import Matrix

matrix0 = Matrix("1 2\n3 4")
print matrix0.row(2)

matrix1 = Matrix("1")
print matrix1.row(1)

matrix2 = Matrix("1")
print matrix2.column(1)


