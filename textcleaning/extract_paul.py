"""
Created on 7/13/2021

@author: erika
"""

'''This file takes a csv file, extracts sections of text containing words relevant to 
St Paul's, and removes texts without relevance to St. Paul's. Exports dataframe as a csv'''

import numpy as np
import pandas as pd

#Takes a text and extracts the 10 words before and after a key word
#and returns a string of all the chunks

def extract(txt):
    text = txt.lower()
    pt2 = ["paul", "paul's", "faith", "faith's", "paule", "paule's", "pauls", "paules", "faiths"] # These are our key words but feel free to change it!
    new = text.split(" ")
    st = ["st", "st.", "saint"]
    list = []
    idx = 0
    for word in new:
        if (word in st) and (new[idx+1] in pt2):
            if idx > 9:
                sublist = new[idx-10:idx+10]
                for i in sublist:
                    list.append(i)
            elif idx <= 9:
                sublist = new[0:idx+10]
                for i in sublist:
                    list.append(i)
        idx += 1
    return " ".join(list)


if __name__ == '__main__':

    infile = open("D://csv/combined_filtered_2.csv", "r", encoding='latin-1')
    sample = pd.read_csv(infile)

    for row in sample.index:

        cell = extract(sample['text'][row])
        sample.at[row, 'text'] = cell

    # this section drops all rows with null cells
    sample.replace('', np.nan, inplace=True)
    sample.dropna(inplace=True)

    print(sample)

    sample.to_csv('combined_text.csv')




