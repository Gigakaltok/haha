single_dim_array = [10, 20, 30, 40, 50]
two_dim_array = [
    [gusion,fanny,ling],
    [clint,miya,layla],
    [khufra,tigreal,atlas]
]

def display_single_dim_array(arr):
    print("single-dimensional array elements: ")
    for element in arr:
        print(element)
        
def display_two_dim_array(arr):
    print("two-dimensional array elements: ")
    for sublist in arr:
        print(sublist)
        
choice = input("which array you want to display? (1 for single , 2 for two-dimensional): ")

if choice == "1": 
    display_single_dim_array(single_dim_array)
elif choice == "2":
    display_two_dim_array(two_dim_array)
else:
    print("error")