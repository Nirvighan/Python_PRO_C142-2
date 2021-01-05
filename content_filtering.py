# IMPORT MODULES
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# READ THE CSV
df = pd.read_csv("article.csv")


#CONVERT ARTICLE TITLE INTO LOWER STRING
title = [x.lower() for x in df["eventType"]]

# REMOVING THE EXTRA WORDS FROM  TITLE
count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(title)

# CLASSIFY THE ARTICLES
cosine_sim2 = cosine_similarity(count_matrix,count_matrix)

# CHANGE THE INDEX 
df = df.reset_index()
indices = pd.Series(df.index,index = df["eventType"])

# WRITE A FUNCTION FOR GETTING THE RECOMMENDATIONS
def get_recommendations(title,cosine_sim):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  
  sim_scores = sim_scores[1:11]
  article_indices = [i[0]for i in sim_scores]
  return df['eventType'].iloc[article_indices]

get_recommendations('CONTENT SHARED',cosine_sim2)
