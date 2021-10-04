class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {"(": ")", "[": "]", "{": "}"}   #Dictionary; a set of key: value pairs with each being unique.
        stack = []
        for b in s:
            if not stack:                           #tests if the list is empty; this will return false
                if b not in pair:                 #if the character is not in dictionary at all, then return false and end
                    return False
                stack.append(b)                      #otherwise add to the stack
            else:
                if b not in pair and pair[stack[-1]] != b:   
                    return False
                if b == pair[stack[-1]]:
                    print(pair[stack[-1]])
                    stack.pop()                  #deletes topmost element of the stack
                    
                else:
                    stack.append(b)  #
        return not stack                            #if the stack is empty, so it will return false, return true


test = Solution()
print(test.isValid("[()({}))]"))

class Solution2:
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {"Fruit": "Apple", "Car": "Tesla", "Ship": "Titanic"}   #Dictionary; a set of key: value pairs with each being unique.
        stack = []
        for b in s:
            if not stack:                           #tests if the list is empty; this will return false
                if b not in pair:                 #if the character is not in dictionary at all, then return false and end
                    return False
                stack.append(b)                      #otherwise add to the stack
            else:
                if b not in pair and pair[stack[-1]] != b:   
                    return False
                if b == pair[stack[-1]]:
                    print(pair[stack[-1]])
                    stack.pop()                  #deletes topmost element of the stack
                    
                else:
                    stack.append(b)  #
        return not stack                            #if the stack is empty, so it will return false, return true

test2 = Solution2()
print(test2.isValid2("FruitAppleCarTesla"))