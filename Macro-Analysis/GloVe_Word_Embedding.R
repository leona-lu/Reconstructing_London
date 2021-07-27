# Load Library
library(XML)
library(tidyverse)
library(textmineR)
library(text2vec)

# T1
## Create TCM
T1$ID <- T1$X
tokens <- T1$texts %>% tolower %>% word_tokenizer
length(tokens)
it <- itoken(tokens)
v <- create_vocabulary(it) %>% prune_vocabulary(term_count_min = 5)
vectorizer <- vocab_vectorizer(v)
t1_tcm <- create_tcm(it, vectorizer, skip_grams_window = 10)

## Fit Word_Embedding Model
glove <- GlobalVectors$new(rank = 50, x_max = 20)
fit_main <- glove$fit_transform(t1_tcm, n_iter = 5, convergence_tol = 0.00001)
#### Default should be 1000 iteration, but lack the computing power on personal laptop
#### Each iteration for 2500 text takes around 2 minutes 
#### 1000 iterations would take 33 hours to run  
fit_context <- glove$components
word_vectors <- fit_main + t(fit_context)

### Calculate Cosine Similarities
T1_phoenix = word_vectors["phoenix", , drop = F]
cos_sim_T1_phoenix = sim2(x = word_vectors, y = T1_phoenix, method = "cosine", norm = "l2")
cos_sim_T1_phoenix["christ",]
cos_sim_T1_phoenix["king",]

head(sort(cos_sim_T1_phoenix[,1], decreasing = T), 10)

# T2
## Create TCM
T2$ID <- T2$X
tokens <- T2$texts %>% tolower %>% word_tokenizer
length(tokens)
it <- itoken(tokens)
v <- create_vocabulary(it) %>% prune_vocabulary(term_count_min = 5)
vectorizer <- vocab_vectorizer(v)
t2_tcm <- create_tcm(it, vectorizer, skip_grams_window = 10)

## Fit Word_Embedding Model
glove <- GlobalVectors$new(rank = 50, x_max = 20)
fit_main <- glove$fit_transform(t2_tcm, n_iter = 5, convergence_tol = 0.00001)
#### Default should be 1000 iteration, but lack the computing power on personal laptop
#### Each iteration for 2500 text takes around 2 minutes 
#### 1000 iterations would take 33 hours to run  
fit_context <- glove$components
word_vectors <- fit_main + t(fit_context)

### Calculate Cosine Similarities
T2_phoenix = word_vectors["phoenix", , drop = F]
cos_sim_T2_phoenix = sim2(x = word_vectors, y = T2_phoenix, method = "cosine", norm = "l2")
cos_sim_T2_phoenix["christ",]
cos_sim_T2_phoenix["king",]
head(sort(cos_sim_T2_phoenix[,1], decreasing = T), 10)

# T3
## Create TCM
T3$ID <- T3$X
tokens <- T3$texts %>% tolower %>% word_tokenizer
length(tokens)
it <- itoken(tokens)
v <- create_vocabulary(it) %>% prune_vocabulary(term_count_min = 5)
vectorizer <- vocab_vectorizer(v)
t3_tcm <- create_tcm(it, vectorizer, skip_grams_window = 10)

## Fit Word_Embedding Model
glove <- GlobalVectors$new(rank = 50, x_max = 20)
fit_main <- glove$fit_transform(t3_tcm, n_iter = 5, convergence_tol = 0.00001)
#### Default should be 1000 iteration, but lack the computing power on personal laptop
#### Each iteration for 2500 text takes around 2 minutes 
#### 1000 iterations would take 33 hours to run  
fit_context <- glove$components
word_vectors <- fit_main + t(fit_context)

### Calculate Cosine Similarities
T3_phoenix = word_vectors["phoenix", , drop = F]
cos_sim_T3_phoenix = sim2(x = word_vectors, y = T3_phoenix, method = "cosine", norm = "l2")
cos_sim_T3_phoenix["christ",]
cos_sim_T3_phoenix["king",]

head(sort(cos_sim_T3_phoenix[,1], decreasing = T), 10)

# T4
## Create TCM
T4$ID <- T4$X
tokens <- T4$texts %>% tolower %>% word_tokenizer
length(tokens)
it <- itoken(tokens)
v <- create_vocabulary(it) %>% prune_vocabulary(term_count_min = 5)
vectorizer <- vocab_vectorizer(v)
t4_tcm <- create_tcm(it, vectorizer, skip_grams_window = 10)

## Fit Word_Embedding Model
glove <- GlobalVectors$new(rank = 50, x_max = 20)
fit_main <- glove$fit_transform(t4_tcm, n_iter = 5, convergence_tol = 0.00001)
#### Default should be 1000 iteration, but lack the computing power on personal laptop
#### Each iteration for 2500 text takes around 2 minutes 
#### 1000 iterations would take 33 hours to run  
fit_context <- glove$components
word_vectors <- fit_main + t(fit_context)

### Calculate Cosine Similarities
T4_phoenix = word_vectors["phoenix", , drop = F]
cos_sim_T4_phoenix = sim2(x = word_vectors, y = T4_phoenix, method = "cosine", norm = "l2")
cos_sim_T4_phoenix["christ",]
cos_sim_T4_phoenix["king",]

head(sort(cos_sim_T4_phoenix[,1], decreasing = T), 10)

### Plot
tsne <- Rtsne(word_vectors[2:500,], perplexity = 50, pca = FALSE)
tsne_plot <- tsne$Y %>%
  as.data.frame() %>%
  mutate(word = row.names(word_vectors)[2:500]) %>%
  ggplot(aes(x = V1, y = V2, label = word)) + 
  geom_text(size = 3)
tsne_plot

# Load Document 
P1 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p1.csv")
P2 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p2.csv")
P3 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p3.csv")
P4 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p4.csv")
P5 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p5.csv")
P6 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p6.csv")
P7 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p7.csv")
P8 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p8.csv")
P9 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p9.csv")
P10 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p10.csv")
P11 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_p11.csv")
P12 <- read.csv("C:/Users/yl583/Desktop/Reconstructing_Utopia/Phase 1/Cleaned_Data_test.csv")

Phase_1 <- rbind(P1,P2)
Phase_1 <- rbind(Phase_1,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12)

# Separate by Time Period 
T1 <- Phase_1 %>% filter(Date < 1666 & Date >= 1660)
T2 <- Phase_1 %>% filter(Date < 1678 & Date >= 1666)
T3 <- Phase_1 %>% filter(Date < 1686 & Date >= 1678)
T4 <- Phase_1 %>% filter(Date >= 1686)
