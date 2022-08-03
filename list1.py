

# Implementing append method
list1=[1,2,1,4,5,6]
def purge_organize(l):
    list2=[0]*6
    index=0
    for i in l:
        if i not in list2:
            list2[index]=i
        else:
            list2[index]=i 
        index=1+index
    return list2
result=purge_organize(list1)
print(result,len(result))
              