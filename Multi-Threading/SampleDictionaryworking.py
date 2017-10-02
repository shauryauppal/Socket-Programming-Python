#dictionary item no. ('itemname',price)
d = {'1':('tomato',20),'2':('potato',10),'3':('onion',40),'4':('carrot',10),'5':('apple',45)}
#print dictionry
print(d)
#iterator using key values
for keys in d.keys():
    #method1
    print(d[keys][0],d[keys][1])
    #method2
    name,cost = d[keys]
    print('Keys->',keys,'Grocery -> :',name,'\n','The cost is :',cost)

