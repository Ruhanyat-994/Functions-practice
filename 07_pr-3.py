# sum(8)=(1+2+3+4+5+6+7+8) 
#sum(8)= sum(7)+8
# sum(n)=sum(n-1)+8
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
a=sum(100)
print(a)
