#################################
#   Javier Gonzalez             #
#   UTSA ECE                    #
#   CS 5103                     #
#################################

# Useful Material below
# https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn
# https://scikit-learn.org/stable/modules/neighbors.html#neighborhood-components-analysis
# http://archive.ics.uci.edu/ml/datasets/Iris

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay


if __name__ == '__main__':
    print("User must enter the time zone they are in, for ")
    print("default please press enter without hitting a key")
    print("The user must enter a string in the following format:")
    #print("     mm/dd/yyyy hh:mm")
    timestring = input("     mm/dd/yyyy hh:mm")
    mon = timestring[0:2]
    day = timestring[3:3]
    year = timestring[6:10]
    hour = timestring[11:13]
    min = timestring[14:16]
