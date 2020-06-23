#[1,2, 2 , 2, 3,4,5,6,9]
#[2,3,4,7,9]
#[2,3,4]

def intersection_lists(list1, list2):
    intersection = []

    i = 0
    j = 0

    l1 = len(list1)
    l2 = len(list2)

    if l2>l1:
        intersection_lists(list2, list1)

    # percentage to decide when n log m is better than m+n



    while i < len(list1) and j < len(list2):

        if list1[i] == list2[j]:
            intersection.append(list1[i])
            i +=1
            j +=1

        elif list1[i] < list2[j]:
            i +=1

        else:
            j +=1

    return intersection


print intersection_lists([-1,0,1,2,2,2,2,3,3,4,5,6,9], [-1,2,2,3,4,4,7,9])