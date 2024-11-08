import random
from faker import Faker
import streamlit as st 
import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt
import firebase_admin  
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.subheader("Proyecto Integrador")


if not firebase_admin._apps:    # Verificar si ya existe una instancia de la aplicación
    firebase_credentials = st.secrets["FIREBASE_CREDENTIALS"]  # Cargar las credenciales de Firebase desde los secretos de Streamlit
    secrets_dict = firebase_credentials.to_dict()  # Convertir las credenciales a un diccionario Python
    cred = credentials.Certificate(secrets_dict)   # Crear un objeto de credenciales usando el diccionario 
    app = firebase_admin.initialize_app(cred)     # Inicializar la aplicación de Firebase con las credenciales
db = firestore.client()   # Obtener el cliente de Firestore


tad_descripcion, tab_Generador, tab_datos, tab_Análisis_Exploratorio, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Generador de datos", "Datos", "Análisis Exploratorio", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Descripciòn del sitio.
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

    -   Resumen de los   Chronos Manager ha mejorado la gestión de horarios, el control de accesos y la validación de ausencias en áreas administrativas, optimizando el flujo de trabajo y garantizando la seguridad.
    
    -   Logros alcanzados: Se logró una administración centralizada y automatizada de los horarios, con un control preciso de accesos, horas extras y ausencias, reduciendo los errores y aumentando la productividad.
    
    -   Dificultades encontradas: Se presentaron desafíos en la integración con sistemas de control de acceso preexistentes y en la adaptación a las necesidades específicas de cada empresa.

    -   Aportes personales: Nuestras contribuciónes se centran en el desarrollo de funcionalidades de validación de ausencias y en la personalización de la interfaz de usuario, buscando mejorar la experiencia del administrador en el manejo de datos y control de accesos.
    ''')

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------

# Generador de registros de empleados
def generate_employee_records(n):
    empleados = [
        {'ID': '001', 'Nombre': 'Juan Pérez'},
        {'ID': '002', 'Nombre': 'Ana Gómez'},
        {'ID': '003', 'Nombre': 'Carlos Ruiz'},
        {'ID': '004', 'Nombre': 'Laura Díaz'},
        {'ID': '005', 'Nombre': 'Sofía Castillo'},
        {'ID': '007', 'Nombre': 'Manuel Longas'},
        {'ID': '008', 'Nombre': 'Dario Gomez'},
        {'ID': '009', 'Nombre': 'Donal Trump'},
        {'ID': '010', 'Nombre': 'James Rodriguez'},
        {'ID': '011', 'Nombre': 'Esperanza Gomez'},
        {'ID': '012', 'Nombre': 'Megan Fox'},
    ]

    registros = []
    fecha_inicio = datetime(2023, 1, 1)
    for _ in range(n):
        fecha = (fecha_inicio + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        empleado = random.choice(empleados)
        hora_entrada = random.choice(['08:00', '08:15', '09:00', ''])
        hora_salida = '' if hora_entrada == '' else random.choice(['17:00', '17:30', '18:00', '18:30'])
        horas_trabajadas = 0 if hora_entrada == '' else round(random.uniform(7, 9), 1)
        horas_extras = max(0, horas_trabajadas - 8)
        ausente = 'Sí' if hora_entrada == '' else 'No'

        registros.append([
            fecha, empleado['ID'], empleado['Nombre'], hora_entrada, hora_salida,
            horas_trabajadas, horas_extras, ausente
        ])

    return pd.DataFrame(registros, columns=[
        'Fecha', 'ID', 'Nombre', 'Hora Entrada', 'Hora Salida',
        'Horas Trabajadas', 'Horas Extras', 'Ausente'
    ])


with tab_Generador:    # Interfaz visual para el generador de registros
    st.write('Esta función Python genera datos ficticios de usuarios, productos y registros de acceso y horario.')
    st.subheader('Registros de Empleados')
    num_records = st.number_input('Número de registros a generar', min_value=1, max_value=5000, value=5000)
    
    if st.button('Generar Registros de Empleados'):
        # Genera y muestra los registros
        df = generate_employee_records(num_records)
        st.dataframe(df)
        df.to_csv('registro_accesos.csv', index=False, encoding='utf-8')
        st.success(f'Archivo CSV generado exitosamente con {num_records} registros.')

#----------------------------------------------------------
#Datos
#----------------------------------------------------------

with tab_datos:
    st.write('Esta función muestra datos de control de acceso, productos y registros de empleados almacenados en una base de datos Firestore, permitiendo una visualización organizada y fácil acceso a la información.')

    tab_fecha, tab_empleado, tab_registros = st.tabs(["Fecha", "Empleados", "Registros de Empleados"])

if 'df' in locals():
    with tab_fecha:
        column_order = ['Fecha', 'ID', 'Hora Entrada', 'Hora Salida', 'Horas Trabajadas', 'Horas Extras']
        df_tab_fecha = df.reindex(columns=column_order)  # Selecciona las columnas específicas para esta vista
        st.dataframe(df_tab_fecha)
        
    with tab_empleado:
        column_order = ['ID', 'Nombre']
        df_tab_empleado = df.reindex(columns=column_order)  # Selecciona solo las columnas específicas para esta vista
        st.dataframe(df_tab_empleado)
        
    with tab_registros:
        st.write('Visualización de registros de empleados generados.')
        st.dataframe(df)
        st.subheader('Filtrar registros por fecha')
        
        fecha_inicio = st.date_input('Fecha de inicio', datetime(2023, 1, 1))
        fecha_fin = st.date_input('Fecha de fin', datetime(2023, 12, 31))

        # Convertir las fechas a formato de datetime para el filtrado
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df_filtrado = df[(df['Fecha'] >= pd.to_datetime(fecha_inicio)) & (df['Fecha'] <= pd.to_datetime(fecha_fin))]
        
        st.dataframe(df_filtrado)

#-------------------------------------------------------------
# Analítica 1
#-------------------------------------------------------------

with tab_Análisis_Exploratorio:

    if 'df' in locals():
        df_users = df         
        df_users.columns = df_users.columns.str.strip()  # Elimina espacios en blanco en los nombres de las columnas   
        st.title("Análisis Exploratorio")
        
        st.markdown("### Aquí las primeras 5 filas de los datos:")
        st.write(df_users.head())  # Mostrar primeras 5 filas del DataFrame de usuarios
        
        st.markdown("### Tipos de datos de las columnas de los datos de usuarios:")
        st.write(df_users.dtypes)
        
        st.markdown("### Columnas con valores nulos en los datos de usuarios:")
        st.write(df_users.isnull().sum())
        
        st.markdown("### Resumen Usuario:")  # Mostrar resumen estadístico de usuarios
        st.dataframe(df_users.describe())
        
        columna_categorica = st.selectbox('Selecciona una columna', df_users.columns)  # Para seleccionar la columna categórica
        
        # Verificar si la columna seleccionada es de tipo categórico o numérico
        
        if df_users[columna_categorica].dtype == 'object':
            st.write(f"Frecuencia de valores únicos en la columna '{columna_categorica}':")
            st.dataframe(df_users[columna_categorica].value_counts())
        
        elif df_users[columna_categorica].dtype in ['int64', 'float64']:  # Columnas numéricas como 'edad'
            st.write(f"Frecuencia de valores en la columna '{columna_categorica}':")
            st.dataframe(df_users[columna_categorica].value_counts())
        
        else:
            st.write(f"La columna '{columna_categorica}' no es válida. Selecciona una columna válida.")
    else:
        st.write("Aún no se han generado los datos de usuarios. Por favor, genera los datos primero en la sección 'Registros de Empleados'.")

#----------------------------------------------------------------------------
# Analítica 2
#--------------------------------------------------------------------------

with tab_Filtro_Final_Dinámico:
    st.title("Filtro Final Dinámico")
    st.markdown("### Aplica filtros dinámicos y actualiza los resultados automáticamente.")

    if 'df' in locals():
        df_users = df  # Asignar el DataFrame generado a df_users

        # Selección de columna para filtrar
        columna_seleccionada = st.selectbox('Selecciona una columna para filtrar', df_users.columns, key='columna_filtro_dinamico')

        # Verificar si la columna seleccionada es categórica, numérica o de fecha
        if df_users[columna_seleccionada].dtype == 'object':
            valor_filtro = st.selectbox(f'Selecciona un valor para filtrar en la columna {columna_seleccionada}', 
                                        df_users[columna_seleccionada].astype(str).unique(), key='valor_filtro_dinamico')
        
        elif df_users[columna_seleccionada].dtype in ['int64', 'float64']:
            # Filtro para columnas numéricas
            min_valor = float(df_users[columna_seleccionada].min())
            max_valor = float(df_users[columna_seleccionada].max())
            valor_filtro = st.number_input(f'Ingresa un valor para filtrar en la columna {columna_seleccionada}', 
                                           min_value=min_valor, max_value=max_valor, key='valor_filtro_num_dinamico')
        
        elif pd.api.types.is_datetime64_any_dtype(df_users[columna_seleccionada]):
            # Filtro para columnas de tipo fecha
            min_valor = df_users[columna_seleccionada].min()
            max_valor = df_users[columna_seleccionada].max()
            valor_filtro = st.date_input(f'Selecciona una fecha para filtrar en la columna {columna_seleccionada}', 
                                         value=min_valor, min_value=min_valor, max_value=max_valor, key='valor_filtro_fecha_dinamico')
        
        else:
            st.write("Tipo de columna no compatible con el filtro.")
            valor_filtro = None

        # Aplicar el filtro solo si `valor_filtro` tiene un valor válido
        if valor_filtro is not None:
            if isinstance(valor_filtro, pd.Timestamp):  # Convertir Timestamp a string o date si es necesario
                valor_filtro = valor_filtro.date()
            df_filtrado = df_users[df_users[columna_seleccionada] == valor_filtro]
            st.markdown(f"**Criterios de filtrado aplicados**: Columna = '{columna_seleccionada}', Valor = '{valor_filtro}'")
            st.markdown("### Tabla de datos filtrados:")
            st.dataframe(df_filtrado)
        else:
            st.write("No se pudo aplicar el filtro.")

