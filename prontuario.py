# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:33:24 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd

def main():
    st.title("Archivos xlsx")

    st.header("Filtra la columna para realizar una búsqueda")
    st.subheader("Creado por: jahoperi")

    # Cargar el archivo Excel
    uploaded_file = st.file_uploader("Elige un archivo Excel", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Datos del archivo:")
        st.write(df)

        # Input de búsqueda
        search_column = st.selectbox("Selecciona la columna para buscar", df.columns)
        search_term = st.text_input("Introduce el término de búsqueda")

        if search_term:
            # Filtrar el DataFrame
            filtered_df = df[df[search_column].astype(str).str.contains(search_term, case=False, na=False)]
            st.write("Resultados de la búsqueda:")
            ##st.write(filtered_df)
            st.dataframe(filtered_df, width=1500, height=400)  # Ajusta el ancho y la altura según tus necesidades
            
            
            
            
            
if __name__ == "__main__":
    main()
