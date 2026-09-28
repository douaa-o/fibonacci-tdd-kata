def fibonacci(n, m):
    
    def pisano(m):
        previous, current = 0,1
        for i in range(m*m):
            previous, current = current, (previous + current) % m
            
            if (previous == 0 and current == 1):
                return i+1
        
    pisano_period = pisano(m)

    n = n % pisano_period

    pr, c = 0,1
    if n == 0:
        return 0
    for i in range(n-1):
        pr, c = c, pr + c
    
    return (c % m)