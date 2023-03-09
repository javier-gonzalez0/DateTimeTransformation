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
from datetime import datetime, timedelta



if __name__ == '__main__':
    print("User must enter the time zone they are in, for ")
    print("default please press enter without hitting a key")
    print("The user must enter a string in the following format:")
    #print("     mm/dd/yyyy hh:mm")
    timestring = input("     mm/dd/yyyy hh:mm")
    input_mon = int(timestring[0:2])
    input_day = int(timestring[3:5])
    input_year = int(timestring[6:10])
    input_hour = int(timestring[11:13])
    input_min = int(timestring[14:16])

    ValidDate = None

    try:
        currentdate = datetime(year=input_year,month=input_mon,day=input_day,
                                        hour=input_hour,minute=input_min)
        ValidDate = True
    except ValueError:
        ValidDate = False
        if str(ValueError) == "month must be in 1..12":
            print("YOU MUST ENTER CORRECT MONTH INFO")
    print(str(ValidDate))
    print(":::",str(ValueError),":::")
    print(":::",ValueError,":::")
