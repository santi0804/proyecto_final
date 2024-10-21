import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

# Cargar archivo CSV subido por el usuario
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

# Si el usuario ha subido un archivo, usa ese. Si no, usa el archivo por defecto.
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv('./static/datasets/ventas.csv')

# Tabs para diferentes análisis
tab_descripcion, tab_analisis_exploratorio, tab_filtrado_basico, tab_filtro_final_dinamico = st.tabs(
    ["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"]
)

#----------------------------------------------------------
# Generador de datos
#----------------------------------------------------------
with tab_descripcion:      
    st.markdown('''
    ## Plantilla Básica para Proyecto Integrador

    ### Introducción
    - **¿Qué es el proyecto?** Chronos Manager es una aplicación para gestionar horarios de trabajo...
    
    COMPAS ARGUMENTAR MAS DESCRICIONES AQUI EN ESTE ESPACIO, TENER PRESENTE LAS ARGUMENTACIONES QUE DIO EL PROFE EN LA DOCUMENTACIÒN 
    ...
    ''')

#----------------------------------------------------------
# Análisis Exploratorio
#----------------------------------------------------------
with tab_analisis_exploratorio:    
    st.title("Análisis Exploratorio")
    st.markdown("""
    * Muestra las primeras 5 filas del DataFrame. **(df.head())**
    * Muestra la cantidad de filas y columnas del DataFrame. **(df.shape)**
    * Muestra los tipos de datos de cada columna. **(df.dtypes)**
    * Identifica y muestra las columnas con valores nulos. **(df.isnull().sum())**
    * Muestra un resumen estadístico de las columnas numéricas. **(df.describe())**
    """)
    st.dataframe(df.head())

#----------------------------------------------------------
# Filtrado Básico
#----------------------------------------------------------
with tab_filtrado_basico:
    st.title("Filtro Básico")
    column = st.selectbox("Selecciona la columna para filtrar", df.columns)
    value = st.text_input(f"Introduce el valor para filtrar en {column}")
    if value:
        filtered_data = df[df[column] == value]
        st.dataframe(filtered_data)

#----------------------------------------------------------
# Filtro Final Dinámico
#----------------------------------------------------------
with tab_filtro_final_dinamico:
    st.title("Filtro Final Dinámico")
    st.markdown("""
    * Muestra un resumen dinámico del DataFrame filtrado.
    """)
    st.dataframe(df)
