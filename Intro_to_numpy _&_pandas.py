# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:57:41 2018

@author: VijayBalaji
"""
#Creating Arrays
import numpy as np

my_list1 = [1,2,3,4]

my_array1=np.array(my_list1)

my_array1

array([1, 2, 3, 4])

my_list2=[11,22,33,44]

my_list=[my_list1,my_list2]

my_array2=np.array(my_list)

my_array2

my_array2.shape

my_array2.dtype

np.zeros(5)

my_zeros_array=np.zeros(5)

my_zeros_array.dtype

np.empty(5)

array([ 0.,  0.,  0.,  0.,  0.])

np.eye(5)

np.arange(10)

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(1,10,2)

array([1, 3, 5, 7, 9])
