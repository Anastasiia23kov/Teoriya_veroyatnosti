# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, 
# для третьего — 0.6. Найти вероятность того, что выстрел произведен: a). первым спортсменом 
# б). вторым спортсменом в). третьим спортсменом.

# По формуле Байеса: P(B|A) = P(A|B) * P(B) / P(A)
# P(A) = P(A|B1) * P(B1) + P(A|B2) * P(B2) + P(A|B3) * P(B3) = 9/10
#      = 9/10 * 1/3 + 8/10 * 1/3 + 6/10 * 1/3 = 23/30 - вер-ть того, что в мишень попали

# a). первым спортсменом 
# P(B|A) - вер-ть того, что выстрелил 1ый спортсмен, при условии, что в мишень попали.
# P(A|B) = 0,9 - вер-ть того, что в мишень попал 1ый спортсмен.
# P(B) = 1/3 - вер-ть того, что выстрелил 1ый спортсмен
# P(B|A) = P(A|B) * P(B) / P(A)
print(f"Вероятность того, что выстрел произведен: a). первым спортсменом: {float(9/10 * 1/3) / (23/30)}")

# б). вторым спортсменом 
# P(B|A) - вер-ть того, что выстрелил 2ой спортсмен, при условии, что в мишень попали.
# P(A|B) = 0,8 - вер-ть того, что в мишень попал 2ой спортсмен.
# P(B) = 1/3 - вер-ть того, что выстрелил 2ой спортсмен
print(f"Вероятность того, что выстрел произведен: б). вторым спортсменом: {float(8/10 * 1/3) / (23/30)}")

# в). третьим спортсменом.
# P(B|A) - вер-ть того, что выстрелил 3й спортсмен, при условии, что в мишень попали.
# P(A|B) = 0,6 - вер-ть того, что в мишень попал 3й спортсмен.
# P(B) = 1/3 - вер-ть того, что выстрелил 3й спортсмен
print(f"Вероятность того, что выстрел произведен: в). третьим спортсменом: {float(6/10 * 1/3) / (23/30)}")
