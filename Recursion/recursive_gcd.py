# find the gcd amoung two numbes 

def gcd(p,q): # q is the smaller number p is the bugger 
    # first 2, 9 was passed
      if q==0:
        return p
      else:
        return (gcd(q,p%q)) #first case 9, 2%9 --> 2

#base case for recursive function 
# divisor reaches one so it is the base case 
p = int(input("Enter first no :"))
q = int(input("Ente 2nd number ; "))
z=gcd(p,q) # 2, 9 
print(z)