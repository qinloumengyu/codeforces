# coding: utf-8
a1, a2, a3, a4 = [int(i) for i in input().split()]
s = input()
print(s.count('1')*a1+s.count('2')*a2+s.count('3')*a3+s.count('4')*a4)
