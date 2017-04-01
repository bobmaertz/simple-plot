#plotter.py
#Created: 01/09/2016
#Author: Bob Maertz
#Description: Very simple script to batch plot csv/txt files containing x,y data.
#license: 


import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import datetime

class Plotter():
    file = None
    plot_title  = 'PT Curve'
    plot_xlabel = 'Time'
    plot_ylabel = 'Pressure'
    plot_label = 'PT Curve for :' #can remove too.
    plot_color = 'r' #Red for default - b, g, y (blue, green, yellow, etc..)
    figure = None
    showPlot = 1  #if set to 0, wont show plot.
    savePlot = 1  #if set to 0, wont save file.
    showPlotLabel = 1 #if set to 0, wont show line label.

    def __init__(self, file):
        self.file = file
    
    def plot_results(self, x,y):
        self.figure = plt.figure()
    
        ax1 = self.figure.add_subplot(1,1,1)
    
        ax1.set_title(self.plot_title)
        ax1.set_xlabel(self.plot_xlabel)
        ax1.set_ylabel(self.plot_ylabel)
        
        if self.showPlotLabel:
            ax1.plot(x,y, c=self.plot_color, label=self.plot_label)
        else:
            ax1.plot(x,y, c=self.plot_color)
        
        leg = ax1.legend()
        
        if self.showPlot:
            plt.show()

    def save_plot(self):
        if self.save_plot:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            image_filename = os.path.splitext(self.file)[0] +'_'+timestamp+'_plot.jpg'
            self.figure.savefig(image_filename)
    
    def plot_file(self):
        file_extension = os.path.splitext(self.file)[1][1:].strip().lower()
        if file_extension == 'txt':
            with open(self.file) as f:
                data = f.read()
            print('Plotting '+self.file)
            data = data.split('\n')
            x = [row.split(' ')[0] for row in data]
            y = [row.split(' ')[1] for row in data]
            self.plot_results(x,y)
            self.save_plot()
        elif file_extension == 'csv':
            print('Plotting '+self.file)
            data = np.genfromtxt(self.file, delimiter=' ', names=['x', 'y'])
            x = data['x']
            y = data['y']
            self.plot_results(x,y)
            self.save_plot()
        else:
            print('Ignoring a non-txt/csv file.')


def main():

    file = raw_input('Enter the filename (full path if it is not in the same directory): ')
    plotter = Plotter(file)
    if os.path.isfile(file):
        plotter.plot_file()
    elif os.path.isdir(file):
        directory = file
        for batch_file in os.listdir(directory):
            plotter = Plotter(batch_file)
            plotter.plot_file()
    else:
        print('There was an error. Exiting.')
        exit()
        

if __name__ == "__main__":
    main()
