class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {"(": ")", "[": "]", "{": "}"}   #Dictionary; a set of key: value pairs with each being unique.
        stack = []
        for b in s:
            if not stack:               #tests if the list is empty 
                if b not in pair:       #if the character is not in dictionary at all, then return false and end
                    return False
                stack.append(b)
            else:
                if b not in pair and pair[stack[-1]] != b:   
                    return False
                if b == pair[stack[-1]]:
                    print(pair[stack[-1]])
                    stack.pop()    #deletes topmost element of the stack
                    
                else:
                    stack.append(b)  #
        return not stack             #if the stack is empty, so it will return false, return true


test = Solution()
print(test.isValid("[()({})]"))

