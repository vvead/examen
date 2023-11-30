from sklearn.datasets import fetch_20newsgroups
import pickle

ng20 = fetch_20newsgroups(subset="test")

# Write pickled data to a file
with open("./dataset.pkl", "wb") as file:
    pickle.dump(ng20, file)