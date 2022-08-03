# removing duplicate from the list 

list1=[1,2,1,4,5,6]
def duplicate_remove(l):
    list2=[]
    for i in l:
        if i not in list2:
            list2.append(i)
    return list2
result=duplicate_remove(list1)
print(result)



