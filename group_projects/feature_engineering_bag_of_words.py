from normalize_text import normalize_corpus
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
    content = normalize_corpus(content[:5], html_stripping = False, contraction_expansion = False)

    cv = CountVectorizer(min_df=0., max_df=1.)
    cv_matrix = cv.fit_transform(content)
    cv_matrix = cv_matrix.toarray()
    vocab = cv.get_feature_names_out()
    df = pd.DataFrame(cv_matrix, columns=vocab)
    print(df)
