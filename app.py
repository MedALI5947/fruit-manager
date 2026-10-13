import streamlit as st
from fruit_manange import*

st.title("Dashbord de la Plantation")
inventaire = ouvrir_inventaire()
prix = ouvrir_prix
tresorerie = ouvrir_tresoreries()
st.header(" tresoreri")
st.metric(label ="Montant disponible", value=f"{tresorerie:.2f}$")
st.header("Inventaire")
st.table(inventaire)
