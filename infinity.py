# -*- coding: utf-8 -*-
""" ZADACHA 2 """
a=[6789, 101]

def asd(a):
	text=str(a)
	z=0
	s=""
	while  text not in s:
		z+=1
		plus=str(z)
		s+=plus
	answer=int(s.index(text)+1)
	print "answer is: %s"%(answer)

	
for i in a:
	print "for number %s"%(i)
	asd(i)