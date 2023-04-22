# 2. В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают 
# случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

# Например, для случая ББ БЧЧЧ - это ББ ЧБЧЧ, ББ ЧЧБЧ, ББ ЧЧЧБ. 
# Либо использовать сочетания, которые просто учтут количественный выбор. 

'''
Благоприятные исходы (где 3 мяча белые):	
1 ящик - берем 2 мяча | 2 ящик - берем 4 мяча

1. ББ БЧЧЧ
2. ББ ЧБЧЧ
3. ББ ЧЧБЧ
4. ББ ЧЧЧБ

5. БЧ ББЧЧ
6. БЧ БЧБЧ
7. БЧ БЧЧБ
8. БЧ ЧББЧ
9. БЧ ЧБЧБ
10. БЧ ЧЧББ

11. ЧБ ББЧЧ
12. ЧБ БЧБЧ
13. ЧБ БЧЧБ
14. ЧБ ЧББЧ
15. ЧБ ЧБЧБ
16. ЧБ ЧЧББ

17. ЧЧ БББЧ
18. ЧЧ ЧБББ
19. ЧЧ БЧББ
20. ЧЧ ББЧБ
'''

BB = (5/8*4/7*5/12*7/11*6/10*5/9)+(5/8*4/7*7/12*5/11*6/10*5/9)+(5/8*4/7*7/12*6/11*5/10*5/9)+(5/8*4/7*7/12*6/11*5/10*5/9)
#print(f"Вероятность того, что 3 мяча белые (1 ящик: ББ):{BB}")

YY = (3/8*2/7*5/12*4/11*3/10*7/9)+(3/8*2/7*5/12*7/11*4/10*3/9)+(3/8*2/7*5/12*4/11*7/10*3/9)+(3/8*2/7*7/12*5/11*4/10*3/9)
#print(f"Вероятность того, что 3 мяча белые (1 ящик: ЧЧ):{YY}")

BY = (5/8*3/7*5/12*4/11*7/10*6/9)+(5/8*3/7*5/12*7/11*4/10*6/9)+(5/8*3/7*5/12*7/11*6/10*4/9)+(5/8*3/7*7/12*5/11*4/10*6/9)+(5/8*3/7*7/12*5/11*6/10*4/9)+(5/8*3/7*7/12*6/11*5/10*4/9)
#print(f"Вероятность того, что 3 мяча белые (1 ящик: БЧ):{BY}")

YB = (3/8*5/7*5/12*4/11*7/10*6/9)+(3/8*5/7*5/12*7/11*4/10*6/9)+(3/8*5/7*5/12*7/11*6/10*4/9)+(3/8*5/7*7/12*5/11*4/10*6/9)+(3/8*5/7*7/12*5/11*6/10*4/9)+(3/8*5/7*7/12*6/11*5/10*4/9)
#print(f"Вероятность того, что 3 мяча белые (1 ящик: БЧ):{YB}")

all = BB+YY+BY+YB
print(f"Вероятность того, что 3 мяча белые:{all}")