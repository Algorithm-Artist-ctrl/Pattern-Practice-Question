def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    lst=[]
    while(n>0):
        lst.append("*"*n)
        n-=1
    return lst
num=int(input("Enter height and base of inverted right-angled triangle:\n"))
print(generate_inverted_triangle(num))
