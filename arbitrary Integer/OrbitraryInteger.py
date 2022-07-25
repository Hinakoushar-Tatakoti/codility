import random
import math

def solution(n):
    if n>1 & n< (999999999):
        rem = 10-n%10
        return (rem+n)

if _name=='main_':
    sol = solution(10000000)
    print(sol)