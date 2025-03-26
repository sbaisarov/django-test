def output_numbers(n):
    for i in range(1, n+1):
        ctr = 0
        while ctr < i:
            print(i, end=" ")
            ctr += 1
            
output_numbers(8)
output_numbers(23)
output_numbers(100)