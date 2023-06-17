'''This program include heapq module with its various methods listed below
1) heapq.heappush(heap,item)
2)heapq.heappop(heap)
3)heapq.heappushpop(heap,item)
4)heapq.replace(heap,item)
5)heapq.heapify(list)
6)heapq.nsmallest(n,heap)
7)heapq.nlargest(n,heap)
'''
import heapq
heap=[2,5,4,7,89,45,23,16,45,79]
# heapq.heappush(heap,1)
# heapq.heappush(heap,20)
# heapq.heappush(heap,2)
# heapq.heappush(heap,100)

heapq.heapify(heap)

heapq.heappop(heap)
heapq.heappop(heap)

#heapq.heappushpop(heap,100)

#heapq.heapreplace(heap,100)

print(heapq.nsmallest(3,heap))
print(heapq.nlargest(3,heap))
print(heap)
