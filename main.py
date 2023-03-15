# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    heap=[(0,i) for i in range(n)]
    heapq.heapify(heap)
    
    for i, ti in enumerate(data):
        st_time, thread = heapq.heappop(heap)
        output.append((thread, st_time))
        heapq.heappush(heap,(st_time + ti, thread))

    return output
    
def main():
    n, m=map(int, input().split())
    data=list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread, time in result:
        print(thread,time) 
     
if __name__ == "__main__":
    main()
