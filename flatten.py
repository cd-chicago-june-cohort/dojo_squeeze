def flatten(arr, i , newArr):
    if i == len(arr):
        return newArr
    if isinstance(arr[i],tuple):
        flatten(list(arr[i]),0,newArr)
    elif isinstance(arr[i],list):
        #return newArr.append(flatten(arr[i],0,newArr))
        flatten(arr[i],0,newArr)
    else:
        newArr.append(arr[i])
    return flatten(arr,i+1,newArr)

x = [1,[2,3],4,(5,6),[7,8,[10,[11,12],[13,[14]]]]]

print flatten(x,0,[])