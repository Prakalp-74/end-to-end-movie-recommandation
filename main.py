from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
import os

app = FastAPI()


BASE_DIR = os.path.dirname(__file__)

movies = pickle.load(open(os.path.join(BASE_DIR, "movie.pkl"), "rb"))
indices = pickle.load(open(os.path.join(BASE_DIR, "indices.pkl"), "rb"))
tfidf_matrix = pickle.load(open(os.path.join(BASE_DIR, "tfidf_matrix.pkl"), "rb"))


def normalize(title):
    return title.strip().lower()


if not isinstance(indices, dict):
    indices = {k: int(v) for k, v in indices.items()}


indices = {normalize(k): v for k, v in indices.items()}



def recommend(movie, top_n=5):
    movie = normalize(movie)

    if movie not in indices:
        raise HTTPException(status_code=404, detail="Movie not found")

    idx = indices[movie]


    query_vec = tfidf_matrix[idx]
    scores = (tfidf_matrix @ query_vec.T).toarray().ravel()

 
    sorted_indices = np.argsort(-scores)

    recommendations = []
    for i in sorted_indices:
        if i == idx:
            continue
        title = movies.iloc[i]["title"]
        recommendations.append(title)
        if len(recommendations) >= top_n:
            break

    return recommendations


@app.get("/")
def home():
    return {"message": "Movie API running"}


@app.get("/recommend")
def get_recommend(movie: str):
    recs = recommend(movie)
    return {"recommendations": recs}
