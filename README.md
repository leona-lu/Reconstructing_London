This is the GitHub repository for 2021 Duke university Data+ Project 17 [Constructing Utopia in Restoration London](https://bigdata.duke.edu/projects/constructing-utopias-restoration-london).

# Project Overview
Who should get to decide what a utopian society looks like? After London was razed to the ground in the Great Fire of 1666, its reconstruction into the “emerald gem of Europe” was heavily influenced by the monarchy and aristocratic elites. In building a utopian epicenter focused on political and economic interests, immense sacrifices had to be made by London’s most marginalized citizens. 

Project team led by ([Professor Astrid Giugni](https://bigdata.duke.edu/people/astrid-adele-giugni) and PHD Candidate [Nicholas Smolenski](https://scholars.duke.edu/person/nicholas.smolenski)) will 
investigate those questions using machine learning algorithm.Undergradute researcher include: [Yuchen Lu](https://www.linkedin.com/in/yuchen-lu-2023/), [Erika Wang](https://www.linkedin.com/in/erika-wang-90911a175/), [Audrey Liu](https://www.linkedin.com/in/audrey-liu-2b244a1a3/).

# Database
We used text from [EEBO-TCP Database](https://quod.lib.umich.edu/e/eebogroup/).
We filtered out 1600-1700 text using [teir2r package](https://rdrr.io/github/michaelgavin/tei2r/).To address spelling 
variation in Early English Printed Book, the project utilized [VARD 2.0](http://ucrel.lancs.ac.uk/vard/about/). We applied 50% threshold for 
all text. 

# Poster and Presentation
Check out our project [poster](https://docs.google.com/presentation/d/1RCK63lLp28E32rZVp1LH8O7z6PfwLqFesWOEgg2Gx64/edit?usp=sharing) and [website](https://sites.duke.edu/reconstructingutopia/). 

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

Kulshrestha, Ria. “NLP 101: Word2Vec — Skip-gram and CBOW”. Towards Data Science. 2019.

[3] Garg, N., Schiebinger, L., Jurafsky, D., & Zou, J. (2018). Word embeddings quantify 100 years of gender and ethnic stereotypes. Proceedings of the National Academy of Sciences, 115(16), E3635–E3644. https://doi.org/10.1073/pnas.1720347115

[4] Charu C. Aggarwal. 2018. Neural Networks and Deep Learning: A Textbook (1st. ed.). Springer Publishing Company, Incorporated.

[5] Prabhakaran, Selva. “Cosine Similarity – Understanding the math and how it works (with python codes)”. Machine Learning +. 2018.

### Sentiment Analysis
[6] Jockers, Matthew. Text Analysis with R for Students of Literature. Springer. 2014.

[7] Silge, Julia and David Robinson. “Sentiment analysis with tidy data”. Text Mining with Tidy Approach. 




