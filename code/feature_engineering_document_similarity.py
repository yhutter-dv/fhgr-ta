from normalize_corpus import normalize_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
    content = normalize_corpus(content[:5], html_stripping = False, contraction_expansion = False)

    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2',
                     use_idf=True, smooth_idf=True)
    tv_matrix = tv.fit_transform(content)
    tv_matrix = tv_matrix.toarray()

    similarity_matrix_pdist = pdist(tv_matrix, "cosine")
    similarity_df_pdist = pd.DataFrame(squareform(similarity_matrix_pdist))

    print(content)
    print(similarity_df_pdist)
