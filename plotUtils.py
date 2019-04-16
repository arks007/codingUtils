'''
Author: Sujoy Purkayastha
Last modified: 4/15/19
Description: A python utility file that will streamline the generation of scientific plots using numpy and matplotlib
'''

import matplotlib.pyplot as plt
import numpy as np

#this function plots the elements in numpy array, npArray.
#x-axis: index of element
#y-axis: value of element
#npArray: 1D array of elements to plot
#plotName: title of the plot
#display: a boolean whether or not to display a plot
#save: a numpy array --> [0: boolean, 1: string path+name, 2: string file type]
def simplePlot(npArray, plotName, display, save):
    plt.plot(npArray)
    plt.title(plotName)
    plt.ylabel('Element Value')
    plt.xlabel('Element Index')
    plt.axis([0, npArray.size - 1, 0, np.amax(npArray)])
    if(display):
        plt.show()
    if(save[0]):
        plt.savefig(save[1] + save[2], bbox_inches='tight')


#indVar: a numpy array representing the x-value of a point
#indVarName: the name of the independent variable
#depVar: a numpy array representing the y-value of a point
#depVarName: the name of the dependent variable
#plotName: title of the plot
#pointType: the color and shape of a graphed point as a string
#display: a boolean whether or not to display a plot
#save: a numpy array --> [0: boolean, 1: string path, 2: string file type]
def simplePlot2D(indVar, indVarName, depVar, depVarName, plotName, pointType, display, save):
    plt.plot(indVar, depVar, pointType)
    plt.title(plotName)
    plt.ylabel(depVarName)
    plt.xlabel(indVarName)
    plt.axis([0, np.amax(indVar) + 1, 0, np.amax(depVar) + 1])
    if(display):
        plt.show()
    if(save[0]):
        plt.savefig(save[1] + save[2], bbox_inches='tight')

#Z suffix reinforces that this is a GENERAL PURPOSE multiple plot generator 
#it is recommended to use a helper method that will read the parameters off a text file 
#indVarZ: a 2D numpy array holding multiple sets of x-values of points
#indVarNameZ: a numpy array holding the names of the independent variables
#depVarZ: a 2D numpy array holding multiple sets of y-values of points
#depVarNameZ: a numpy array holding the names of the dependent variables
#numRows: number of rows 
#numCols: number of cols 
#plotNameZ: a numpy array holding the names of the plots
#pointTypeZ: a numpy array holding the colors and shapes of a graphed points as strings
#display: a boolean whether or not to display a plot
#save: a numpy array --> [0: boolean, 1: string path, 2: string file type]
def multiPlot(indVarZ, indVarNameZ, depVarZ, depVarNameZ, numRows, numCols, numPlotZ, plotNameZ, pointTypeZ, display, save):
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.5, wspace = 0.5)
    for i in range(1, numPlotZ + 1):
        fig.add_subplot(numCols, numCols, i) 
        plt.plot(indVarZ[i - 1], depVarZ[i - 1], pointTypeZ[i - 1])
        plt.title(plotNameZ[i - 1])
        plt.ylabel(depVarNameZ[i - 1])
        plt.xlabel(indVarNameZ[i - 1])
        plt.axis([0, np.amax(indVarZ[i - 1]) + 1, 0, np.amax(depVarZ[i - 1]) + 1])
    if(display):
        plt.show()
    if(save[0]):
        plt.savefig(save[1] + save[2], bbox_inches='tight')



save = np.array([False, '', ''])

#1
x = np.array([0, 1, 2, 3, 4, 5])
simplePlot(x, 'Test', True, save)


#2
a = np.array([1, 2, 3, 4])
b = np.array([1, 4, 9, 16])
simplePlot2D(a, "independent variable",  b, 'dependent variable', 'Simple 2D Plot', 'ro', True, save)

#3
iVarZ = np.array([[1, 2, 3], [1, 2, 3]])
iVarNameZ = np.array(['inputs', 'inputs'])
dVarZ = np.array([[1, 4, 9], [1, 8, 27]])
dVarNameZ = np.array(['inputs squared', 'inputs cubed'])
numRows = 1
numCols = 2
numPlotZ = 2
plotNameZ = np.array(['Squared', 'Cubed'])
pointTypeZ = np.array(['ro', 'ro'])
display = True
multiPlot(iVarZ, iVarNameZ, dVarZ, dVarNameZ, numRows, numCols, numPlotZ, plotNameZ, pointTypeZ, display, save)
