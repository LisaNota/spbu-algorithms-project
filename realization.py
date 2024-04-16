import numpy as np

# Параметры задачи
r_min = 1  # минимальный радиус цилиндра
r_max = 10  # максимальный радиус цилиндра
z_min = 1 # миниальное положение вдоль оси z
z_max = 1000  # максимальное положение вдоль оси z
alpha = 0.6  # коэффициент теплопроводности
T_top = 70.0 # заданная температура на верхней границе
T0 = 30.0  # начальная температура

# Функция распределения источинка тепла
def Q(r, z, t):
    if z < 50:
        return 10
    if z > 950:    
        return -10
    
    return 0

# Шаги по радиусу и по оси z
delta_r = 1
delta_z = 10

# Временной шаг
delta_t = 1

# Количество шагов по времени
num_time_steps = 1000

# Размеры сетки
num_r_points = int((r_max - r_min) / delta_r) + 1
num_z_points = int((z_max - z_min) / delta_z) + 1

# Создание сетки для температур
T = np.zeros((num_r_points, num_z_points))

# Установка начальных условий
T[:, :] = T0

# Цикл по времени
for t in range(num_time_steps):
    # Создание временной копии температур
    T_temp = np.copy(T)
    
    #Процернт выполнения
    if t % 100 == 0:
        print(t / num_time_steps * 100, '%')

    # Цикл по радиусу
    for i in range(0, num_r_points):
        # Цикл по оси z
        for j in range(0, num_z_points):
            if j == num_z_points - 1:
                T[i, j] = T_top
                continue
            
            if j == 0:
                T[i, j] = T_temp[i, j] + delta_t * Q(r_min + i * delta_r, z_min + j * delta_z, t * delta_t)
                continue

            if i == 0 or i == num_r_points - 1:
                continue

            # Численное решение уравнения теплопроводности
            T[i, j] = T_temp[i, j] + (alpha * delta_t / (delta_r ** 2)) * (T_temp[i + 1, j] - 2 * T_temp[i, j] + T_temp[i - 1, j]) \
                                    + (alpha * delta_t / (delta_z ** 2)) * (T_temp[i, j + 1] - 2 * T_temp[i, j] + T_temp[i, j - 1]) \
                                    + delta_t * Q(r_min + i * delta_r, z_min + j * delta_z, t * delta_t)
    
    # Применение граничных условий (температура на верхней границе)
    T[:, -1] = T_top

# Вывод результатов по одному радиусу
print(T[1, :])
