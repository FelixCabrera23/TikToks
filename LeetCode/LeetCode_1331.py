# LeetCode for TikTok 1331
# by F.C. Vogel
# Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/description/

def arrayRankTransform(arr):
    sor_arr = sorted(set(arr))
    rank ={}
    for i in range(len(sor_arr)):
        rank[sor_arr[i]] = i+1
        
    ans = []
    
    for num in arr:
        ans.append(rank[num])
    return ans

if __name__ == "__main__":
    arr = [37,12,28,9,100,56,80,5,12]
    
    print(arrayRankTransform(arr))
    