import random
from faker import Faker
import streamlit as st 
import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt
import firebase_admin  
from firebase_admin import credentials, firestore  

st.set_page_config(layout="wide")

st.subheader("Proyecto Integrador")


if not firebase_admin._apps:    # Verificar si ya existe una instancia de la aplicación
    firebase_credentials = st.secrets["FIREBASE_CREDENTIALS"]  # Cargar las credenciales de Firebase desde los secretos de Streamlit
    secrets_dict = firebase_credentials.to_dict()  # Convertir las credenciales a un diccionario Python
    cred = credentials.Certificate(secrets_dict)   # Crear un objeto de credenciales usando el diccionario 
    app = firebase_admin.initialize_app(cred)     # Inicializar la aplicación de Firebase con las credenciales
db = firestore.client()   # Obtener el cliente de Firestore


tad_descripcion, tab_Generador, tab_datos, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Generador de datos", "Datos", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''   

    ## Introducción

    -   Que somos:
        Chronos Manager es una solución integral diseñada para optimizar la gestión de horarios, el control de accesos, y el registro de horas extras y ausencias en entornos laborales y educativos. Utiliza tecnología avanzada para facilitar la planificación de horarios, garantizar la seguridad mediante control de accesos, y proporcionar un seguimiento efectivo de la asistencia y el tiempo trabajado. Esta plataforma centralizada permite a los administradores gestionar fácilmente la ocupación de espacios y supervisar el rendimiento de los empleados o estudiantes.
    
    -   Obejtivo:  Nuestro objetivo principal de Chronos Manager es proporcionar una herramienta eficiente y fácil de usar que permita a las organizaciones gestionar sus horarios y accesos de manera efectiva. Esto incluye la planificación de turnos, el registro de horas trabajadas, la gestión de ausencias y horas extras, y la implementación de controles de acceso seguros. Al hacerlo, se busca mejorar la productividad, optimizar los recursos, y asegurar un entorno de trabajo o aprendizaje organizado y seguro.
    
    -   Por qué es importante: La importancia de Chronos Manager radica en la creciente necesidad de las organizaciones de adaptarse a un entorno laboral y educativo dinámico y en constante cambio. Con la evolución de las prácticas laborales y las exigencias de seguridad, es fundamental contar con herramientas que faciliten la gestión eficiente del tiempo y los accesos. Este proyecto no solo ayuda a minimizar el riesgo de acceso no autorizado, sino que también proporciona a los líderes información valiosa sobre la asistencia y el rendimiento, lo que a su vez permite la toma de decisiones informadas y la implementación de mejoras continuas en la gestión de recursos humanos.

    ## Desarrollo

    -   Explicación detallada del proyecto : Somos un software diseñado para gestionar controles de acceso, horas extras y ausencias en áreas administrativas de cualquier tipo de empresa. Facilita el monitoreo de asistencia, la validación de ausentismos y el seguimiento del tiempo extra trabajado, optimizando la eficiencia operativa.
    
    -   Procedimiento utilizado :  Para implementar Chronos Manager, se integran dispositivos de control de acceso con una plataforma central que registra horarios, ausencias y horas extras. Los datos se procesan y visualizan en un panel intuitivo para los administradores.
        Tambien se pueden adaptar a sistemas operativos actualizados.
    
    -   Resultados obtenidos:  Los resultados incluyen una mejora significativa en la organización de los horarios, un aumento en la seguridad del acceso, y una reducción del tiempo dedicado a gestionar ausencias y horas extras, lo cual contribuye a una mayor productividad empresarial.

    ## Conclusión

    -   Resumen de los resultados:  Chronos Manager ha mejorado la gestión de horarios, el control de accesos y la validación de ausencias en áreas administrativas, optimizando el flujo de trabajo y garantizando la seguridad.
    
    -   Logros alcanzados: Se logró una administración centralizada y automatizada de los horarios, con un control preciso de accesos, horas extras y ausencias, reduciendo los errores y aumentando la productividad.
    
    -   Dificultades encontradas: Se presentaron desafíos en la integración con sistemas de control de acceso preexistentes y en la adaptación a las necesidades específicas de cada empresa.

    -   Aportes personales: Nuestras contribuciónes se centran en el desarrollo de funcionalidades de validación de ausencias y en la personalización de la interfaz de usuario, buscando mejorar la experiencia del administrador en el manejo de datos y control de accesos.
    ''')

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------

with tab_Generador:
    st.write('Esta función Python genera datos ficticios de usuarios y productos y los carga en una base de datos Firestore, proporcionando una interfaz sencilla para controlar la cantidad de datos generados y visualizar los resultados.')
    # Inicializar Faker para Colombia
    fake = Faker('es_CO')

    
    ciudades_colombianas = [        # Lista de ciudades colombianas
        'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 
        'Cúcuta', 'Bucaramanga', 'Pereira', 'Santa Marta', 'Ibagué',
        'Pasto', 'Manizales', 'Neiva', 'Villavicencio', 'Armenia'
    ]

    def generate_fake_users(n):
        users = []
        for _ in range(n):
            user = {
                'nombre': fake.name(),
                'email': fake.email(),
                'edad': random.randint(18, 80),
                'ciudad': random.choice(ciudades_colombianas)
            }
            users.append(user)
        return users

    def generate_fake_products(n):
        categories = {
            'Electrónica': [
                'Celular', 'Portátil', 'Tablet', 'Audífonos', 'Reloj inteligente', 
                'Cámara digital', 'Parlante Bluetooth', 'Batería portátil', 
                'Monitor', 'Teclado inalámbrico'
            ],
            'Ropa': [
                'Camiseta', 'Jean', 'Vestido', 'Chaqueta', 'Zapatos', 
                'Sudadera', 'Medias', 'Ruana', 'Gorra', 'Falda'
            ],
            'Hogar': [
                'Lámpara', 'Cojín', 'Cortinas', 'Olla', 'Juego de sábanas', 
                'Toallas', 'Espejo', 'Reloj de pared', 'Tapete', 'Florero'
            ],
            'Deportes': [
                'Balón de fútbol', 'Raqueta de tenis', 'Pesas', 
                'Colchoneta de yoga', 'Bicicleta', 'Tenis para correr', 
                'Maletín deportivo', 'Termo', 'Guantes de boxeo', 'Lazo para saltar'
            ]
        }

        products = []
        for _ in range(n):
            category = random.choice(list(categories.keys()))
            product_type = random.choice(categories[category])
            
            product = {
                'nombre': product_type,
                'precio': round(random.uniform(10000, 1000000), -3),  # Precios en pesos colombianos
                'categoria': category,
                'stock': random.randint(0, 100)
            }
            products.append(product)
        return products

    def delete_collection(collection_name):
        docs = db.collection(collection_name).get()
        for doc in docs:
            doc.reference.delete()

    def add_data_to_firestore(collection, data):
        for item in data:
            db.collection(collection).add(item)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Usuarios')
        num_users = st.number_input('Número de usuarios a generar', min_value=1, max_value=100, value=10)
        if st.button('Generar y Añadir Usuarios'):
            with st.spinner('Eliminando usuarios existentes...'):
                delete_collection('usuarios')
            with st.spinner('Generando y añadiendo nuevos usuarios...'):
                users = generate_fake_users(num_users)
                add_data_to_firestore('usuarios', users)
            st.success(f'{num_users} usuarios añadidos a Firestore')
            st.dataframe(pd.DataFrame(users))

    with col2:
        st.subheader('Productos')
        num_products = st.number_input('Número de productos a generar', min_value=1, max_value=100, value=10)
        if st.button('Generar y Añadir Productos'):
            with st.spinner('Eliminando productos existentes...'):
                delete_collection('productos')
            with st.spinner('Generando y añadiendo nuevos productos...'):
                products = generate_fake_products(num_products)
                add_data_to_firestore('productos', products)
            st.success(f'{num_products} productos añadidos a Firestore')
            st.dataframe(pd.DataFrame(products))

#----------------------------------------------------------
#Datos
#----------------------------------------------------------
with tab_datos:
    st.write('Esta función muestra datos de usuarios y productos almacenados en una base de datos Firestore, permitiendo una visualización organizada y fácil acceso a la información.')
    tab_user, tab_productos = st.tabs(["Usuarios", "Productos"])
    with tab_user:       
            
        users = db.collection('usuarios').stream()   # Obtener datos de una colección de Firestore 
        users_data = [doc.to_dict() for doc in users] # Convertir datos a una lista de diccionarios
        
        # Crear DataFrame
        
        df_users = pd.DataFrame(users_data)  
        column_order = ['nombre', 'email', 'edad', 'ciudad']  # Reordenar las columnas
        df_users = df_users.reindex(columns=column_order)   

        st.dataframe(df_users)
    with tab_productos:    
             
        users = db.collection('productos').stream()  # Obtener datos de una colección de Firestore
        users_data = [doc.to_dict() for doc in users]  # Convertir datos a una lista de diccionarios
        
         # Crear DataFrame
         
        df_products = pd.DataFrame(users_data)
        column_order = ['nombre', 'categoria', 'precio', 'stock']   # Reordenar las columnas
        df_products = df_products.reindex(columns=column_order)
        
        st.dataframe(df_products)

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio: 
    
    df_users.columns = df_users.columns.str.strip()  # Elimina espacios en blanco en los nombres de las columnas   
    st.title("Análisis Exploratorio")
    
    st.markdown("### Aqui las primeras 5 filas de los datos:")
    st.write(df_users.head())   # Mostrar primeras 5 filas del DataFrame de usuarios
    
    st.markdown("### Tipos de datos de las columnas de los datos de usuarios:")
    st.write(df_users.dtypes)
    
    st.markdown("### Columnas con valores nulos en los datos de usuarios:")
    st.write(df_users.isnull().sum())
    
    st.markdown("### Resumen Usuario:")   # Mostrar resumen estadístico de usuarios
    st.dataframe(df_users.describe())
    
    st.markdown("### Resumen productos:")  # Mostrar resumen estadístico de productos
    st.dataframe(df_products.describe())
    
    st.markdown("### Frecuencia de valores únicos:")
    
    columna_categorica = st.selectbox('Selecciona una columna', df_users.columns)  # Para seleccionar la columna categórica
    
     # Verificar si la columna seleccionada es de tipo categórico (object) o numérico
     
    if df_users[columna_categorica].dtype == 'object':
        st.write(f"Frecuencia de valores únicos en la columna '{columna_categorica}':")
        st.dataframe(df_users[columna_categorica].value_counts())
    
    elif df_users[columna_categorica].dtype in ['int64', 'float64']:  # Columnas numéricas como 'edad'
        st.write(f"Frecuencia de valores en la columna '{columna_categorica}':")
        st.dataframe(df_users[columna_categorica].value_counts())
    
    else:
        st.write(f"La columna '{columna_categorica}' no es válida. Selecciona una columna válida.")
        
    
#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------

with tab_Filtrado_Básico:
    st.title("Filtro Básico")
    st.markdown(" ### Filtrar datos usando condiciones simples.")

    # Selección de columna para filtrar
    columna_seleccionada = st.selectbox('Selecciona una columna para filtrar', df_users.columns, key='columna_filtro_unica')

    # Verificar si la columna es categórica u ofrece valores numéricos
    if df_users[columna_seleccionada].dtype == 'object':
        valor_filtro = st.selectbox(f'Selecciona un valor para filtrar en la columna {columna_seleccionada}', 
        df_users[columna_seleccionada].astype(str).unique(), key='valor_filtro_unico')
        
    else:
        min_valor = float(df_users[columna_seleccionada].min())
        max_valor = float(df_users[columna_seleccionada].max())
        valor_filtro = st.number_input(f'Ingresa un valor para filtrar en la columna {columna_seleccionada}', 
        min_value=min_valor, max_value=max_valor, key='valor_filtro_num')

    # Selección de operador de comparación (Igual, Diferente, Mayor que, Menor que)
    operador = st.radio('Selecciona un operador de comparación', ('Igual', 'Diferente', 'Mayor que', 'Menor que'), key='operador_comparacion')

    # Aplicar el filtro según el tipo de columna y el operador seleccionado
    if operador == 'Igual':
        df_filtrado = df_users[df_users[columna_seleccionada] == valor_filtro]
    elif operador == 'Diferente':
        df_filtrado = df_users[df_users[columna_seleccionada] != valor_filtro]
    elif operador == 'Mayor que' and df_users[columna_seleccionada].dtype != 'object':
        df_filtrado = df_users[df_users[columna_seleccionada] > valor_filtro]
    elif operador == 'Menor que' and df_users[columna_seleccionada].dtype != 'object':
        df_filtrado = df_users[df_users[columna_seleccionada] < valor_filtro]
    else:
        st.write("El operador seleccionado no es válido para una columna categórica.")

    # Mostrar los datos filtrados y la tabla
    st.markdown(f"### Datos filtrados por la columna '{columna_seleccionada}' con el valor '{valor_filtro}':")
    st.dataframe(df_filtrado)


#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------


with tab_Filtro_Final_Dinámico:
    st.title("Filtro Final Dinámico")
    st.markdown("### Aplica filtros dinámicos y actualiza los resultados automáticamente.")

    # Selección de columna para filtrar
    columna_seleccionada = st.selectbox('Selecciona una columna para filtrar', df_users.columns, key='columna_filtro_dinamico')

    # Verificar si la columna seleccionada es categórica o numérica
    if df_users[columna_seleccionada].dtype == 'object':
        valor_filtro = st.selectbox(f'Selecciona un valor para filtrar en la columna {columna_seleccionada}', 
        df_users[columna_seleccionada].astype(str).unique(), key='valor_filtro_dinamico')
    else:
        min_valor = float(df_users[columna_seleccionada].min())
        max_valor = float(df_users[columna_seleccionada].max())
        valor_filtro = st.number_input(f'Ingresa un valor para filtrar en la columna {columna_seleccionada}', 
        min_value=min_valor, max_value=max_valor, key='valor_filtro_num_dinamico')

    # Aplicar el filtro
    df_filtrado = df_users[df_users[columna_seleccionada] == valor_filtro]

    # Mostrar los criterios de filtrado aplicados
    st.markdown(f"**Criterios de filtrado aplicados**: Columna = '{columna_seleccionada}', Valor = '{valor_filtro}'")

   
    st.markdown("### Tabla de datos filtrados:")   # Mostrar la tabla de datos filtrados
    st.dataframe(df_filtrado)

    
    st.markdown("### Resumen estadístico del DataFrame filtrado:") # Resumen estadístico dinámico del DataFrame filtrado
    st.dataframe(df_filtrado.describe())


    if df_users[columna_seleccionada].dtype != 'object':  # Gráfico de distribución si la columna es numérica
        st.markdown("### Gráfico de distribución de la columna filtrada:")
        st.bar_chart(df_filtrado[columna_seleccionada])

    
    else:                                                 # Gráfico de barras para columna categórica
        st.markdown(f"### Gráfico de frecuencia de valores en la columna '{columna_seleccionada}':")
        
         # Crear gráfico con Seaborn y Matplotlib
         
        plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
        sns.barplot(x=df_filtrado[columna_seleccionada].value_counts().index,
                y=df_filtrado[columna_seleccionada].value_counts().values,
                color='lightgreen', width=0.1)  # Ancho ajustado y color
    
         # Mostrar gráfico en Streamlit
        st.pyplot(plt)
    
    st.markdown(f"### Total de registros filtrados: {len(df_filtrado)}") # Mostrar la cantidad de datos filtrados

