def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    k=n
    if k>=0:
        for i in range(n):
            if k>=0:
                b=1
                while(b<=i):
                    print(" ",end='')
                    b=b+1
                j=1
                while(j<=k):
                    print("*",end='')
                    j=j+1
                k=k-2
                print()
            else:
                break
row=int(input("Enter no. of rows in Inverted Pyramid;\n"))
generate_inverted_pyramid(row)
