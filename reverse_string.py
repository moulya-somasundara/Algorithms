#Write a function that reverses a string. The input string is given as an array of characters char[].

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

#You may assume all the characters consist of printable ascii characters.

def reverse_string(self, s):
    left_index = 0
    right_index = len(s)-1
    while left_index < right_index:
        s[left_index], s[right_index] = s[right_index], s[left_index]
        left_index += 1
        right_index -= 1

#Time Complexity = o(n)
#Space Complexity = o(1)