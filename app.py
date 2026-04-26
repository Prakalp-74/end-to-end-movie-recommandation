import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🎬 Movie Recommendation System")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    if movie == "":
        st.warning("Please enter a movie")
    else:
        response = requests.get(
            f"{API_URL}/recommend",
            params={"movie": movie}
        )

        if response.status_code == 200:
            data = response.json()

            st.subheader("Recommended Movies:")
            for m in data["recommendations"]:
                st.write(m)
        else:
            st.error("Movie not found")