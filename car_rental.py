print('Welcome to car rentals!')

while True:
    
    y_or_n = input('Would you like to continue (y/n)? ') #ask the user if he wants to continue
    if y_or_n == 'y': #if yes than we calculate the amount billed to the costumer 
        b_or_d = input('Custumer code (b or d): ') #ask the user to tell us what classification code he has
        days = int(input('Number of days: ')) #ask the user to tell us for how many days he rented the car 
        start_od = int(input('Odometer reading at the start: '))
        end_od = int(input('Odometer reading at the end: '))
        miles = end_od - start_od # miles driven calculated
        print('Miles driven: ', miles)

        if b_or_d == 'b': # "budget" classification code 
            amount = 40 * days + 0.25 * miles
            print('Amount due: ', amount)
        else:
            if (miles/days) > 100: # "daily" classification code
                amount = 60 * days + 0.25 * (miles - days *100) #the base charge is 60 and then 0.25$ are added for every mile driven above 100 miles per day 
                print('Amount due: ', amount) # This is the amount for classification code 'd'
            else:
                amount = 60 * days
                print('Amount due: ', amount)
    else:
        break



        
