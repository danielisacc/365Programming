"""
* Developer - Daniel Isacc Delavega

* Date - 03-20-2024

* File Name - Staircase.py

* Description:
    This file contains the function decrypter that takes a file name or file path as
    a parameter and returns either a decrypted message or False. 

    The file supplied is encrypted using the staircase method. 
        (i.e. a file that looks like...
        1,The
        2,Manly
        3,Cat
        4,Dog
        5,Urgent
        6,Lover
        ...is broken into the multi-dimentional array...
        [[The,],[Manly,Cat],[Dog,Urgent,Lover]])

        With each level increasing in size by one. The word selected for decryption is the last in the set

        This example would return "The Cat Lover".

    If the last line in the file is not the last element of a level, i.e if the file was 7 lines rather than
    the six in the previous example, it returns False. 
"""

# Math imported to use the math function sqrt()
import math


def decrypter(file_name: str):
    """
    * Function Developer - Daniel Delavega

    * Date - 03-20-2024

    * Function Name - decrypter

    * Parameter - file_name : String

    * Local Variables:
        word_arr : Array - Stores the words from the lines of the given file
        line_arr: Array -  Stores the contents of each line into an array


        last_in_set: Float - Decievingly stores the staircase level the last line is in...
            If the float is equal to it's Integer coutnerpart, then it is indeed the last
            element within the staircase level. (i.e. 
                If the file has 6 lines, the expression returns 3.0 which is equal to 3,
                but if it is 7 it returns 3.27 which is not equal to 3 or 4.)

        level_index : Integer - Stores the index of the last element of the each level
        decrypted_message : String - Stores the decrypted string of the text file
    """
    with open(file_name, "r") as file:
        # Opens the given file to decrypt
        word_arr = []

        for line in file:
            line_arr = line.strip("\n").split(" ")
            line_arr[0] = int(line_arr[0])
            word_arr.append(line_arr)
        word_arr = sorted(word_arr)  # sorting the values

        last_in_set = (math.sqrt(8 * len(word_arr) + 1) - 1) / 2

        if last_in_set.is_integer():
            level_index = 0
            decrypted_message = ""
            for level in range(1, int(last_in_set)+1):
                # Iterate through steps on the staircase
                level_index += level
                decrypted_message += word_arr[level_index-1][1] + " "
            return decrypted_message
        else:
            return False


print(decrypter("encrypted.txt"))
