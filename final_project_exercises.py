# Final Project Exercises
# Lindsay Amendola
# Carli Peters
# 22 December 2020

# Exercise 1
import numpy as np 
import matplotlib as plt
def tentmap(y, n):
 # need to create lists for input and output
 inp = np.array([])
 out = np.array([])
 for i inp range(1, n):
 	inp = np.append(inp, y)
 	if y < 0.5:
 		y = 2*y
 	elif y >= 0.5:
 		y = 2 - 2 * y
 	out = np.append(out, y)
 print(inp)
 print(out)
 tentmap(0.34685264,3)


