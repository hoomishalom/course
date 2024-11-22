
# string manipulation

def string_slicing():
    a = "STRING"
    print("1. Letter Number 0 (in python we start counting from 0 - S) = " + a[0])                             # var_name[*letter_number*]
    print("\n2. Letter Number -1 (-1 in string slicing means the last letter - G) = " + a[-1])
    print("\n3. Get A Sequence Of Letters From A String (letters 0-3 excluding 3 - STR) = " + a[0:3])              # var_name[*starting*:*ending*] excluding the 3 letter
    print("\n4. You Can Also Get A Sequence Of Letters With A Jumping Interval (Letters 0,2,4 - SRN) = " + a[::2]) # var_name[*starting*:*ending*:*jump_interval*] 
    print("\n5. In Addition You Can Do A Reversed Jumping Interval (Letters -1,-3,-5 - GIT) = " + a[::-2])         # var_name[*starting*:*ending*:*jump_interval*] 
    print("\n6. Useful Thing To Do With With String Slicing Is To Reverse The String - GNIRTS = " + a[::-1])          # var_name[::-1] to reverse a string 

# string_slicing()

