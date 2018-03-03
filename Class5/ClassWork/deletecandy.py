# This program allows the user to delete
# a record in the candy.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the coffee to delete.
    search = raw_input('Which candy do you want to delete? ')
    
    # Open the original candy.txt file.
    candy_file = open('candy.txt', 'r')

    # Open the temporary file to write
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    descr = candy_file.readline()

    # Read the rest of the file.
    while descr:
        # Read the quantity field.
        qty = float(candy_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = candy_file.readline()

    # Close the candy file and the temporary file.
    candy_file.close()
    candy_file.close()

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


