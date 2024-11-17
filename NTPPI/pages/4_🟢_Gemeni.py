import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configura la interfaz de usuario con Streamlit
st.title("Generador de Datos - CHRONOS MANAGER")
st.sidebar.title("Opciones")

# Generar datos simulados
data = {
    "Region": ["Norte", "Sur", "Este", "Oeste", "Centro"] * 100,
    "Accesos": [500, 300, 450, 400, 550] * 100,
    "Horas_Trabajadas": [40, 35, 45, 38, 42] * 100,
    "Horas_Extras": [5, 2, 8, 4, 7] * 100,
    "Ausencias": [1, 3, 2, 4, 0] * 100,
}
df = pd.DataFrame(data)

# Selector para región
region_seleccionada = st.sidebar.selectbox("Selecciona una región:", ["Todas"] + df["Region"].unique().tolist())

# Filtrar datos por región seleccionada
if region_seleccionada == "Todas":
    datos_filtrados = df
else:
    datos_filtrados = df[df["Region"] == region_seleccionada]

# Resumen de estadísticas
resumen = datos_filtrados.groupby("Region").agg(
    Total_Accesos=("Accesos", "sum"),
    Promedio_Horas_Trabajadas=("Horas_Trabajadas", "mean"),
    Promedio_Horas_Extras=("Horas_Extras", "mean"),
    Total_Ausencias=("Ausencias", "sum"),
)

st.write(f"### Resumen de datos para: {region_seleccionada}")
st.dataframe(resumen)

# Crear gráficos
st.write("### Visualización de datos")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Total de accesos
resumen["Total_Accesos"].plot(kind="bar", color="skyblue", ax=axes[0, 0], title="Total de Accesos por Región")
axes[0, 0].set_ylabel("Accesos")
axes[0, 0].tick_params(axis="x", rotation=45)

# Promedio de horas trabajadas
resumen["Promedio_Horas_Trabajadas"].plot(kind="bar", color="lightgreen", ax=axes[0, 1], title="Promedio de Horas Trabajadas")
axes[0, 1].set_ylabel("Horas")
axes[0, 1].tick_params(axis="x", rotation=45)

# Promedio de horas extras
resumen["Promedio_Horas_Extras"].plot(kind="bar", color="orange", ax=axes[1, 0], title="Promedio de Horas Extras")
axes[1, 0].set_ylabel("Horas Extras")
axes[1, 0].tick_params(axis="x", rotation=45)

# Total de ausencias
resumen["Total_Ausencias"].plot(kind="bar", color="red", ax=axes[1, 1], title="Total de Ausencias")
axes[1, 1].set_ylabel("Ausencias")
axes[1, 1].tick_params(axis="x", rotation=45)

# Ajustar diseño y mostrar
plt.tight_layout()
st.pyplot(fig)

# Exportar resumen
st.write("### Exportar Resumen")
if st.button("Exportar a CSV"):
    resumen.to_csv(f"resumen_{region_seleccionada.lower()}_chronos_manager.csv")
    st.success(f"Resumen exportado como 'resumen_{region_seleccionada.lower()}_chronos_manager.csv'")
