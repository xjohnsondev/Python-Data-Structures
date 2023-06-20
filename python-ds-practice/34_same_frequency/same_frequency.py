def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    result_1 = {}
    result_2 = {}
    
    for num in str(num1):
        if num not in result_1:
            result_1[num] = 1
        else:
            result_1[num] += 1
    
    for num in str(num2):
        if num not in result_2:
            result_2[num] = 1
        else:
            result_2[num] += 1

    return result_1 == result_2
