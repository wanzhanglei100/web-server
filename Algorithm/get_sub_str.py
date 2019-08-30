#!/usr/bin/python
import random

class Solution(object):
    def __init__(self, arrayList):
        self.arrayList = arrayList

    # solution type 1
    def get_max_sub_str_1(self):
        maxSum = 0
        startIndex = 0
        endIndex = 0
        itemCount = 0
        for i in range(len(self.arrayList)):
            for j in range(i, len(self.arrayList)):
                tmpSum = 0
                for k in range(i, j + 1):
                    tmpSum += self.arrayList[k]

                if tmpSum > maxSum:
                    maxSum = tmpSum
                    startIndex = i
                    endIndex = k
                    itemCount = k - i + 1

        return maxSum, startIndex, endIndex, itemCount

    def get_max_sub_str_2(self):
        maxSum = 0
        startIndex = 0
        endIndex = 0
        itemCount = 0
        for i in range(len(self.arrayList)):
            tmpSum = 0
            for j in range(i, len(self.arrayList)):
                tmpSum += self.arrayList[j]

                if tmpSum > maxSum:
                    maxSum = tmpSum
                    startIndex = i
                    endIndex = j
                    itemCount = j - i + 1

        return maxSum, startIndex, endIndex, itemCount       

    def get_max_sub_str_3(self):
        maxSum = 0
        tmpSum = 0
        startIndex = 0
        endIndex = 0
        itemCount = 0
        for i in range(len(self.arrayList)):
            tmpSum += self.arrayList[i]
            if tmpSum > maxSum:
                maxSum = tmpSum
                endIndex = i
            elif tmpSum < 0:
                tmpSum = 0
                startIndex = i + 1
            itemCount = endIndex - startIndex + 1

        return maxSum, startIndex, endIndex, itemCount  


if __name__ == '__main__':
    COUNT = 100
    arrayList = [random.randint(-100, 100) for i in range(COUNT) ]
    print (arrayList)
    solution = Solution(arrayList)
    maxSum, startIndex, endIndex, itemCount = solution.get_max_sub_str_1()
    print ('res is:', maxSum, startIndex, endIndex, itemCount)

    maxSum, startIndex, endIndex, itemCount = solution.get_max_sub_str_2()
    print ('res is:', maxSum, startIndex, endIndex, itemCount)

    maxSum, startIndex, endIndex, itemCount = solution.get_max_sub_str_3()
    print ('res is:', maxSum, startIndex, endIndex, itemCount)