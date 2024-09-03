# LeetCode for TikTok 21
# by F.C. Vogel
# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/


def mergeTwoLists(list1, list2):
    out = []
    i = 0
    while True :
        if len(list1) > i:
            out.append(list1[i])
        if len(list2) > i:
            out.append(list2[i])
        if len(list1) <= i and len(list2) <= i:
            break
        i+=1
    
    return sorted(out)

if __name__ == '__main__':
    list1 = [1,2,4]
    list2 = [1,3,4]
    
    print(mergeTwoLists(list1,list2))
    