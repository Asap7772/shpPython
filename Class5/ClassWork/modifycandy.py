# This program allows the user to modify the quantity
# in a record in the candy.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = raw_input('Enter a description to search for: ')
    new_qty = float(raw_input('Enter the new quantity: '))
    
    # Open the original file.
    candy_file = open('candy.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    descr = candy_file.readline()

    # Read the rest of the file.
    while descr:
        # Read the quantity field.
        qty = float(candy_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.
        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # Read the next description.
        descr = candy_file.readline()

    # Close the candy file and the temporary file.
    candy_file.close()
    temp_file.close()

    # Delete the original candy.txt file.
    os.remove('candy.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'candy.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print 'The file has been updated.'
    else:
        print 'That item was not found in the file.'

# Call the main function.
main()