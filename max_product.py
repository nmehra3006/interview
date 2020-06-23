#[1,3, 2,4,5]

def max_product(arr):

     zero = 0
     if arr.count(zero) >1:
         return 0


     n = len(arr)
     n_count = 0
     max_prod = 1
     min_least_index = float('inf')
     min_great_index = float('inf')
     min_positive_index = float('inf')


     for i,a in enumerate(arr):

         if a<0:
            

         else:
             min_positive_index = min(min_positive_index, i)


    if n_count == 0:
        skip_index = min_positive_index

    elif n_count % 2 == 0:

        skip_index = min_least_index

    else:
        skip_index = min_great_index

    return  max_prod


print max_product([-1,-2, 2,-4,-5])