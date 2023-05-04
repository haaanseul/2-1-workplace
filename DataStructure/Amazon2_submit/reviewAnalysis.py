from doublylinkedlist import *

def load_data(dataset: CircularDoublyLinkedList):
    with open('amazon_reviews_us_Jewelry_v1_001.tsv', 'r', encoding='UTF-8') as file:
        next(file)
        for line in file:
            fields = line.split('\t')
            key = fields[12] # key = review_headline
            value = fields[8] # value = helpful_vote 수
            dataset.append(key, value) # 도움되는 리뷰를 모아볼 수 있다


def get_data(dataset: CircularDoublyLinkedList):
    filtered = dataset.filter(CircularDoublyLinkedListFilter())
    print
    for dict_item in filtered:
        for key, value in dict_item.items():
            print("%s(%s)"%(key, value)) # 리뷰 제목(도움되는 리뷰 좋아요 수) 형태로 출력


if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    get_data(dataset)

    