from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def answer_question(question, text):
    sentences = text.split(".")
    corpus = sentences + [question]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)

    question_vec = tfidf[-1]
    text_vecs = tfidf[:-1]

    sims = cosine_similarity(question_vec, text_vecs)[0]
    best_idx = np.argmax(sims)

    return sentences[best_idx].strip()
