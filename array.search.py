
def search(arr,x):
    for i ,value in enumerate(arr):
        if value==x:
            return i
    return -1

arr=[1,2,3,4,5]
x=3
print(search(arr,x))