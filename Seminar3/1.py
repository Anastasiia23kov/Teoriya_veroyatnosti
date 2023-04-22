# 1. Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки.

# среднее арифметическое 
n = (100+80+75+77+89+33+45+25+65+17+30+24+57+55+70+75+65+84+90+150)/20
print(f"среднее арифметическое: {n}")

# смещенную и несмещенную оценки дисперсий для данной выборки
ss = (100-n)**2 +(80-n)**2 +(75-n)**2 +(77-n)**2 +(89-n)**2 +(33-n)**2 +(45-n)**2 +(25-n)**2 +(65-n)**2 +(17-n)**2 +(30-n)**2 +(24-n)**2 +(57-n)**2 +(55-n)**2 +(70-n)**2 +(75-n)**2 +(65-n)**2 +(84-n)**2 +(90-n)**2 +(150-n)**2
print(f"смещенная оценка дисперсии: {ss/20}")
print(f"НЕсмещенная оценка дисперсии: {ss/(20-1)}")

# среднее квадратичное отклонение

print(f"среднее квадратичное отклонение: квадратный корень из {ss/20-1} = 31.624607341019814")