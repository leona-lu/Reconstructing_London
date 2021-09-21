"""
Created on 7/13/2021

@author: erika
"""

"""
This file combines multiple csv's in a folder
"""

import os
import glob
import pandas as pd

if __name__ == '__main__':
    os.chdir("D://csv")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    # export to csv
    combined_csv.to_csv("combined_filtered_2.csv", index=False, encoding='utf-8-sig')
