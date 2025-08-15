def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    b=1
    j=1
    for i in range(1,n+1):
        while(b<=j):
            print(b,end='')
            b=b+1
        j=j+1+i
        print()
rows=int(input("Enter the number of Rows:\n"))
generate_floyds_triangle(rows)