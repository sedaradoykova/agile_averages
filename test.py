import csv
import numpy as np

def run_averages(file_input='number.csv', file_output='average.csv'):
 
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=float,  delimiter=',')
    
    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=0)[np.newaxis,:]

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')

run_averages('numbers.csv','output.csv')