from normalize_text import normalize_corpus

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
    content = normalize_corpus(content[:5], html_stripping = False, contraction_expansion = False)
    print(content[:5])
