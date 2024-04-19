import streamlit as st
import numpy as np
import calculations as calc
import matplotlib.pyplot as plt
import time as tm


def random_L():
    L = np.zeros((10, 10, 10))
    for time in range(L.shape[0]):
        for height in range(L.shape[1]):
            for radius in range(L.shape[2]):
                L[time, height, radius] = 100 - height * 5 + radius + time * 2

    return L

@st.cache_data()
def calculate_L(length=10, radius=10, time=10, magma=100, final_temperature=100, alpha=0.1, capacity=4.2, dl=1, dr=1, dt=1):
    L = calc.run_program(length, radius, time, magma, final_temperature, alpha, capacity, dl, dr, dt)
    return L


# Поля для ввода параметров
length = st.number_input("Length", value=10)
radius = st.number_input("Radius", value=10)
time = st.number_input("Time", value=10)
magma = st.number_input("Magma", value=100)
final_temperature = st.number_input("Final Temperature", value=100)
alpha = st.number_input("Alpha", value=0.1)
capacity = st.number_input("Capacity", value=4.2)
dl = st.number_input("dl", value=1)
dr = st.number_input("dr", value=1)
dt = st.number_input("dt", value=1)


# Зададим L[время][высота][радиус]
# L = calculate_L()
L = random_L()

x = [[] for i in range(L.shape[0])]
y = [[] for i in range(L.shape[0])]
z = [[] for i in range(L.shape[0])]
temperature = [[] for i in range(L.shape[0])]

for time in range(L.shape[0]):
    for height in range(L.shape[1]):
        for radius in range(L.shape[2]):
            theta = np.linspace(0, 2 * np.pi, 45)
            for fi in theta:
                x[time].append(radius * np.sin(fi))
                y[time].append(radius * np.cos(fi))
                z[time].append(height)
                temperature[time].append(L[time, height, radius])

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Рисуем точки, используя температуру для цветовой карты
vmin = np.min(temperature)  # Minimum temperature value
vmax = np.max(temperature)  # Maximum temperature value

st.write("Temperature Steps:")
if st.checkbox("Real-time"):
    # Проггресс бар для отображения времени
    progress = st.progress(0)

    for step in range(L.shape[0]):
        sc = ax.scatter(x[step], y[step], z[step], c=temperature[step], cmap='coolwarm', alpha=0.3, vmin=vmin, vmax=vmax)
        # Добавляем colorbar для отображения температуры
        fig.colorbar(sc)
        # Выводим график в Streamlit
        st.pyplot(fig)

        # Обновляем прогресс бар
        progress.progress((step + 1) / L.shape[0])
        tm.sleep(2)

        # Обновляем страницу stremlit
        
        
   
else:
    step = st.slider("Step", min_value=0, max_value=L.shape[0]-1, value=0)
    sc = ax.scatter(x[step], y[step], z[step], c=temperature[step], cmap='coolwarm', alpha=0.3, vmin=vmin, vmax=vmax)

    # Добавляем colorbar для отображения температуры
    fig.colorbar(sc)

    # Выводим график в Streamlit
    st.pyplot(fig)
