from normalize_text import normalize_corpus

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
    content = normalize_corpus(content[:1000], html_stripping = False, contraction_expansion = False)
    print(content)
