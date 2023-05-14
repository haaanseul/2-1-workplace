from lpn_frequency import *
from heap import *

def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0

  data_file = open("linkbench.trc")

  lfu_freq = lpn_freq()
  lfu_heap = Heap()
  
  # 리스트에 힙에 있는 원소  페이지 저장
  page_in_heap = set()

  for line in data_file.readlines():
    lpn = line.split()[0]

    lfu_freq.add_freq(lpn) # 빈도수 더하기
    tot_cnt += 1

    if lpn in page_in_heap: # 이미 힙에 있는 경우
      lfu_heap.plus_freq(lpn)
      cache_hit += 1

    else:
        if (lfu_heap.size() == cache_slots):
          page_in_heap.remove(lfu_heap.min()[0])

          lfu_heap.deleteMin()
          
        if (lfu_heap.size() < cache_slots):      
          lfu_heap.insert(lfu_freq.get_list(lpn)) # 리스트를 힙에 삽입
          page_in_heap.add(lpn)

  # Program here
  print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)