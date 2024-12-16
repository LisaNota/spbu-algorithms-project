import numpy as np
from matplotlib import pyplot
from tkinter import Tk, Label, Entry, Button, StringVar

# Function to run the simulation
def run_simulation():
    try:
        # Retrieve user inputs
        diff = float(diffusivity_var.get())
        length = 100
        height = 100
        time = float(time_var.get())
        nodes = int(nodes_var.get())
        start_temp = float(start_temp_var.get())
        
        top_temp = float(top_temp_var.get())
        bottom_temp = float(bottom_temp_var.get())
        left_temp = float(left_temp_var.get())
        right_temp = float(right_temp_var.get())

        # Initialization
        dx = length / nodes
        dy = height / nodes
        dt = min(dx**2 / (4 * diff), dy**2 / (4 * diff))
        t_nodes = int(time // dt)

        vec = np.zeros((nodes, nodes)) + start_temp

        # Boundary conditions
        vec[0, :] = top_temp
        vec[-1, :] = bottom_temp
        vec[:, 0] = left_temp
        vec[:, -1] = right_temp

        # Visualization setup
        fig, axis = pyplot.subplots()
        pcm = axis.pcolormesh(vec, cmap=pyplot.cm.jet, vmin=0, vmax=max(top_temp, bottom_temp, left_temp, right_temp+30))
        pyplot.colorbar(pcm, ax=axis)

        # Simulation loop
        counter = 0
        while counter < time:
            vecopy = vec.copy()
            for i in range(1, nodes - 1):
                for j in range(1, nodes - 1):
                    dd_ux = (vecopy[i - 1, j] - 2 * vecopy[i, j] + vecopy[i + 1, j]) / dx**2
                    dd_uy = (vecopy[i, j - 1] - 2 * vecopy[i, j] + vecopy[i, j + 1]) / dy**2
                    vec[i, j] = dt * diff * (dd_ux + dd_uy) + vecopy[i, j]
            counter += dt
            pcm.set_array(vec.ravel())
            axis.set_title("Distribution at t: {:.3f} [s]\nAverage temperature: {:.2f} [C]".format(counter, np.average(vec)))
            pyplot.pause(0.01)

        pyplot.show()

    except ValueError:
        print("Please enter valid numerical values!")

# GUI setup
root = Tk()
root.title("Heat Diffusion Simulation")

# Input variables
diffusivity_var = StringVar(value="10")
time_var = StringVar(value="100")
nodes_var = StringVar(value="100")
start_temp_var = StringVar(value="10")

bottom_temp_var = StringVar(value="35")
top_temp_var = StringVar(value="25")
left_temp_var = StringVar(value="30")
right_temp_var = StringVar(value="30")

# Input fields
fields = [
    ("Diffusivity (Heat Conductivity):", diffusivity_var),
    ("Time (s):", time_var),
    ("Nodes (Resolution):", nodes_var),
    ("Initial Temperature (C):", start_temp_var),
    ("Top Boundary Temperature (C):", top_temp_var),
    ("Bottom Boundary Temperature (C):", bottom_temp_var),
    ("Left Boundary Temperature (C):", left_temp_var),
    ("Right Boundary Temperature (C):", right_temp_var),
]

# Add input fields to the GUI
for i, (label_text, variable) in enumerate(fields):
    Label(root, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    Entry(root, textvariable=variable).grid(row=i, column=1, padx=10, pady=5)

# Run button
Button(root, text="Run Simulation", command=run_simulation).grid(row=len(fields), column=0, columnspan=2, pady=20)

root.mainloop()
