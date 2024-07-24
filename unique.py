def check(num):
    num=a
    rem=0
    s=""
    while(num<=b):
        ld=num%10
        rem=num/10
        s=s+str(ld)
        
        length=len(s)
        num+=1
        while(length>=0):
          if(s[length]==s[length-1]):
             length-=1
          else:
             return num
a=int(input("Enter the initial value "))
b=int(input("Enter the final value "))
result=check(a)            
print("Unique numbers are ")
print(" ",result)
