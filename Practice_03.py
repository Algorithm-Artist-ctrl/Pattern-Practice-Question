def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    lst=[]
    if n>=1 and m<=100:
        for i in range(n):
            lst.append("*"*m)
        return lst
    else:
        return None
length=int(input("Enter no of rows:\n"))
breadth=int(input("Enter no of columns\n"))
print(generate_rectangle(length,breadth))