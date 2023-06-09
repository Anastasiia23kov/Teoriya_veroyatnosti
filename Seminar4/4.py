# Задача 4. Рост взрослого населения города X имеет нормальное распределение. 
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

# Z = (X - M)/ sigma
M = 174
sigma = 8

print("Bероятность того, что человек имеет рост: ")

print(f" a).больше 182 см: {(182 - M)/ sigma} => {round((100 - 84.13),2)}%")
print(f" б).больше 190 см: {(190 - M)/ sigma} => {round((100 - 97.72),2)}%")
print(f" в).от 166 см до 190 см: от {(166 - M)/ sigma} до {(190 - M)/ sigma} => {round((97.72 - 15.87),2)}%")
print(f" г).от 166 см до 182 см: от {(166 - M)/ sigma} до {(182 - M)/ sigma} => {round((84.13 - 15.87),2)}%")
print(f" д).от 158 см до 190 см: от {(158 - M)/ sigma} до {(190 - M)/ sigma} => {round((97.72 - 2.28),2)}%")
print(f" е).не выше 150 см или не ниже 190 см: {(150 - M)/ sigma}, {(190 - M)/ sigma} => {round((0.14 + 100 - 97.72),2)}%")
print(f" ё).не выше 150 см или не ниже 198 см: {(150 - M)/ sigma}, {(198 - M)/ sigma} => {round((0.14 + 100 - 99.86),2)}%")
print(f" ж).ниже 166 см: {(166 - M)/ sigma} => {15.87}%")
