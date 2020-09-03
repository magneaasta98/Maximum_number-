length = int(input("Input the length of series: "))
counter = 0
for i in range(1,length +1):
    row = i * 2 * (-1)**(i+1)
    counter += row 
    print(row)
print('Sum: ', counter)