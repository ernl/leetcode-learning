class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        haystack_list = list(haystack)
        needle_list = list(needle)
        window_queue = haystack_list[0:len_needle]
        if len_needle == 0 or needle == haystack:
            return 0
        for i in range(1, len_haystack-len_needle+2):
            if window_queue == needle_list:
                return i-1
            else:
                if i+len_needle-1 < len_haystack:
                    window_queue.append(haystack_list[i+len_needle-1])
                    window_queue.pop(0)
        return -1

