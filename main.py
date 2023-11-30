import numpy as np
import umap
import pickle
# Parser to use method as an argument
import argparse
import hdbscan

from sklearn.datasets import fetch_20newsgroups
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score

from sentence_transformers import SentenceTransformer




def dim_red(mat, p, method):
    '''
    Perform dimensionality reduction

    Input:
    -----
        mat : NxM list 
        p : number of dimensions to keep 
    Output:
    ------
        red_mat : NxP list such that p<<m
    '''
    if method=='ACP':
        pca = PCA(n_components=p)
        red_mat = pca.fit_transform(mat)
        
    elif method=='TSNE':
        tsne = TSNE(n_components = p, random_state=42)
        red_mat = tsne.fit_transform(mat)
        
    elif method=='UMAP':
        umap_model = umap.UMAP(n_components=p, n_neighbors=35,
            min_dist=0.1,
            metric="cosine",
            random_state=42,)
        red_mat = umap_model.fit_transform(mat)
        
    else:
        raise Exception("Please select one of the three methods : APC, AFC, UMAP")
    
    return red_mat


def clust(mat, k, model):
    '''
    Perform clustering

    Input:
    -----
        mat : input list 
        k : number of cluster
    Output:
    ------
        pred : list of predicted labels
    '''
    if model=='KMeans':
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
        pred = kmeans.fit_predict(mat)
    elif model=='HDBSCAN':
        clusterer = hdbscan.HDBSCAN(min_samples=3, min_cluster_size = 15,
                               metric='euclidean', 
                               cluster_selection_method='eom')
        pred = clusterer.fit_predict(mat)
    else:
        raise Exception("Please select one of the two models: KMeans, HDBSCAN")
    
    return pred

def load_data():
    try:
        # Load the dataset from the local cache
        with open("./dataset/dataset.pkl", "rb") as file:
            return pickle.load(file)
    except Exception as err:
        print("error loading data from local file", err)
        # In case of error, download remote data
        return fetch_20newsgroups(subset="test")
    

# load data
ng20 = load_data()
corpus = ng20.data[:2000]
labels = ng20.target[:2000]
k = len(set(labels))

# embedding
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(corpus)

def main():
    METHODS = ["ACP", "TSNE", "UMAP"]
    MODELS = ["KMeans", "HDBSCAN"]
    parser = argparse.ArgumentParser(description="Examen parser")
    parser.add_argument(
        "--method", help="Specify the method.", choices=METHODS, required=True
    )
    parser.add_argument(
        "--model", help="Specify the model.", choices=MODELS, required=True
    )
    args = parser.parse_args()
    # Get the method and model from args
    method = args.method
    model = args.model

    # Computing
    red_emb = dim_red(embeddings, 20, method)

    # Perform clustering
    pred = clust(red_emb, k, model)

    # Evaluate clustering results
    nmi_score = normalized_mutual_info_score(pred, labels)
    ari_score = adjusted_rand_score(pred, labels)

    # Print results
    print(f"Method: {method}\nNMI: {nmi_score:.2f} \nARI: {ari_score:.2f}\n")

# Call the main
main()
