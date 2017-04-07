def SmartGrocer(textFile):
    #Open File to be read
    with open(textFile, 'r') as prices:
        #Read and Store the prices
        data = prices.readlines()
        d = {}
        for item in data:
            item = (item.lower()).split()

            name = ' '.join(item[0:-1]) #processes the names

            #processes the prices
            price = item[-1]
            if '¢' in price:
                price = price.replace('¢', '')
                price = float(price)/100
            elif '$' in price:
                price = price.replace('$', '')
            price = float(price)

            #add to dictionary if item/price doesn't exist within dictionary
            if name not in d:
                d[name] = [price]
            else:
                d[name].append(price)

    #User Interface
    while True:
        answer = input("Type 'list' for a list of items, 'print' to output data, <item name> for pricing info, 'quit to quit: \n").lower()
        if answer == 'quit':
            break
        elif answer == 'list':
            print(d.keys())
        elif answer == 'print':
            with open('output.txt', 'w') as outfile:
                for key in d.keys:
                    output = key + ' ' + ' '.join(str( d[key])) + '\n'
                    outfile.write(output)
        elif answer in d.keys():
            print("High: ")
            print(max(d[answer]))
            print("Low: ")
            print(min(d[answer]))
            print("Average: ")
            print(sum(d[answer])/len(d[answer]))

        else:
            print("Incorrect input. Try again")
            
        
SmartGrocer('prices.txt') #Call Program with a txt file as the parameter(which should include the items and prices
