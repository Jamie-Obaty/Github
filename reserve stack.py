def rev(num):
    stack  = []   # storing reverse elements

    while len(num) >0:
        x = num.pop()
        stack.append(x)
    
    return stack

# Just add new features into my code

arr = [1,2,3,4,5]
arr = [5,4,3,2,1]

print(rev(arr))


