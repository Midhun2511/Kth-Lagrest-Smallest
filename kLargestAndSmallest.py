import heapq
lis = [5,1,6,4,10,2]
k = 2
print(lis)
kthLargestElement = heapq.nlargest(k,lis)
kthSmallestElement = heapq.nsmallest(k,lis)
print("kthLargestElement is", kthLargestElement)
print("kthSmallestElement is", kthSmallestElement)
