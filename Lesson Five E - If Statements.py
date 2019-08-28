"""
Lesson Five E - If Statements

In this lesson you will learn
how to use if, elif, else statements
"""

#Example 1 - Basic if, then statement
    
    #n = 6
    #if(n > 5):             What this means is that if n > 5 run the indented code
        #print("True")
    #else:                  This is ran if the statement above is false such as if n was equal to 4
        #print("Fale")

#Example 2 - if, elif, else

n = int(input("Type A Value: "))

if(n > 5):             #What this means is that if n > 5 run the indented code
    print("True")
elif(n == 5):           #elif is used when you want another condition to run if the "if" statement is false, you can have as many elif statements as you want
    print("elif")
else:                  #This is ran if all the statements above are false such as if n was equal to 4
    print("False")

#Practice - Write your own
    
