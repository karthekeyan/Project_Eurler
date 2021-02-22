# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:17:54 2021

@author: uia76912
"""

max_value_of_series = int(input("Please enter the final value to be considered in fiboniacci series:"))

previous_term = 0
current_term = 1
next_term = 0
fibonacci_series = [0,1]
sum_of_even_values = 0

while next_term < max_value_of_series:
    next_term = previous_term + current_term
    fibonacci_series.append(next_term)
    previous_term = current_term
    current_term = next_term
    
    if (next_term % 2) == 0:
        sum_of_even_values += next_term
    
print("\n Fibonacci values are :\n", fibonacci_series)  
print("\n Sum of all even values:\n", sum_of_even_values)