def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    for i in range(1,n+1):
        if i==1 or i==n:
            for j in range(n):
                print("*",end='')
            print()
        else:
            for k in range(1,n+1):
                if k==1 or k==n:
                    print("*",end='')
                else:
                    print(" ",end='')
            print()

row=int(input("Enter the no. of rows:\n"))
generate_hollow_square(row)
    