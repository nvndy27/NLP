from src.representations.simple_tokenizer import SimpleTokenizer
from src.representations.count_vectorizer import CountVectorizer

def main():
    
    tokenizer = SimpleTokenizer()

    vectorizer = CountVectorizer(tokenizer)

    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]

    vectors = vectorizer.fit_transform(corpus)

    print("Vocabulary:", vectorizer.vocabulary_)
    print("Document-term matrix:")
    for vec in vectors:
        print(vec)

if __name__ == "__main__":
    main()