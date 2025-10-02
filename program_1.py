# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    miles = kilometers * 0.621372
    #Created by Logan Gibson on 10/1/25
    #The program's name is "Kilometers to Miles Calculator"
    ######################    


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    converted_kilometers = kilometer_conversion(float(input("What is the distance in kilometers?")))
    # Display the miles
    print(f"Your distance is {converted_kilometers} miles.")