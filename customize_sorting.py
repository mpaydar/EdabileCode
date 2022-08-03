user_list=[(1,2),(3,3),(1,1)]

def get_element(tuple):
    return tuple[1]

def customize_ordering(my_list):
    my_list.sort(key=get_element)
    print(my_list)
customize_ordering(user_list)