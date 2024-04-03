import numpy as np

# Параметры задачи
z_min = 1 # миниальное положение вдоль оси z
z_max = 1000  # максимальное положение вдоль оси z
alpha = 50  # коэффициент теплопроводности
T_top = 70.0 # заданная температура на верхней границе
T0 = 30.0  # начальная температура

# Функция распределения источинка тепла
def Q(z, t, Ti):
    if z < 5:
        return 1
    if z > 980:    
        return 0.01* (70 - Ti) #Пытаюсь симулировать потерю тепла
    
    return 0

# Шаги по радиусу и по оси z
delta_z = 10

# Временной шаг
delta_t = 1

# Количество шагов по времени
num_time_steps = 10000

# Размеры сетки
num_z_points = int((z_max - z_min) / delta_z) + 1

# Создание сетки для температур
T = np.zeros((num_z_points))

# Установка начальных условий
T[:] = T0

# Цикл по времени
for t in range(num_time_steps):
    # Создание временной копии температур
    T_temp = np.copy(T)
    
    #Процернт выполнения
    if t % 1000 == 0:
        print(t / num_time_steps * 100, '%')

    # Цикл по оси z
    for j in range(0, num_z_points):
        if j == num_z_points - 1:
            T[j] = T_temp[j] + delta_t * Q(z_min + j * delta_z, t * delta_t, T_temp[j]) #Пытаюсь симулировать потерю тепла
            continue
        
        if j == 0:
            T[j] = T_temp[j] + delta_t * Q(z_min + j * delta_z, t * delta_t, T_temp[j]) #Пытаюсь симулировать нагрев
            T[j] = T[j] - (T_temp[j] - T_temp[j + 1]) * 0.5 #Пытаюсь симулировать передачу тепла
            continue

        # Численное решение уравнения теплопроводности
        T[j] = T_temp[j] + (alpha * delta_t / (delta_z ** 2)) * (T_temp[j + 1] - 2 * T_temp[j] + T_temp[j - 1]) \
                                + delta_t * Q(z_min + j * delta_z, t * delta_t, T_temp[j])

    # Применение граничных условий (температура на верхней границе)
    #T[num_z_points - 1] = T_top

# Вывод результатов по одному радиусу
print(T)