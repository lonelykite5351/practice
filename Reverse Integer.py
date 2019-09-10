# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:36:21 2019

@author: lonelykite
"""

# =============================================================================
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21
# =============================================================================

class Solution:
    def reverse(x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        temp=[]
        min = -2**31
        max = 2**31 - 1

        if (x <= min or x > max):
            return(0)
        if x in range(-9,9 + 1):
            return(x)
        elif x <= -10:
            x_num = x
            x_str = str(x)
            temp.append(x_str[0])
            x_str = x_str.strip('-')
            x = int(x_str)
        else:
            x_num = x

        while(x != 0):           
            a = x % 10
            temp.append(a)
            if x // 10 == 0:
                if (temp[1] == 0 and x_num < 0):
                    temp.pop(1)
                    while (temp[1] == 0):
                        temp.pop(1)

                while temp[0] == 0:
                    temp.pop(0)
                    if (temp[0] != 0):
                        break
                temp = list(map(str,temp))
                x_reverse = "".join(temp)
                x_reverse = int(x_reverse)
                if (x_reverse <= min or x_reverse > max):
                    return(0)
                else:  
                    return(x_reverse)
            else:
                x = x // 10

    a=1534236469
    
    print(reverse(a))
    print(2**31)
    