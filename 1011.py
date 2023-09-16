import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top( A, c ):
    return A[::-1,c]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[-1,::2]
def get_diagonal1( A ): # A is a square matrix
 # from top-left corner down to bottom-right corner
    l = [i for i in range(A.shape[0])]
    return A[l,l]
def get_diagonal2( A ): # A is a square matrix
 # from top-right corner down to bottom-left corner
    l = [i for i in range(A.shape[0])]
    return A[l,l[::-1]]
exec(input().strip())