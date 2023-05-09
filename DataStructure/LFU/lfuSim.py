
def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0

  data_file = open("linkbench.trc")


  for line in data_file.readlines():
    lpn = line.split()[0]

    # Program here 

    #print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

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