list1=[1,2,1,4,5,6]
def sort_list(l):
    for index,value in enumerate(l):
        if index<len(l)-2 and value>l[index+1] :
            temp=value
            l[index]=l[index+1]
            l[index+1]=temp
    return l

result2=sort_list(list1)
print(result2)