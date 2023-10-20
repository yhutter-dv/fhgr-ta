import pandas as pd

if __name__ == "__main__":
    labels = []
    sentences = []
    with open("./train.csv", "r", encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            result = line.split(";", 1)
            label =  result[0]
            text = result[1]
            labels.append(label)
            sentences.append(text)
    df = pd.DataFrame(list(zip(labels, sentences)), columns=["Label", "Text"])
    print(df)
