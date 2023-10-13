from normalize_text import normalize_corpus

if __name__ == "__main__":
    with open("./newscrawl_2012_10K.txt", "r") as f:
        content = f.readlines()
        content = [[sentence] for sentence in content]
    content = normalize_corpus(content[:10])
    print(content[:10])