# вычисляем свободные сотки садового участка

#Запарашиваем площадь участка в стоках
s_place=float(input()) #s_place - площадь участка в сотках

lenght=25 # длина грядки в метрах
width=15 # ширина грядки в метрах

s_rest=int((s_place*100)%(lenght*width))  
	
    
print(s_rest)
    
