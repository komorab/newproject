def fib( x ):
    "to caculate the value of fibonacci sequence"
    if isinstance( x ,int ) & (x > 0):
        if (x == 1) | (x == 2):
            return 1
        elif x>2:
            sum = 0
            firstx = 1
            secondx = 1
            count = 3
            while count <= x:
                sum = firstx + secondx
                secondx = firstx
                firstx = sum
                count += 1
            return sum
    else:
        return 'ValueError'

def fibsum( x ):
    sum = 0
    for i in range( 1, x+1 ):
        sum += fib(i)
    return sum