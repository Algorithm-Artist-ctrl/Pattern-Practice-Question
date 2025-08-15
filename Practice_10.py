'''' I am using two functions (Practice_06 and Practice_10) to print the Diamond 
    but there is some change in my last function inverted Pyramid as you move forward 
    you will be able understand how i Do it '''
def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    k=1
    i=1
    while(i<=n):
        b=1 #it will count the space
        while(b<=5-i):
            print(" ",end='')
            b+=1
        j=1 # print *
        while(j<=k):
            print("*",end='')
            j+=1
        k=k+2
        print()
        i+=1
def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    k = 2 * n - 3  # start from second last row star count
    i = 1
    while i <= n - 1:
        b = 1
        while b <= i:
            print(" ", end='')
            b += 1
        j = 1
        while j <= k:
            print("*", end='')
            j += 1
        k = k - 2
        print()
        i += 1
row=int(input("Enter no. of rows in Inverted Diamond;\n"))
generate_pyramid(row)
generate_inverted_pyramid(row)

