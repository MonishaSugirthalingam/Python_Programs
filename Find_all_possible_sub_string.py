"""
INPUT:
MONISHA
OUPUT:
M
MO
MON
MONI
MONIS
MONISH
MONISHA
O
ON
ONI
ONIS
ONISH
ONISHA
N
NI
NIS
NISH
NISHA
I
IS
ISH
ISHA
S
SH
SHA
H
HA
A
"""
#to print all possible substrings from given string
s=input("Enter the string : ")
def tofindsubstring(s):
    for i in range(len(s)+1):
        for j in range(i,len(s)+1):
            print(s[i:j])
tofindsubstring(s)

