count={}
def most_frequent(a):
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key in count:
        print(key,count[key])
b=input("Enter string:")
c=most_frequent(b)
print(c)
            
            
    
        
