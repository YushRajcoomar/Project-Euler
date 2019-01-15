# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.



def evenfib():
    evensum = 0
    x = 1
    y = 2
    while x <= 4000000:
        if x%2==0:
            evensum += x
        x, y = y, x + y
    return evensum

print(evenfib())

