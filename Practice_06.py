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
            b+=b
        j=1 # print *
        while(j<=k):
            print("*",end='')
            j+=1
        k=k+2
        print()
        i+=1
row=int(input("Enter no of Rows:\n"))
generate_pyramid(row)
