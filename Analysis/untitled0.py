#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:25:00 2018

@author: Kartik
"""


#Subarray with day i - day (i-1) price difference

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

#Mid index is 7~18
#Low = 0
#High = 15

#Creating a function to return an array in reverse from a given midpoint

def reverse(A, mid):
    B = []
    i = mid
    while i >= 0:
        B.append(A[i])
        i = i-1
    return(B)

#Find Max-Crossing-Subarray
def max_crossing_sub(A, low, mid, high):
    left_sum = -100000
    summ = 0
    B = reverse(A, 7)
    for i in range(low, mid):  #Don't know how to do range(mid, low) so creating a function reverse
        summ = summ + B[i]
        if summ > left_sum:
            left_sum = summ
            max_left = mid - i #Because array is reversed 
    right_sum = -10000
    summ = 0
    for j in range((mid + 1), high):
        summ = summ + A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
    return (max_left, max_right, (left_sum+right_sum))

max_crossing_sub(A,0,7,15)

#Find Max subarray

