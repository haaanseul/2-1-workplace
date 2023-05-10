# 

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

    elif lfu_heap.isEmpty():
        page_in_heap.add(lpn)
        lfu_heap.insert(lfu_freq.get_list(lpn)) # 리스트를 힙에 삽입

      # heap에 없는 경우 : min의 freq값이 방금 얻은 lpn의 freq 값보다 작거나 힙이 비어 있으면
      # cache_slots 이상은 최소값 삭제 최소값과 새로운 값도 비교해야됨
    else:
        if (lfu_heap.size() >= cache_slots) and (lfu_heap.min()[1] <= lfu_freq.get_freq(lpn)):
          # cache_hit -= lfu_heap.min()[1] - 1
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


# 개수, 횟수는 lpn_frequency에서 딕셔너리로 관리
# heap에서는 정렬만

# lpn_frequency.py 딕셔너리로 횟수 세고? 세고? 고세? -> 객체로 만들어

# 횟수로 힙에 정렬
# 횟수 같으면 새로운 걸로
# 이미 있으면 cache_hit ++
# 넘치면 삭제

# 비교연산자 쓰기
# 덧셈은 필요가 있나?

# cache_slots은 어떻게 하지?
# 힙 만들때 한계를 어떻게 설정하지