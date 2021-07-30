# install the development version of superheat
# devtools::install_github("rlbarter/superheat")
library(superheat)
library(XML)
library(tidyverse)
library(textmineR)
# options(error=recover)
library(ggplot2)
library(pheatmap)

# Create TCM
Creat_TCM <- function(df){
  df$ID <- df$X
  df_tokens <- df$texts %>% tolower %>% word_tokenizer
  df_it <- itoken(df_tokens)
  df_v <- create_vocabulary(df_it) %>% prune_vocabulary(term_count_min = 5)
  df_vectorizer <- vocab_vectorizer(df_v)
  df_tcm <- create_tcm(df_it, df_vectorizer, skip_grams_window = 10)
  return(df_tcm)
}

# Fit Word_Embedding Model
Fit_Model <- function(TCM){
  glove <- GlobalVectors$new(rank = 50, x_max = 20)
  fit_main <- glove$fit_transform(TCM, n_iter = 5, convergence_tol = 0.00001)
  #### Default should be 1000 iteration, but lack the computing power on personal laptop
  #### Each iteration for 2500 text takes around 2 minutes 
  #### 1000 iterations would take 33 hours to run  
  fit_context <- glove$components
  word_vectors <- fit_main + t(fit_context)
  return(word_vectors)
}

# Compaison
compare_two_words <- function(word1,word2,word_vectors){
  matrix = word_vectors[word1, , drop = F]
  cos_sim = sim2(x = word_vectors, y = matrix, method = "cosine", norm = "l2")
  return(cos_sim[word2,])
}

fill_in_cos_value <- function(df,wordlist){
  for(i in 1:nrow(df)){
    for(j in 1:ncol(df)){
      if (i == j){
        df[i,j] <- 1}
      else{
        df[i,j] <- as.numeric(compare_two_words(wordlist[i],wordlist[j],word_vectors))}
    }
  }
  return(df)
}

# Build Heat Map
Build_Heat_TCM <- function(TCM,Worldlist){
  word_vectors <- Fit_Model(TCM)
  
  heat_df <- data.frame(matrix("", ncol = length(wordlist), nrow = length(wordlist)))
  rownames(heat_df) <- wordlist
  colnames(heat_df) <- wordlist
  total_heat <- fill_in_cos_value(heat_df,wordlist)
  
  total_heat[] <- lapply(total_heat, function(x) as.numeric(as.character(x)))
  heat_map <- pheatmap(total_heat, display_numbers = T)
  
  return(heat_map)
}

# Build Line Map
Fill_in_Line_DF <- function(word,df){
  for (i in 1:nrow(df)){
    for (j in 1:ncol(df)){
      TCM <- Creat_TCM(yearlist[i])
      word_vectors <- Fit_Model(TCM)
      df[i,j] <- compare_two_words(word,wordlist[j],word_vectors)
    } 
  }
  return(df)
}

Build_Line_TCM <- function(word,wordlist,yearlist){
  Line_df <- data.frame(matrix("", ncol = 2, nrow = 4))
  rownames(Line_df) <- yearlist
  colnames(Line_df) <- wordlist
  
  Line_df <- Fill_in_Line_DF(word,Line_df)
  
  colors <- c(wordlist[1] = "blue",wordlist[2]= "red")
  
  p <- ggplot(Line_df, aes(x = Year,group=1)) +
    geom_line(aes(y = Line_df[1], color = wordlist[1]), size = 1.5) +
    geom_line(aes(y = Line_df[2], color = wordlist[2]), size = 1.5) +
    labs(x = "Year",y = "Cos Similarity",color = "Legend") +
    theme(axis.title.x = element_text(size = 14, hjust = 0.5, vjust = -5))
  
  return(p)
}

## TOTAL
total_tcm <- Creat_TCM(Phase_1)
Total_heat <- Build_Heat_TCM(total_tcm,wordlist)
## T1
T1_tcm <- Creat_TCM(T1)
T1_heat <- Build_Heat_TCM(T1_tcm,wordlist)
## T2
T2_tcm <- Creat_TCM(T2)
T2_heat <- Build_Heat_TCM(T2_tcm,wordlist)
## T3
T3_tcm <- Creat_TCM(T3)
T3_heat <- Build_Heat_TCM(T3_tcm,wordlist)
## T4
T4_tcm <- Creat_TCM(T4)
T4_heat <- Build_Heat_TCM(T4_tcm,wordlist)

# Build Heat map
wordlist <-  c("phoenix","fire","pain","tax","work","king","glory",
               "martyrdom","christ","love","london")

Build_Heat_TCM(total_tcm,wordlist)

# Build Line Plot
wordlist <- c("christ","king")
yearlist <- c("T1", "T2","T3","T4")
word <- "phoenix"

Build_Line_TCM(word,wordlist,yearlist)
