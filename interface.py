import tkinter as tk

class GUI:
    """
    Класс, реализующий интерфейс
    """

    def init(self, root):
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
