from normalize_text import normalize_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
    content = normalize_corpus(content[:1000], html_stripping = False, contraction_expansion = False)

    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2',
                     use_idf=True, smooth_idf=True)
    tv_matrix = tv.fit_transform(content)
    tv_matrix = tv_matrix.toarray()
    vocab = tv.get_feature_names_out()
    df = pd.DataFrame(np.round(tv_matrix, 2), columns=vocab)
    print(content)
    print(df)
