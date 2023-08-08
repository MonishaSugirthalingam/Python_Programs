"""
AIM     : A program using the function to solve a classic ancient puzzle.
AUTHOR  : MONISHA.S
DATE    : 27-12-2021
"""
def headsAndlegs(m,n):
    x=(legs//2)-heads#number of four legs animals
    print(x)
    y=heads-x #number of two legs animals
    print(y)
heads=int(input())
legs=int(input())
headsAndlegs(heads,legs)
