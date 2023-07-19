# import the processes data and build a chatbot to ask question
import numpy as np
import pandas as pd

from script.utils.utils import answer_question

# read in data
data_path = "/home/data"
cleaned_path = data_path + "/cleaned/"
processed_path = data_path + "/processed/"

df = pd.read_csv(processed_path + "dbt_manifest_embeddings.csv", index_col=0)

# turn to array
df["embeddings"] = df["embeddings"].apply(eval).apply(np.array)

# use ai to anwser question
answer_question(df=df, question="What does active_pages mean ?", debug=False)


answer_question(df=df, question="List out the columns in active_pages?", debug=False)
