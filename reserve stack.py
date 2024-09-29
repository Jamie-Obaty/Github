def rev(num):
    stack  = []

    while len(num) >0:
        x = num.pop()
        stack.append(x)
    
    return stack

arr = [1,2,3,4,5]

rev(arr)


