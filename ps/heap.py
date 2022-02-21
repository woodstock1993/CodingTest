import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    i = 0
    while(len(scoville) > 1):
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville) * 2))
        i += 1
        if (scoville[0] > K):
            return i
    return -1#
