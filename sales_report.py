"""Generate sales report showing total melons each salesperson sold."""
# pseudocode

# create an empty list for salespeople
# create an empty list for melons_sold
# open the sales-report text file
# for each line in the text file:
    # strip the line
    # split each line on the | character
    # set the salesperson list to the first line at entries[0]
    # create melons variable and set it to an integer at entries[2]

    # if the salesperson at entries[0] is in the salespeople list:
        # create position varialbe and set it to salespeople at index salesperson
        # increment melons_sold list at position variable by melons variable
    # else:
        # the salesperson isn't in the list, so append the salesperson to salespeople
        # append the melons variable to the melons_sold list

    # loop through the entire length of the salespeople list:
        # print the salesperson and the melons from melons_sold at the same index

# refactored code to make a dictionary instead of two lists to pull info at the same index from each


salespeople_dict = {}

f = open('sales-report.txt')

for line in f:
    
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople_dict:
        salespeople_dict[salesperson] += melons
    else:
        salespeople_dict[salesperson] = melons


for salesperson in salespeople_dict:
    print(f"{salesperson} sold {salespeople_dict[salesperson]} melons")
        
        # f'{salespeople[i]} sold {melons_sold[i]} melons')




