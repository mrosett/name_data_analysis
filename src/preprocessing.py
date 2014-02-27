'''
Created on Feb 25, 2014

@author: Max
'''

import csv
import os

def joinCSV(inFolder, outPath, useFileNames = False):
    print(inFolder)
    outWriter = csv.writer(open(outPath,'w'),lineterminator='\n')
    for file in os.listdir(inFolder):
        if file.lower().endswith('.txt') or file.lower().endswith('.csv'):
            inReader = csv.reader(open(inFolder + file,'r'))
            print(file)
            for row in inReader:
                if useFileNames:
                    row = [file[:-4]] + row
                outWriter.writerow(row)
        else: print('Ignored file: ' + file)
             
             
#nPath = './../data/originals/national/'
#[os.rename(nPath + f, nPath+f[3:]) for f in os.listdir(nPath) if f.startswith('yob')]

#joinCSV('./../data/originals/states/','./../data/processed/allStates.csv')
joinCSV('./../data/originals/national/','./../data/processed/national.csv',useFileNames = True)
