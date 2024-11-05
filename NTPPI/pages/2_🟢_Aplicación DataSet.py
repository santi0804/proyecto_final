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
                
    # Plantilla Básica Proyecto Integrador
    -------------------------------------------

    ## Introducción
    
    #### ¿Qué es el proyecto?
    
     Chronos Manager es una aplicación para gestionar horarios de trabajo, controlar horas extras, ausencias y generar reportes de asistencia. Permite registrar entradas y salidas de empleados, calcular horas trabajadas y gestionar permisos.
    
    
    #### ¿Cuál es el objetivo principal?
    
     El objetivo principal de Chronos Manager es facilitar el control y la gestión de horarios de trabajo, optimizando el seguimiento de asistencia, horas extras y ausencias en equipos laborales.


    #### ¿Por qué es importante?
    
    Chronos Manager es importante porque ayuda a las empresas a gestionar de manera eficiente los horarios de trabajo, mejorando la precisión en el registro de asistencia, horas extras y ausencias. Esto optimiza la administración del tiempo, reduce errores, y facilita la generación de reportes, lo que mejora la productividad y la toma de decisiones.
    
    
     ## Desarrollo
     
    
    Este proyecto titulado Gestor de Horarios, Control de Accesos y Analizador de Datos, 
    tiene como objetivo proporcionar una solución integral para la gestión de asistencia y horarios de empleados, 
    así como el control de accesos en una organización. La plataforma permite crear, modificar y gestionar los horarios del personal, registrar la entrada y salida a través de un 
    sistema de control de accesos y, además, generar reportes analíticos basados en estos datos. Estas funcionalidades permiten optimizar la gestión de los recursos humanos, mejorar la eficiencia en la administración del tiempo y 
    proporcionar información valiosa para la toma de decisiones estratégicas a través del análisis de los datos obtenidos.
    
    
    ##  Procedimiento utilizado
     
    El procedimiento utilizado para el desarrollo del proyecto Gestor de Horarios, Control de Accesos y Analizador de Datos fue el siguiente:

    Análisis de Requisitos: Se realizó un análisis detallado para identificar las necesidades del sistema, como la gestión de horarios, control de acceso, y 
    el análisis de datos de asistencia. Se 
    establecieron los módulos clave del sistema y las interacciones entre ellos.

    Diseño de la Arquitectura: Se definió una arquitectura basada en un frontend intuitivo y funcional, conectado a un backend robusto que administra los datos de usuarios y asistencias. El frontend fue desarrollado con tecnologías como React para la interfaz de usuario, mientras 
    que el backend utilizó Node.js con una base de datos MySQL para almacenar y gestionar la información.

    Desarrollo del Sistema: Se implementaron las funcionalidades clave:

    Gestor de Horarios: Permite crear y asignar horarios personalizados para cada empleado. Control de Accesos: Monitorea la entrada y salida de los empleados, registrando sus tiempos de trabajo.
    Analizador de Datos: Genera reportes y visualizaciones analíticas a partir de los datos recopilados, permitiendo una mejor comprensión del desempeño y asistencia.
    Pruebas y Depuración: Se realizaron pruebas exhaustivas para asegurar el correcto funcionamiento de todas las características, corrigiendo errores y ajustando el rendimiento del sistema.

    Documentación y Despliegue: Se preparó la documentación técnica y el sistema fue desplegado, asegurando que los usuarios puedan interactuar fácilmente con el mismo.
     
     
    ##  Resultados obtenidos
     
    Los resultados obtenidos con el desarrollo del proyecto Gestor de Horarios, Control de Accesos y Analizador de Datos fueron muy positivos, logrando cumplir con los objetivos planteados. Entre los resultados destacan:

    Automatización de la Gestión de Horarios: Se implementó un sistema eficiente para crear y gestionar horarios personalizados para los empleados, reduciendo significativamente el tiempo y esfuerzo manual necesario para esta tarea.

    Control de Accesos en Tiempo Real: El sistema permite registrar la entrada y salida de los empleados de manera automática, proporcionando un control más preciso y fiable de la asistencia, mejorando la seguridad y la puntualidad.

    Generación de Reportes Analíticos: El módulo de análisis de datos permitió generar reportes detallados sobre la asistencia de los empleados, identificando patrones, días de ausencias y horas extras. Estos reportes ayudan a los administradores a tomar decisiones informadas y estratégicas sobre la gestión del personal.

    Interfaz de Usuario Intuitiva: Gracias al uso de tecnologías modernas como React para el frontend, el sistema ofrece una experiencia de usuario amigable e interactiva, facilitando la navegación y la gestión diaria.

    Mejora en la Eficiencia Operativa: El proyecto ayudó a optimizar los procesos de recursos humanos, minimizando errores en el registro de asistencia y proporcionando una visión clara del rendimiento de los empleados, lo que impacta positivamente en la productividad organizacional.
     
     
    ## Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    
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
