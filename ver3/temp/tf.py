from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")
labels = data['id']
encode = data['encode']

classifier = LogisticRegression()
model = classifier.fit(np.array(encode), np.array(labels))
print(model.score(np.array(encode), np.array(labels)))