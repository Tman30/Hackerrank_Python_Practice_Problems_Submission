# -*- coding: utf-8 -*-
import math
AB = float(input())
BC = float(input())
AC = math.sqrt(AB*AB + BC*BC)
CM= AC/2
angleC = math.atan(AB/BC)
BM = math.sqrt(CM*CM+BC*BC - 2*CM*BC*math.cos(angleC))
x = (BM*BM+BC*BC-CM*CM)/(2*BM*BC)
theta = math.acos((BM*BM+BC*BC-CM*CM)/(2*BM*BC))
print(str(int(round(math.degrees(theta)))) + '°')