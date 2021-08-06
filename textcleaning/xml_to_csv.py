"""
Created on 6/26/2021

@author: erika
"""

"""
Iterates through folders, imports xml file, cleans the text, finds date, title, author, calls VARD on text, 
creates csv and places each file in a row in csv
"""

from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import os.path
import csv
import subprocess
import glob

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
apos = re.compile("'")

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
everything = re.compile(r"[^a-zA-Z'\- ]")

# then, attempt to get rid of roman numerals (except those containing exactly one I)
roman = re.compile(r"\b((?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?(I{0}|I{2,})))\b",
                   re.IGNORECASE)

# finally, remove extra spaces
spaces = re.compile(r" {2,}")

def clean_text():
    bodies = soup.find_all('div')
    text = ''
    for i in bodies:
        text += i.get_text()

    text1 = text.replace("\n", " ")

    temp = text1
    for trash in structural_garbage:
        temp = trash.sub("", temp)
    temp = amper.sub("and", temp)
    temp = dash.sub(" ", temp)
    temp = apos.sub("", temp)
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

    # remove everything else, except for hyphens, apostrophes, letters, and spaces
    temp = everything.sub("", temp)

    # replace 'andc' artifact with &c
    # delete roman numerals (except for I)
    temp = etc.sub("&c", temp)
    temp = roman.sub("", temp)
    temp = spaces.sub(" ", temp)
    temp = temp.lower()

    return temp


# text date, extract date from index 1 of dates, (manually change index)
def find_date():
    dates = soup.find_all('date')
    date = dates[0].get_text()
    date_str = ''
    for i in date:
        if i in '1234567890':
            date_str += i
    if len(date_str) == 3:
        date_str = date_str  # turns 168 to 1685
    if len(date_str) >= 8:
        date_str = date_str[0:4]  # turns 1658-1659 to 1598
    if len(date_str) == 6:
        date_str = date_str[2:6]  # turns a date to only the year

    return date_str

# extract information from file, change if needed
def parse_xml():
    titles = soup.find_all('title')
    title = ''
    for i in titles:
        title = i.get_text()

    author = ''
    authors = soup.find_all('author')
    for i in authors:
        author = i.get_text()


    return title, author

# make empty csv file
def make_csv():
    cols = ['title', 'author', 'date', 'text']
    rows = []
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('P5.csv')     # change each time

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
    row_list = []
    make_csv()
    rootdir = "C:/Users/erika/Documents/eebo" # change each time
    #"C:/Users/erika/Documents/eebo"

    num = 0
    exception_files = []
    for subdir, dir, files in os.walk(rootdir):
        file_num = 0
        for filename in files:
            if filename.endswith('.xml') and (filename[0] == 'A' or filename[0] == 'B'):

                infile = open(os.path.join(subdir, filename), "r", encoding = 'utf-8')
                contents = infile.read()
                soup = BeautifulSoup(contents, "xml")

                print(os.path.join(subdir, filename))
                if len(find_date()) != 0:       #does not include roman numeral years
                    date_int = int(find_date())
                    if date_int >= 1600 and date_int <= 1700:  # sets range
                        num += 1
                        title_data, author_data = parse_xml()
                        pretxt = clean_text()

                        txt = pretxt.replace("to the extent possible under law the text creation partnership has waived all copyright and related or neighboring rights to this "
                                           "keyboarded and encoded edition of the work described above according to the terms of the public domain dedication "
                                           "httpcreativecommonsorgpublicdomainzero this waiver does not extend to any page images or other supplementary files associated with this "
                                           "work which may be protected by copyright or other license restrictions please go to httpswwwtextcreationpartnershiporg for more "
                                           "information about the projectcreated by converting tcp files to tei p using tcpteixsl tei oxford eebo-tcp is a partnership between the "
                                           "universities of michigan and oxford and the publisher proquest to create accurately transcribed and encoded texts based on the image "
                                           "sets published by proquest via their early english books online eebo database httpeebochadwyckcom the general aim of eebo-tcp is to "
                                           "encode one copy usually the first edition of every monographic english-language title published between and available in eeboeebo-tcp "
                                           "aimed to produce large quantities of textual data within the usual project restraints of time and funding and therefore chose to create "
                                           "diplomatic transcriptions as opposed to critical editions with light-touch mainly structural encoding based on the text encoding "
                                           "initiative httpwwwtei-corgthe eebo-tcp project was divided into two phases the texts created during phase of the project - initially "
                                           "available only to institutions that contributed to their creation were released into the public domain on january the approximately "
                                           "texts produced during phase - of which had been released as of originally similarly restricted were similarly freed from all "
                                           "restrictions on august as of that date anyone is free to take and use these texts for any purpose modify them annotate them distribute "
                                           "them etc but we do respectfully request that due credit and attribution be given to their original sourceusers should be aware of the "
                                           "process of creating the tcp texts and therefore of any assumptions that can be made about the datatext selection was based on the new "
                                           "cambridge bibliography of english literature ncbel if an author or for an anonymous work the title appears in ncbel then their works "
                                           "are eligible for inclusion selection was intended to range over a wide variety of subject areas to reflect the true nature of the "
                                           "print record of the period in general first editions of a works in english were prioritized although there are a number of works in "
                                           "other languages notably latin and welsh included and sometimes a second or later edition of a work was chosen if there was a compelling "
                                           "reason to do soimage sets were sent to external keying companies for transcription and basic encoding quality assurance was then "
                                           "carried out by editorial teams in oxford and michigan or pages whichever is the greater of each text was proofread for accuracy and "
                                           "those which did not meet qa standards were returned to the keyers to be redone after proofreading the encoding was enhanced andor "
                                           "corrected and characters marked as illegible were corrected where possible up to a limit of instances per text any remaining illegibles"
                                           " were encoded as gaps understanding these processes should make clear that while the overall quality of tcp data is very good some "
                                           "errors will remain and some readable characters will be marked as illegible users should bear in mind that in all likelihood such "
                                           "instances will never have been looked at by a tcp editorthe texts were encoded and linked to page images in accordance with level of "
                                           "the tei in libraries guidelinescopies of the texts have been issued variously as sgml tcp schema ascii text with mnemonic sdata "
                                           "character entities displayable xml tcp schema characters represented either as utf- unicode or text strings within braces or lossless "
                                           "xml tei p characters represented either as utf- unicode or tei g elementskeying and markup guidelines are available at the text creation"
                                           " partnership web site", "")

                        try:
                            # deletes contents of folder containing text to be varded
                            text_files = glob.glob('C:/Users/erika/Downloads/text/*')
                            for tf in text_files:
                                os.remove(tf)

                            # put text into a file into directory 'text'
                            outFileName = "C:/Users/erika/Downloads/text/" + filename + ".txt"
                            outFile = open(outFileName, "w")
                            outFile.write(txt)
                            outFile.close()

                            call_vard("C:/Users/erika/Downloads/vard/VARD2.5.4/clui.jar",
                                      "C:/Users/erika/Downloads/vard/VARD2.5.4/default",
                                      "50",
                                      "1",
                                      "C:/Users/erika/Downloads/text",
                                      "false",
                                      "C:/Users/erika/Downloads/testvard",
                                      "true")

                            # open varded file
                            with open("C:/Users/erika/Downloads/testvard/varded(50%) - Changes Unmarked" + "/" + filename + ".txt") as f:
                                vard_text = f.read()


                            set = [num, title_data, author_data, date_int, vard_text]
                            print(set)
                            with open('P5.csv', 'a', encoding="utf-8") as f:    # change each time
                                writer = csv.writer(f, lineterminator = '\n')
                                writer.writerow(set)
                            num += 1
                        except:
                            print(filename + ' exception')
                            exception_files.append(filename)
                            print(exception_files)

                            # put exception_list into a file into directory 'exception_listP4A0' (already made)
                            outFileName = "C:/Users/erika/Downloads/exceptionb18/" + 'exceptions2' + '.txt'
                            outFile = open(outFileName, "w")
                            outFile.write(' '.join([str(elem) for elem in exception_files]))
                            outFile.close()

    outFileName = "C:/Users/erika/Downloads/exceptionb18/" + 'catchfinal' + '.txt'
    outFile = open(outFileName, "w")
    outFile.write(' '.join([str(elem) for elem in exception_files]))
    outFile.close()



