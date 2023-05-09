class lpn_freq:
    def __init__(self):
        self.freq = {}

    # freq 더하기
    def add_freq(self, page):
        if page in self.freq:
            self.freq[page] += 1
        else:
            self.freq[page] = 1

    # freq 얻기
    def get_freq(self, page):
        return self.freq.get(page, 0)

    
    # [page, freq] 리스트 만들기
    def get_list(self, page):
        return [page, self.freq[page]]