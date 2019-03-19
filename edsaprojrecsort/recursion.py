def sum_array(array):

    '''Return sum of all items in array'''
    sum1 = 0
    for item in array:
         sum1 = sum1 + item  # adding every item to sum1
    return sum1  # returning total sum1

def fibonacci(number):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if number <= 1:
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)

def factorial(n):

    '''
    Return n!
    Example :
    n! = 1*2*3*4....n
    '''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''

    picking from last to first index
        Return word in reverse

    '''
    return  word[::-1]
