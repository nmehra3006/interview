def maxSumTwoNoOverlap(A, L, M):
    N = len(A)
    sumMs = []
    for i in range(N - M + 1):
        sumMs.append([(i, i + M), sum(A[i:i + M])])

    sumNs = []
    for i in range(N - L + 1):
        sumNs.append([(i, i + L), sum(A[i:i + L])])

    sumMs.sort(key=lambda x: x[1], reverse=True)
    sumNs.sort(key=lambda x: x[1], reverse=True)

    print sumMs
    print sumNs
    globalSum = 0
    for i in range(len(sumMs)):
        for j in range(len(sumNs)):
            ml, mr = sumMs[i][0]
            nl, nr = sumNs[j][0]

            if mr <= nl or nr <= ml:
                globalSum = max(sumMs[i][1] + sumNs[j][1], globalSum)

    return globalSum


print maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2)