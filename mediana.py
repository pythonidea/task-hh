# -*- coding: utf-8 -*-
""" ZADACHA 1 """
a = [1,2,3,4]
b = [1,4,5,6]
print a
print b

def answer(a,b):
	"""Функция которая объеденяет массивы a и b, сортирует их и выдает результат"""
	e = []
	for i in a:
	    e.append(i)
	for i in b:
		e.append(i)
	e.sort()
	dlina = len(e)
	hay = dlina%2
	if hay == 0:
		mini = ((dlina)/2)-1
		maxi = ((dlina)/2)
		otvet = (e[mini]+e[maxi])/2.0
		print "mediana is: %s"%(otvet)		
	elif hay == 1:
		gde = ((dlina+1)/2)-1
		otvet = e[gde]
		print "mediana is: %s"%(otvet)
	else:
		print "Что-то пошло не так:)"

answer(a,b)