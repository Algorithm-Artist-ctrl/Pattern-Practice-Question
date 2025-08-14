def generate_triangle(n):
    
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    lst=[]
    for i in range(1,n+1):
        lst.append("*"*i)
    return lst
num=int(input("Enter the height and base of the right-angled triangle:\n"))
print(generate_triangle(num))
