# Take Principal(p),Period(N)Year,Rate of intrest(R) %p.a.and
P = float(input('Plese enter Principal in INR :'))
N = float(input('Plese enter period in year :'))
R = float(input('plese enter rate of interest %.p.a. :'))
# calculate simple interest
I = (P*N*R)/100
#calculate amount
A=P+I

# Print above results
print(f'Simple Intrest for given values is {I:.2f} INR')
print(f'Amount is {A:.2f} INR')