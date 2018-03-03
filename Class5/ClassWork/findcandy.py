# This program allows the user to search the
# candy.txt file for records matching a
# description.

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = raw_input('Enter a description to search for: ')

    # Open the candy.txt file.
    candy_file = open('candy.txt', 'r')

    # Read the first record's description field.
    descr = candy_file.readline()


    # Read the rest of the file.
    while descr != '' and found == False:
        # Read the quantity field.
        qty = float(candy_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if descr == search:
            # Display the record.
            print 'Description: '+ str(descr)
            print 'Quantity: '+ str(qty)
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = candy_file.readline()

    # Close the file.
    candy_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print 'That item was not found in the file.'

# Call the main function.
main()
