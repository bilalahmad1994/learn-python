def sequentialsearch(arr,ele):
    position=0
    found=False
    while position<len(arr)and not found:
        if arr[position]==ele:
            found=True
        else:
            position=position+1
    return found
arr=[1,9,24,8,6]
print(sequentialsearch(arr,8))
