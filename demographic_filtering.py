# IMPORT MODULES
import pandas as pd
import numpy as np

# READ THE CSV
df = pd.read_csv("article.csv")

# SORT THE DATA AND SHOW THE FINAL RESULT

df_main = df.sort_values('total_events',ascending = True)
print(df_main.head(20))

