import numpy as np
import pickle
import streamlit as st

page_bg = """
<style>
[data-testid="stAppViewContainer"]{
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    background: radial-gradient(circle farthest-side, rgba(255,0,182,0.15), rgba(255,255,255,0));
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)


model = pickle.load(open('data_trained/model.pkl', 'rb'))
books_name = pickle.load(open('data_trained/movies_name.pkl', 'rb'))
final_rating = pickle.load(open('data_trained/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('data_trained/movies_pivot.pkl', 'rb'))

selected_books = st.selectbox(
    "Seleciona el libro que deseas:",
    books_name
)


# funcion para recomendar libros similares al libro seleccionado por el usuario
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    # poster_url = []

    # iteramos sobre las sugerencias(suggestion) de libros
    for book_id in suggestion:
        # obtenemos el nombre del libro basado en su book_id
        book_name.append(book_pivot.index[book_id])
    # buscamos indice correspondiente
    for name in book_name[0]:
        # aqui encontraremos el indice
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    # obtenemos la url para la imagen de dicho libro
    # for idx in ids_index:
    #     url = final_rating.iloc[idx]['img_url']
    #     poster_url.append(url)
    #
    # return poster_url


# recomendaremos libros similares con esta funcion al libro selecionado por el usuaripo
def recommend_books(book_name):
    book_list = []  # lista para almacenar nombres recomendados
    book_id = np.where(book_pivot.index == book_name)[0][0] # obtener el id de los recomendados
    # recomendacion de libros similares
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=15)

    # poster_url = fetch_poster(suggestion)
    # iteramos sobre la sugerencia de los libros
    for data in range(len(suggestion)):
        books = book_pivot.index[suggestion[data]]
        for book_recommended in books:
            book_list.append(book_recommended)
    # devolvemos tanto la lista como la url poster_url
    return book_list,


if st.button('Mostrar recomendaciones'):
    recommendation_books = recommend_books(selected_books)
    num_recommendations = len(recommendation_books)

    # Calcular el numero de filas y columnas necesarias
    num_rows = (num_recommendations + 4) // 5
    num_cols = min(5, num_recommendations)

    # Crear las filas y columnas
    for i in range(num_rows):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            index = i * 5 + j
            if index < num_recommendations:
                with cols[j]:
                    st.text(recommendation_books[index])
            else:
                break