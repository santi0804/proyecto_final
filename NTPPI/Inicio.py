import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("CHRONOS MANAGER")
st.subheader("GESTOR DE HORARIOS Y CONTROL DE ACCESOS")
st.subheader("Brindamos soluciones a las gestiones administrativas con nuestro equipo Alpha Developers")

image_path = "./static/control acceso.png"  # Reemplaza con la ruta de la foto
image = Image.open(image_path)  # Imagen de fondo
horizontal_image = image.resize((1100, 350)) 
st.image(horizontal_image) 


st.header("Equipo Alpha Developers")   # Integrantes


col1, col2, col3 = st.columns(3)

with col1:
    st.image("./static/santi.jpeg", width=200)  # Reemplaza con la ruta de la foto
    st.write("**Santiago Tamayo**")
    st.write("Desarrollador de Software")
    

with col2:
    st.image("./static/anderson.jpeg", width=170)  # Reemplaza con la ruta de la foto
    st.write("**Anderson Alzate**")
    st.write("Desarrollador de Software")
    
    
with col3:
    st.image("./static/jorge.jpeg", width=225)  # Reemplaza con la ruta de la foto
    st.write("**Jorge Uribe**")
    st.write("Desarrollador de Software")


# Descripción del proyecto
st.header("Sobre el Proyecto")
st.write("""
[Escribe aquí una breve descripción del proyecto, incluyendo el objetivo principal, la problemática que aborda y el enfoque que se utiliza. Puedes ser creativo y usar un lenguaje atractivo.]
""")

# Más información
st.header("Más Información")

# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas

st.write("""
[Agrega la información adicional que consideres relevante.]
""")

# Footer con links
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.google.com">Google</a> |
        <a href="https://www.facebook.com">Facebook</a> |
        <a href="https://www.linkedin.com">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)