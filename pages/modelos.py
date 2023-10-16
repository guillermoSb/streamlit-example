import tensorflow as tf
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

"""
### Predicción Precio Gasolina Superior
"""
superior_df = pd.read_csv('data/precios_gasolina.csv', parse_dates = ['fecha'], index_col = ['fecha'])
superior_df = superior_df.drop(['tipo_cambio', 'regular', 'diesel', 'bunker', 'cilindro'], axis = 1)
y = superior_df[['superior']]
scaler = StandardScaler()
y = scaler.fit_transform(y.values.reshape(-1, 1))
# importar modelo models/gasolina_superior.h5
new_model = tf.keras.models.load_model('models/gasolina_superior.h5')
new_model.summary()

# Seleccionar año, mes y día entre 2023 y 2024

year = st.slider('Año', 2023, 2024, 2023)
month = st.slider('Mes', 1, 12, 1)
day = st.slider('Día', 1, 31, 1)

# Boton para predecir

if st.button('Predecir'):

    # Predecir
    prediction = new_model.predict([[year, month, day]])
    prediction = scaler.inverse_transform(prediction)
    # Visualizar predicción
    st.write(f'El precio de la gasolina superior en la fecha seleccionada es: {prediction[0][0]}')