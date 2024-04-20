import numpy as np


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

def amount_of_heat(alpha:float, radius:int, L:np.ndarray) -> float:
    """
    Закон Фурье для теплопроводности:

    Q = −α*A*dT/dr 

    где:
        Q - количество тепла, выделяемого на поверхность,
        α - коэффициент теплопроводности воды,
        A - площадь поперечного сечения канала,
        dT/dr  - градиент температуры по радиусу.
        α
    """
    # Вычисление среднего градиента температуры на поверхности
    dTdr = np.mean(L[-1][-1])

    A = np.pi * (radius**2)
    Q = alpha * A * dTdr
    return Q


def run_program(length:int, radius:int, time: int, magma:int, final_temperature:int, alpha:float, capacity:float, dl:int, dr:int, dt:int):
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
    """
    # Количество шагов по радиусу, длине, времени
    number_radius_steps = radius // dr + ((radius % dr) != 0)  
    number_length_steps = length // dl + ((length % dl) != 0)
    number_time_steps = time // dt + ((time % dt) != 0)
    Q = magma * 1000000 # Дж
    po = 1000 #кг/м^3

    # Создание трехмерного массива для хранения температур
    L = np.ndarray((number_time_steps, number_length_steps,  number_radius_steps))
    
    for i in range(len(L)):
        L[0][i] = np.random.normal(100, 3, number_radius_steps)
        L[0][i, 0] = L[0][i, 0] * 0.9 


    for j in range(1, number_time_steps): # каждый промежуток времени
        for el in range(len(L)): # Каждое кольцо
            L[j][el,0] = (L[j-1][el, 0] + ((alpha * dt)/(dr * (dr**2))) * (L[j-1][el, 1] - 2*(L[j-1][el, 0]) + L[j-1][el, 1])) + float(from_heat_to_temperature(Q, capacity, po, dr, dl))*(-1)
            for i in range(1, number_radius_steps - 1): # каждый радиус
                L[j][el, i] = (L[j-1][el, i] + ((alpha * dt)/((i*dr) * (dr**2))) * (L[j-1][el, i+1] - 2*(L[j-1][el, i]) + L[j-1][el, i-1])) * \
                    0.97 + float(from_heat_to_temperature(Q, capacity, po, dr, dl))*(1-0.01*i)
            L[j][el, number_radius_steps-1] = (L[j-1][el, number_radius_steps-1] + ((alpha * dt)/(((number_radius_steps-1)*dr) * (dr**2))) * \
            (L[j-1][el, (number_radius_steps - 2)] - 2*(L[j-1][el, (number_radius_steps - 1)]) + L[j-1][el, (number_radius_steps - 2)])) * 0.97 + float(from_heat_to_temperature(Q, capacity, po, dr, dl)) * 2
            
    
    return L



