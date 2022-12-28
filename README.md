# Mean-Variance-Standard Deviation Calculator

This is the boilerplate for the Mean-Variance-Standard Deviation Calculator project. 
Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

## Steps

![cal](https://user-images.githubusercontent.com/7541585/209807233-f4e6b5ea-bdd8-4915-aa8f-367eede95dab.jpg)

## Description

### Input

The input of the function is a list containing 9 digits `lst=[0,1,2,3,4,5,6,7,8]`

### Calculation Process

The function converts the list into a 3 x 3 NumPy array `function=np.array(lst).reshape((3,3))` 

And if `len(lst) !=9` the function raises a `ValueError` with message `'List must contain nine numbers.'`

### Output

The calculator returns a dictionary containing the `mean, variance, standard deviation, max, min, and sum` along both axes and for the flattened matrix.

The calculator uses NumPy to output the 

- mean 
- variance 
- standard deviation 
- max 
- min
- sum 

