from quickSort import *
from mergeSort import *
from quickSort2 import *
from mergeSort2 import *

def do_sort(input_file):

    data_file = open(input_file)
    A = [] # pages
    B = dict() # pages 접근 횟수 세기
    C = [] # page와 접근 횟수 짝지어 저장

    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
        if lpn in B:
            B[lpn] += 1
        else:
            B[lpn] = 1

    for key, value in B.items():
        temp = []
        temp.append(key)
        temp.append(value)
        C.append(temp)

    # -----------기존-----------
    # for i in range(10):
    #     print(A[i], end=' ')
    # print("")

    # quickSort(A, 0, len(A)-1)
    # mergeSort(A, 0, len(A)-1)

    # for i in range(len(A)-1, len(A)-11, -1):
    #     print(A[i], end=" ")
    # print("")
    # -----------기존------------


    # quickSort2(C, 0, len(C)-1)
    mergeSort2(C, 0, len(C)-1)

    for i in range(len(C)-1, len(C)-11, -1):
        print(C[i][0], C[i][1])
    print("")




if __name__ == "__main__":
    do_sort("linkbench_short.trc")