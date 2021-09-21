"""
Created on 7/8/21

@author: erika
"""

"""
This file cleans and filters titles in a CSV and rewrites the "title" column with the newly cleaned titles.
"""
from pandas import *
import re
import subprocess
import pandas as pd
import csv

# structural garbage
pageA = re.compile('Page Â')
pageUn1 = re.compile(r'Page  \[unnumbered\]')
pageUn2 = re.compile(r'Page \[unnumbered\]')
PageNum = re.compile(r'Page  [0123456789]')
pageNum = re.compile(r'page  [0123456789]')
Un = re.compile(r'\[unnumbered\]')
illust = re.compile(r'\[illustration\]')
Illust = re.compile(r'\[Illustration\]')
Chapter = re.compile('Chapter [0123456789]')
chapter = re.compile('chapter [0123456789]')
Chapt1 = re.compile(r'Chapt\. [0123456789]')
chapt1 = re.compile(r'chapt\. [0123456789]')
Chapt = re.compile('Chapt [0123456789]')
chapt = re.compile('chapt [0123456789]')
structural_garbage = [pageA, pageUn1, pageUn2, PageNum, pageNum, Un, illust, Illust, Chapter, chapter,
                      Chapt1, chapt1, Chapt, chapt]

# some punctuation
amper = re.compile('&')
dash = re.compile('[—-]')
apostrophe = re.compile("'")

# etc.
etc = re.compile('andc')

# text accents
above = re.compile('̄')
a = re.compile('[àáâãäå]')
A = re.compile('[ÀÁÂÃÄÅ]')
e = re.compile('[ęèéêë]')
E = re.compile('[ÈÉÊË]')
ii = re.compile('[ìíîï]')
II = re.compile('[ÌÍÎÏ]')
o = re.compile('[òóôõö]')
O = re.compile('[ÒÓÔÕÖ]')
u = re.compile('[ùúûü]')
U = re.compile('[ÙÚÛÜ]')
c = re.compile('ç')
C = re.compile('Ç')
ae = re.compile('æ')
AE = re.compile('Æ')
oe = re.compile('œ')
thorn = re.compile('[þÞ]')
B = re.compile('ß')

# finally, everything else (except hyphens and apostrophes)
everything = re.compile(r"[^a-zA-Z'\-1234567890 ]")

# then, attempt to get rid of roman numerals (except those containing exactly one I)
roman = re.compile(r"\b((?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?(I{0}|I{2,})))\b",
                   re.IGNORECASE)

# finally, remove extra spaces
spaces = re.compile(r" {2,}")

def clean_title(text):
    clean_titles = []

    for i in text:
        text1 = i.replace("\n", " ")

        temp = text1
        for trash in structural_garbage:
            temp = trash.sub("", temp)
        temp = amper.sub("and", temp)
        temp = dash.sub(" ", temp)
        temp = above.sub("", temp)
        temp = a.sub("a", temp)
        temp = A.sub("A", temp)
        temp = e.sub("e", temp)
        temp = E.sub("E", temp)
        temp = ii.sub("i", temp)
        temp = II.sub("I", temp)
        temp = o.sub("o", temp)
        temp = O.sub("O", temp)
        temp = u.sub("u", temp)
        temp = U.sub("U", temp)
        temp = c.sub("c", temp)
        temp = C.sub("C", temp)
        temp = ae.sub("ae", temp)
        temp = AE.sub("AE", temp)
        temp = oe.sub("oe", temp)
        temp = thorn.sub("th", temp)
        temp = B.sub("B", temp)
        temp = apostrophe.sub("", temp)

        # remove everything else, except for hyphens, apostrophes, letters, and spaces
        temp = everything.sub("", temp)

        # replace 'andc' artifact with &c
        # delete roman numerals (except for I)
        temp = etc.sub("&c", temp)
        temp = roman.sub("", temp)
        temp = spaces.sub(" ", temp)
        temp = temp.lower()

        clean_titles += [temp]

    print(clean_titles)
    return clean_titles

def make_csv():
    cols = ['title', 'author', 'date', 'text']
    rows = []
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('paul.csv')

def call_vard(jar_file, setup_folder, threshold, f_score, input_dir, search_subfolders, output_dir,use_normalization_cache):
  subprocess.call([
    'java',
    '-Xms256M',
    '-Xmx512M',
    '-jar',
    str(jar_file),
    str(setup_folder),
    str(threshold),
    str(f_score),
    str(input_dir),
    str(search_subfolders),
    str(output_dir),
    str(use_normalization_cache)
  ],
  timeout = 360)

if __name__ == '__main__':
    #make_csv()
    data = read_csv("C:/Users/erika/Downloads/Stpaul.csv")
    titles_list = data['title'].tolist()

    clean_titles_list = clean_title(titles_list)

    outFileName = 'C:/Users/erika/Downloads/clean_titles/' + 'titles' + '.txt'
    outFile = open(outFileName, "w")
    outFile.write("\n".join([str(elem) for elem in clean_titles_list]))
    outFile.close()
    print(len(clean_titles_list))

    call_vard("C:/Users/erika/Downloads/vard/VARD2.5.4/clui.jar",
              "C:/Users/erika/Downloads/vard/VARD2.5.4/default",
              "50",
              "1",
              "C:/Users/erika/Downloads/clean_titles",
              "false",
              "C:/Users/erika/Downloads/testvard",
              "true")

    my_file = open("C:/Users/erika/Downloads/testvard/varded(50%) - Changes Unmarked/titles.txt", "r")
    content = my_file.read()

    content_list = content.split("\n")
    my_file.close()
    print(content_list)

    authors_list = data['author'].tolist()
    dates_list = data['date'].tolist()
    texts_list = data['text'].tolist()

    make_csv()

    for i in range(len(content_list)):
        title_tc = content_list[i]
        author_tc = authors_list[i]
        date_tc = dates_list[i]
        text_tc = texts_list[i]
        set = [i, title_tc, author_tc, date_tc, text_tc]

        with open('paul.csv', 'a', encoding="utf-8") as f:  # change each time
            writer = csv.writer(f)
            writer.writerow(set)
