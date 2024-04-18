import streamlit as st
import numpy as np

import plotly.graph_objects as go


# Создание массива L для хранения температуры
L = np.zeros((11, 100, 100))  # Размерность массива: [время][высота][радиус]

# Заполнение массива L случайными значениями температуры
for t in range(11):
    L[t] = np.random.rand(100, 100)

# Добавление временной шкалы
time_slider = st.slider('Time', 0, 10, 0)  # Диапазон времени от 0 до 10, начальное значение 0

# Создание 3D цилиндрической поверхности для отображения температуры.
fig = go.Figure(data=[go.Surface(z=L[time_slider], colorscale='Viridis')])

# Настройка макета
fig.update_layout(title='Температура в канале',
                  scene=dict(aspectratio=dict(x=1, y=1, z=1),
                             aspectmode='manual'))


# Отображение 3D поверхности
st.plotly_chart(fig)
