library(tm)
library("wordcloud")
# Total
## Create TCM & DTM
T1$ID <- T1$X
tokens <- T1$texts %>% tolower %>% word_tokenizer
length(tokens)
it <- itoken(tokens)
v <- create_vocabulary(it) %>% prune_vocabulary(term_count_min = 5)
vectorizer <- vocab_vectorizer(v)
total_dtm <- create_dtm(it, vectorizer)
dtm = as.DocumentTermMatrix(total_dtm, weighting = weightTf)
a0 = (apply(dtm, 1, sum) > 0)   # build vector to identify non-empty docs
dtm = dtm[a0,]                  # drop empty docs


## Build Wordcloud
tst = round(ncol(dtm)/100)  # divide DTM's cols into 100 manageble parts
a = rep(tst,99)
b = cumsum(a);rm(a)
b = c(0,b,ncol(dtm))

ss.col = c(NULL)
for (i in 1:(length(b)-1)) {
  tempdtm = dtm[,(b[i]+1):(b[i+1])]
  s = colSums(as.matrix(tempdtm))
  ss.col = c(ss.col,s)
}

tsum = ss.col
tsum = tsum[order(tsum, decreasing = T)]    

wordcloud(names(tsum), tsum,    
          scale = c(4, 0.5),    
          max.words = 100,       
          colors = brewer.pal(8, "Dark2"))   
title(sub = "Term Frequency - 1660 - 1666")    

# plot barchart for top tokens
test = as.data.frame(round(tsum[1:15],0))
test <- tibble::rownames_to_column(test, "NAME")

ggplot(test, aes(x = NAME, y = `round(tsum[1:15], 0)`)) + 
  geom_bar(stat = "identity", fill = "Blue") +
  labs(x = "top token",y="frequency",
       title = "Top Token - 1660 - 1666"
  )

## Fit Topic Model
embeddings <- FitLdaModel(dtm = tcm,
                          k = 50,
                          iterations = 200,
                          burnin = 180,
                          alpha = 0.1,
                          beta = 0.05,
                          optimize_alpha = TRUE,
                          calc_likelihood = FALSE,
                          calc_coherence = TRUE,
                          calc_r2 = TRUE,
                          cpus = 2)

embeddings$top_terms <- GetTopTerms(phi = embeddings$phi, M = 5)

embeddings$summary <- data.frame(topic = rownames(embeddings$phi),
                                 coherence = round(embeddings$coherence, 3),
                                 prevalence = round(colSums(embeddings$theta), 2),
                                 top_terms = apply(embeddings$top_terms, 2, function(x){
                                   paste(x, collapse = ", ")
                                 }),
                                 stringsAsFactors = FALSE)
### According to Prevalence 
embeddings$summary[ order(embeddings$summary$prevalence, decreasing = TRUE) , ][ 1:10 , ]
### According to Coherence 
embeddings$summary[ order(embeddings$summary$coherence, decreasing = TRUE) , ][ 1:10 , ]
