class Solution:
    def isPalindrome(self, s):
        filtered_list = []
        for i in s:
            if i.isalnum():
                filtered_list.append(i.lower())

        reverse_filtered_list = filtered_list[::-1]

        if reverse_filtered_list == filtered_list:
            return True
        else:
            return False


a = Solution()
a.isPalindrome("A man, a plan, a canal: Panama")