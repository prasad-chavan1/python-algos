'''
Check if there exist two elements in an array whose sum is equal to the sum of rest of the array.

Difficulty Level: Advance, Because You have try to solve in Time complexity : O(n).
And simple solution it can be of Time complexity :  O(n3).

Explanation

If We have an array of integers and we have to find two such elements in the array such that sum of these two elements is equal to the sum of rest of elements in array.

Examples:

Input  : arr[] = {2, 11, 5, 1, 4, 7}
Output : Elements are 4 and 11
Note that 4 + 11 = 2 + 5 + 1 + 7

Input  : arr[] = {2, 4, 2, 1, 11, 15}
Output : Elements do not exist

'''
arr = [1, 0, 1, 4, 0, -2, 19, -19]
# arr = [5, 4, -5, 11, 15]

def existOrNot(arr):
    for i in range(0, len(arr)):  #for 1st element
        for j in range(0, len(arr)):   #for 2nd element
            if i != j:
                sum = 0
                for k in range(0, len(arr)):  #for calculating sun of remaining elements
                    if(k!=j and k!=i):  #if arr elements equal to elem1 or 2 then pass
                        sum += (arr[k])  #stroing sum
                if(sum == arr[i]+arr[j]):   #sum_of_two = arr[i]+arr[j]
                    return 1
            
print('Sum Exist') if(existOrNot(arr)) else print('Not Exist')

