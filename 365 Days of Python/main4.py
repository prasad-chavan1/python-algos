'''
Problem
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.
'''
string = input()
op_str = ''
for i in range(0, len(string)):
    op_str += string[i].upper() if string[i].islower() else string[i].lower()
print(op_str)  
