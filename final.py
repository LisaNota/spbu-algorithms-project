import tkinter as tk
import numpy as np


class GUI:
    """
    Класс, реализующий интерфейс
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Проблема Еллоустоунского зоопарка")
        self.root.geometry('800x600')
        
        self.create_frames()
        self.create_settings()
        self.water_charactericstics()
        self.partitioning_parameters()

    def create_frames(self):
        self.canvas = tk.Canvas(self.root, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.place(relx=0, rely=0.0)

        self.line1 = self.canvas.create_line(0, 240, 350, 240)
        self.line2 = self.canvas.create_line(350, 0, 350, 600)
        self.line3 = self.canvas.create_line(0, 360, 350, 360)
        
    def create_settings(self):
        self.lbl = tk.Label(self.root, text="Входные данные", font=("Arial", 16))
        self.lbl.place(relx=0.1, rely=0.01)

        self.lblfunc = tk.Label(self.root, text="Длина канала", font=("Arial", 14))
        self.lblfunc.place(relx=0.027, rely=0.075)

        self.length_entry = tk.Entry(self.root, width=15)
        self.length_entry.place(relx=0.3, rely=0.085)
        self.length_entry.insert(0, 100)

        self.lbl1 = tk.Label(self.root, text="Радиус канала", font=("Arial", 14))
        self.lbl1.place(relx=0.027, rely=0.14)

        self.radius_entry = tk.Entry(self.root, width=15)
        self.radius_entry.place(relx=0.3, rely=0.15)
        self.radius_entry.insert(0, 100)

        self.lblfunc1 = tk.Label(self.root, text="Температура магмы", font=("Arial", 14))
        self.lblfunc1.place(relx=0.027, rely=0.205)

        self.magma_entry = tk.Entry(self.root, width=15)
        self.magma_entry.place(relx=0.3, rely=0.215)
        self.magma_entry.insert(0, 1300)

        self.lbl2 = tk.Label(self.root, text="Температура жидкости ", font=("Arial", 14))
        self.lbl2.place(relx=0.027, rely=0.27)

        self.lbl3 = tk.Label(self.root, text="у поверхности", font=("Arial", 14))
        self.lbl3.place(relx=0.027, rely=0.32)

        self.final_entry = tk.Entry(self.root, width=15)
        self.final_entry.place(relx=0.3, rely=0.31)
        self.final_entry.insert(0, 70)
    

    def water_charactericstics(self):
        self.lbl = tk.Label(self.root, text="Характеристики воды", font=("Arial", 16))
        self.lbl.place(relx=0.08, rely=0.41)

        self.lblfunc1 = tk.Label(self.root, text="Теплопроводность", font=("Arial", 14))
        self.lblfunc1.place(relx=0.027, rely=0.47)

        self.alpha_entry = tk.Entry(self.root, width=15)
        self.alpha_entry.place(relx=0.3, rely=0.48)
        self.alpha_entry.insert(0, 0.56)

        self.lblfunc2 = tk.Label(self.root, text="Теплоемкость", font=("Arial", 14))
        self.lblfunc2.place(relx=0.027, rely=0.535)

        self.c_entry = tk.Entry(self.root, width=15)
        self.c_entry.place(relx=0.3, rely=0.545)
        self.c_entry.insert(0, 4200)


    def partitioning_parameters(self):
        self.lbl = tk.Label(self.root, text="Параметры разбиения", font=("Arial", 16))
        self.lbl.place(relx=0.08, rely=0.62)

        self.lblfunc1 = tk.Label(self.root, text="Шаг по длине", font=("Arial", 14))
        self.lblfunc1.place(relx=0.027, rely=0.68)

        self.delta_length_entry = tk.Entry(self.root, width=15)
        self.delta_length_entry.place(relx=0.3, rely=0.69)
        self.delta_length_entry.insert(0, 100)

        self.lblfunc2 = tk.Label(self.root, text="Шаг по радиусу", font=("Arial", 14))
        self.lblfunc2.place(relx=0.027, rely=0.745)

        self.delta_radius_entry = tk.Entry(self.root, width=15)
        self.delta_radius_entry.place(relx=0.3, rely=0.755)
        self.delta_radius_entry.insert(0, 10)

        self.lblfunc3 = tk.Label(self.root, text="Шаг по времени", font=("Arial", 14))
        self.lblfunc3.place(relx=0.027, rely=0.81)

        self.time_entry = tk.Entry(self.root, width=15)
        self.time_entry.place(relx=0.3, rely=0.82)
        self.time_entry.insert(0, 100)

        but = tk.Button(self.root, text="Создать модель", width=28, font=("Arial", 14),
                          command=lambda: run_program(int(self.length_entry.get()), int(self.radius_entry.get()), 1000,
                                                      int(self.magma_entry.get()), int(self.final_entry.get()), 
                                                      float(self.alpha_entry.get()), float(self.c_entry.get()),
                                                      int(self.delta_length_entry.get()), int(self.delta_radius_entry.get()),
                                                      int(self.time_entry.get()), self.root),
                          bg="#DDDDDD", activebackground="#CCCCCC", relief=tk.GROOVE)
        but.place(relx=0.024, rely=0.89)
        
def from_heat_to_temperature(Q: int, capacity: float, po: float, radius:int, h: int) -> float:
    """
    Параметры функции:
    Q: количество тепла, передаваемого источником (мощность нагрева)
    capacity: удельная теплоемкость воды
    m: масса воды

    Возвращает разницу в температуре после нагрева
    из формулы Q = c*m*\delta t

    m = p * V
    p - плотность воды
    V - объем
    V = pi * (r) * 2 * h

    """
    V = 2 * np.pi * radius * h
    m = po * V
    delta_t = Q / (capacity*m)
    return delta_t

def amount_of_heat(initial_temperature: float, final_temperature: float, capacity: int, po: int, radius: int, h: int):
    """
    Вычисление тепла, выделяемого на поверхности.
    Используется формула 
    Q = c*m*\delta t
    """
    V = 2 * np.pi * radius * h
    m = po * V
    delta_t = initial_temperature - final_temperature
    Q = capacity * m * delta_t
    return Q


def run_program(length:int, radius:int, time: int, magma:int, final_temperature:int, alpha:float, capacity:float, dl:int, dr:int, dt:int, root: tk.Tk):
    """
    Вычисление температуры в канале и тепла, испаряющегося в поверхность
    Входные параметры:
    length - длина канала
    radius - радиус канала
    time - количество временных шагов
    magma - мощность нагрева магмы
    final_temperature - температура воды у поверхности
    alpha - удельная теплопроводность воды
    capacity - удельная теплоемкость воды
    dl - шаг по длине канала
    dr - шаг по радиусу
    dt - шаг по времени
    root - интерфейс
    """
    # Количество шагов по радиусу, длине, времени
    number_radius_steps = radius // dr + ((radius % dr) != 0)  
    number_length_steps = length // dl + ((length % dl) != 0)
    number_time_steps = time // dt + ((time % dt) != 0)
    Q = magma * 1000000 # Дж
    po = 1000 #кг/м^3


    L = np.ndarray((number_length_steps, number_time_steps, number_radius_steps))
    
    for i in range(len(L)):
        L[i][0] = np.random.normal(100, 3, number_radius_steps)
        L[i][0, 0] = L[i][0, 0] * 0.9 

    for el in range(len(L)): # Каждое кольцо 
        for j in range(1, number_time_steps): # каждый промежуток времени
            L[el][j,0] = (L[el][j-1, 0] + ((alpha * dt)/(dr * (dr**2))) * (L[el][j-1, 1] - 2*(L[el][j-1, 0]) + L[el][j-1, 1])) + float(from_heat_to_temperature(Q, capacity, po, dr, dl))*(-1)
            for i in range(1, number_radius_steps - 1): # каждый радиус
                L[el][j, i] = (L[el][j-1, i] + ((alpha * dt)/((i*dr) * (dr**2))) * (L[el][j-1, i+1] - 2*(L[el][j-1, i]) + L[el][j-1, i-1])) * \
                    0.97 + float(from_heat_to_temperature(Q, capacity, po, dr, dl))*(1-0.01*i)
            L[el][j, number_radius_steps-1] = (L[el][j-1, number_radius_steps-1] + ((alpha * dt)/(((number_radius_steps-1)*dr) * (dr**2))) * \
            (L[el][j-1, (number_radius_steps - 2)] - 2*(L[el][j-1, (number_radius_steps - 1)]) + L[el][j-1, (number_radius_steps - 2)])) * 0.97 + float(from_heat_to_temperature(Q, capacity, po, dr, dl)) * 2
            
    results_str = ""
    for i in range(L.shape[0]):
        results_str += f"Layer {i + 1}:\n"
        for j in range(L.shape[1]):
            results_str += np.array_str(L[i, j], precision=2, suppress_small=True) + "\n"
        results_str += "\n"

    result_text = tk.Text(root, font=("Arial", 8), wrap="word")
    result_text.insert(tk.END, results_str)
    result_text.place(relx=0.5, rely=0.0, relwidth=0.4, relheight=1.0)

    scrollbar = tk.Scrollbar(root, command=result_text.yview)
    scrollbar.place(relx=0.995, rely=0.0, relheight=1.0, anchor="ne")

    result_text.config(yscrollcommand=scrollbar.set)

    answer = amount_of_heat(np.mean(L[-1][0]), final_temperature, capacity, po, dt, dl) 
    answer_window = tk.Toplevel()
    answer_window.title("Ответ")
    
    # Создание текстового поля для отображения ответа
    answer_text = tk.Text(answer_window, font=("Arial", 12), wrap="word")
    answer_text.insert(tk.END, f"Количество тепла, выделяемого на поверхности: {answer/1000000000} МДж")
    answer_text.pack()

   
def main():
    root = tk.Tk()
    app = GUI(root)

    root.mainloop()
    

if __name__ == "__main__":
    main()
