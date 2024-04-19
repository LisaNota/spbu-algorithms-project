"""
To run the Streamlit app, use the following command: streamlit run app/streamlit.py
"""
import streamlit as st
import numpy as np
import calculations as calc
import time as tm
import matplotlib.pyplot as plt


def random_L():
    # Generate a random L matrix
    L = np.zeros((10, 10, 10))
    for time in range(L.shape[0]):
        for height in range(L.shape[1]):
            for radius in range(L.shape[2]):
                L[time, height, radius] = 100 - height * 5 + radius + time * 10
    return L


@st.cache_data()
def calculate_L(length=10, radius=10, time=10, magma=100, final_temperature=100, alpha=0.1, capacity=4.2, dl=1, dr=1, dt=1):
    # Calculate L using the provided parameters
    L = calc.run_program(length, radius, time, magma, final_temperature, alpha, capacity, dl, dr, dt)
    return L


# Input fields for parameters
length = st.sidebar.number_input("Length", value=100)
radius = st.sidebar.number_input("Radius", value=100)
time = st.sidebar.number_input("Time", value=100)
magma = st.sidebar.number_input("Magma", value=1300)
final_temperature = st.sidebar.number_input("Final Temperature", value=70)
alpha = st.sidebar.number_input("Alpha", value=0.56)
capacity = st.sidebar.number_input("Capacity", value=4200)
dl = st.sidebar.number_input("dl", value=10)
dr = st.sidebar.number_input("dr", value=10)
dt = st.sidebar.number_input("dt", value=1)


# Generate L matrix
#L = calculate_L(length, radius, time, magma, final_temperature, alpha, capacity, dl, dr, dt)
L = random_L()

# Initialize empty lists for coordinates and temperature
x = [[] for _ in range(L.shape[0])]
y = [[] for _ in range(L.shape[0])]
z = [[] for _ in range(L.shape[0])]
temperature = [[] for _ in range(L.shape[0])]

# Generate coordinates and temperature values for each point in L
for time in range(L.shape[0]):
    for height in range(L.shape[1]):
        for radius in range(L.shape[2]):
            theta = np.linspace(0, 2 * np.pi, 45)
            for fi in theta:
                x[time].append(radius * np.sin(fi))
                y[time].append(radius * np.cos(fi))
                z[time].append(height)
                temperature[time].append(L[time, height, radius])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the color range for the temperature values
vmin = np.min(temperature)  # Minimum temperature value
vmax = np.max(temperature)  # Maximum temperature value

T = 0.5

st.write("Temperature Steps:")
if st.checkbox("Real-time"):
    # Progress bar and text for displaying the current frame
    progress = st.progress(0.0)
    frame_text = st.text("Frame 0/{}".format(L.shape[0]))
    image = st.empty()

    sc = ax.scatter(x[0], y[0], z[0], c=temperature[0], cmap='coolwarm', alpha=0.3, vmin=vmin, vmax=vmax)
    fig.colorbar(sc)

    image.pyplot(fig)
    tm.sleep(T)

    frame_text.text("Frame 1/{}".format(L.shape[0]))
    progress.progress(0 / (L.shape[0]))


    for step in range(1, L.shape[0]):
        # Remove the previous plot and create a new one for the current frame
        ax.clear()
        ax.scatter(x[step], y[step], z[step], c=temperature[step], cmap='coolwarm', alpha=0.3, vmin=vmin, vmax=vmax)

        # Add a delay to simulate real-time visualization
        image.pyplot(fig)
        tm.sleep(T)

        # Update the progress bar and frame text
        frame_text.text(f"Frame {step + 1}/{L.shape[0]}")
        progress.progress((step + 1) / (L.shape[0]))

    st.button("Re-run")

else:
    # Slider for selecting a specific frame
    step = st.slider("Step", min_value=1, max_value=L.shape[0], value=0)
    sc = ax.scatter(x[step-1], y[step-1], z[step-1], c=temperature[step-1], cmap='coolwarm', alpha=0.3, vmin=vmin, vmax=vmax)

    # Add a colorbar to display the temperature
    fig.colorbar(sc)

    # Display the plot in Streamlit
    st.pyplot(fig)

# Display the amount of heat that has been transferred at the upper boundary
st.write("Heat transferred at the upper boundary:", calc.amount_of_heat(alpha, radius, L), "J")