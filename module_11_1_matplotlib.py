import matplotlib.pyplot as plt

# Построение графика
# x = [1, 2, 3, 4, 5]
# y = [5, 0, 30, 10, 11]
# plt.plot(x, y)

# # Добавление буквенных обозначений
# plt.xlabel('Ось х')
# plt.ylabel('Ось y')
# plt.title('График для демонстрации работы matplotlib')

# Изменение цвета линии и выделение точек
# plt.plot(x, y, color='blue', marker='*', markersize=8)
# plt.show()


# Построение столбчатой диаграммы, а также комбинация её с графиком

x = ['Хлеб', 'Курица', 'Мясо', 'Гречка', 'Творог']
y = [54, 299, 699, 59, 139]
plt.bar(x, y, label='Июль 2024 г.')
plt.plot(x, y, color='red', marker='o', markersize=5)
plt.xlabel('Продукт')
plt.ylabel('Цена за кг, руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()