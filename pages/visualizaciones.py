from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

# Load data from /data directory
importaciones_df = pd.read_csv('data/importaciones_gasolina.csv')
columns = ['Fecha', 'Diesel bajo azufre', 'Diesel ultra bajo azufre', 'Gas licuado de petróleo', 'Gasolina regular', 'Gasolina superior', 'Diesel alto azufre']
importaciones_df = importaciones_df[columns]

# Renombrando columnas
new_column_names = ['fecha', 'diesel_bajo_azufre', 'diesel_ultra_bajo_azufre', 'gas_licuado_petroleo', 'gasolina_regular', 'gasolina_superior', 'diesel_alto_azufre']
importaciones_df.columns = new_column_names

# Obtener el mes de la columna Fecha
importaciones_df['month'] = pd.DatetimeIndex(importaciones_df['fecha']).month
# Obtener el año de la columna Fecha
importaciones_df['year'] = pd.DatetimeIndex(importaciones_df['fecha']).year
# Convertir valores de importaciones a float
for column in new_column_names[1:]:
    importaciones_df[column] = importaciones_df[column].str.replace(',', '').astype(float)


"""
### Porcentaje de importaciones de combustible
"""
# ------------------------------
# Visualizar porcentaje de importaciones
# ------------------------------
# Picker de año
year = st.selectbox('Año', importaciones_df['year'].unique())
# Categories
categories = ['diesel_bajo_azufre', 'diesel_ultra_bajo_azufre', 'gas_licuado_petroleo', 'gasolina_regular', 'gasolina_superior', 'diesel_alto_azufre']
# Obtener el total de importaciones
total_importaciones = importaciones_df[importaciones_df['year'] == year][categories].sum().sum()
# Obtener el porcentaje de importaciones dos decimales
percentage_importaciones = round(importaciones_df[importaciones_df['year'] == year][categories].sum() / total_importaciones * 100,2)
# Crear dataframe para visualizar
df = pd.DataFrame({'Categorias': categories, 'Porcentaje': percentage_importaciones})    
# Visualizar gráfico
fig = px.pie(df, values='Porcentaje', names='Categorias', title=f'Porcentaje de importaciones de gasolina en {year}')
st.plotly_chart(fig)


# ------------------------------
# Visualizar importaciones en serie de tiempo
# ------------------------------

"""
### Importaciones de combustible en serie de tiempo
"""

# Picker rango de años
year = st.slider('Rango de años', 2010, 2023, (2010, 2023))
# Visualizar gráfico
fig = px.line(importaciones_df[(importaciones_df['year'] >= year[0]) & (importaciones_df['year'] <= year[1])], x='fecha', y=categories, title='Importaciones de combustible en serie de tiempo')
st.plotly_chart(fig)


