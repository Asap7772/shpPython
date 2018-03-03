# This program displays the records in the
# candy.txt file.

def main():
    # Open the inventory file.
    candy_file = open('candy.txt', 'r')

    # Read the first record's description field.
    descr = candy_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(candy_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print 'Description: ' + str(descr)
        print 'Quantity: ' + str(qty)

        # Read the next description.
        descr = candy_file.readline()

    # Close the file.
    candy_file.close()

# Call the main function.
main()
