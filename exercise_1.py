import os
import numpy as np
import matplotlib.pyplot as plt

def f(x,A):
    return -(A+47)*np.sin(np.sqrt(np.abs(x/2+(A+47))))-x*np.sin(np.sqrt(np.abs(x-(A+47))))

#параметры
A=512
x_values = np.linspace(-512, 512, 800)

#расчёт координат
y_values = f(x_values, A)
data = [{"x": x, "y": y} for x, y in zip(x_values, y_values)]

#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')

#сохранение в txt
with open('results/function_values.txt', 'w') as file:
    # Заголовок
    file.write('x    f(x)\n')
    # Запись значений функции
    for x, y in zip(x_values, y_values):
        file.write(f'{x:.4f}    {y:.4f}\n')

#построение графика функции
plt.figure(figsize=(16, 9))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()