class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
                # if needle is in haystack return index of occurance,
                # else return -1
        for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                        hay_walker = i
                        for j in range(len(needle)):
                                if (hay_walker == len(haystack)):
                                    return -1
                                if haystack[hay_walker] != needle[j]:
                                        break
                                else:
                                        hay_walker += 1
                                if j == len(needle)-1:
                                        return i
        return -1
                                        

