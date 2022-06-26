import math



q=1789 #random prime number
alpha=2 #primitive root

x=2
for i in range(2,11):
    if(math.gcd((q-1),i)==1):
        x=i  #private key which is a random integer between 2 and q-2
        break






#beta is same as ya

y=pow(alpha,x,q)

#private key is x and public key is q,alpha,y



k=1
for i in range(2,q-1):
    if(math.gcd(q-1,i)==1):
        k=i;
        break



#s1,s2 is similar to y1 and y2
s1=pow(alpha,k,q)
message=11
s2=((message-x*s1)*pow(k,-1,q-1))%(q-1)
if(s2<0):
    s2+=(q-1)

print(s1)
print(s2)


#verification part if v1 and v2 are same then the signature is valid


v1=pow(alpha,message,q)
v2=(pow(y,s1,q)*pow(s1,s2,q))%q

print(v1)
print(v2)