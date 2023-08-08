import cmath
n=input()
m=input()
# Add the complex numbers
c=(complex(n)+complex(m))
#Convert into string
d=str(c);
#Using len() function
print(d [1: len(d)-1])
#Seperate the real and imaginary part
print("Real part is”, int (c. real))
print("Imaginary part is”, int (c. imag))
