from normalize_text import normalize_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

def print_most_similiar_documents(df, number_of_documents = 1):
    df_sorted = df.sort_values(by="Distance", ascending=True)
    for i in range(number_of_documents):
        first_document_index = int(df_sorted["Document\Cluster 1"].values[0])
        second_document_index = int(df_sorted["Document\Cluster 2"].values[0])
        first_document = content[first_document_index]
        second_document = content[second_document_index]
        print(f"Iteration {i}")
        print(f"Document #{first_document_index}")
        print(first_document)
        print(f"Document #{second_document_index}")
        print(second_document)

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
    content = normalize_corpus(content[:1000], html_stripping = False, contraction_expansion = False)

    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2',
                     use_idf=True, smooth_idf=True)
    tv_matrix = tv.fit_transform(content)
    tv_matrix = tv_matrix.toarray()

    similarity_matrix_pdist = pdist(tv_matrix, "cosine")
    linkage_complete = linkage(similarity_matrix_pdist, 'complete')
    linkage_average = linkage(similarity_matrix_pdist, 'average')
    linkage_weighted = linkage(similarity_matrix_pdist, 'weighted')

    df_linkage_complete = pd.DataFrame(linkage_complete, columns=['Document\Cluster 1', 'Document\Cluster 2',
                         'Distance', 'Cluster Size'], dtype='object')
    df_linkage_average = pd.DataFrame(linkage_average, columns=['Document\Cluster 1', 'Document\Cluster 2',
                         'Distance', 'Cluster Size'], dtype='object')
    df_linkage_weighted = pd.DataFrame(linkage_weighted, columns=['Document\Cluster 1', 'Document\Cluster 2',
                         'Distance', 'Cluster Size'], dtype='object')

    segments = 20
    print(content)

    print("=" * segments)
    print(f"Complete Linkage Result")
    print("=" * segments)
    print(df_linkage_complete)
    print_most_similiar_documents(df_linkage_complete, 5)

    print("=" * segments)
    print(f"Average Linkage Result")
    print("=" * segments)
    print(df_linkage_average)
    print_most_similiar_documents(df_linkage_average, 5)

    print("=" * segments)
    print(f"Weighted Linkage Result")
    print("=" * segments)
    print(df_linkage_weighted)
    print_most_similiar_documents(df_linkage_weighted, 5)
