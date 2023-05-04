from quickSort import *
from mergeSort import *
from pageSort import *

def do_sort(input_file):

    data_file = open(input_file)
    A = []
    B = dict()

    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
        B[lpn] = 0 

    # for i in range(10):
    #     print(A[i], end=' ')
    # print("")

    # quickSort(A, 0, len(A)-1)
    # mergeSort(A, 0, len(A)-1)

    # for i in range(len(A)-1, len(A)-11, -1):
    #     print(A[i], end=" ")
    # print("")


    # pageSort 부분

    C = pageSort(A, B)

    for i in range(len(C)-1, len(C)-11, -1):
        print(C[i][0], C[i][1], end="\n")
    print("")


if __name__ == "__main__":
    do_sort("linkbench_short.trc")