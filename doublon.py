

array =[1, 1, 2, 4, 5, 7, 9,  9]
dub=[]
z=0
for i in range(len(array)):
    y= array[i]
    #print(y)
    double = array.count(y)
    #print(double)
    if (double > 1 )and ((y in dub) != True):
        z+= 1
        dub.append(y)
#print(dub)
print(z)

