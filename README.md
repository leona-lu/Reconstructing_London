# Project Overview
Who should get to decide what a utopian society looks like? After London was razed to the ground in the Great Fire of 1666, its reconstruction into the “emerald gem of Europe” was heavily influenced by the monarchy and aristocratic elites. In building a utopian epicenter focused on political and economic interests, immense sacrifices had to be made by London’s most marginalized citizens. 

Project team led by (PHD Candidate [Nicholas Smolenski](https://scholars.duke.edu/person/nicholas.smolenski) and [Professor Astrid Giugni](https://bigdata.duke.edu/people/astrid-adele-giugni)) will investigate those questions using machine learning algorithm.Undergradute researcher include: [Yuchen Lu](https://www.linkedin.com/in/yuchen-lu-2023/), [Erika Wang](https://www.linkedin.com/in/erika-wang-90911a175/), [Audrey Liu](https://www.linkedin.com/in/audrey-liu-2b244a1a3/).

# Database
We used text from [EEBO-TCP Database](https://quod.lib.umich.edu/e/eebogroup/).
We filtered out 1600-1700 text using [teir2r package](https://rdrr.io/github/michaelgavin/tei2r/).To address spelling 
variation in Early English Printed Book, the project utilized [VARD 2.0](http://ucrel.lancs.ac.uk/vard/about/). We applied 50% threshold for 
all text. 

# Poster and Presentation
Check out our project [poster](https://docs.google.com/presentation/d/1RCK63lLp28E32rZVp1LH8O7z6PfwLqFesWOEgg2Gx64/edit?usp=sharing).

# Repository Organization
* 1_[Macro-Analysis](https://github.com/leona-lu/Reconstructing_London/tree/main/Macro-Analysis) - Topic Modeling and Word Embedding on all 17th century text
* 2_[Micro-Analysis]() - Sentiment and Lexical Richness Analysis on St. Paul's Cathedral
* 3_[Graph](https://github.com/leona-lu/Reconstructing_London/tree/main/Graph) - all graphs created along the process 
* 3_[Test](https://github.com/leona-lu/Reconstructing_London/tree/main/Test) - Test code on sample texts  
## Project Refrences 
### Topic Modeling 
[1] Jockers, Matthew. Text Analysis with R for Students of Literature. Springer. 2014.
### Word Embedding 
[2] Socher, Richard. "CS 224D: Deep Learning for NLP", Lecture Notes (https://cs224d.stanford.edu/lecture_notes/notes2.pdf)
