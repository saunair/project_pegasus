
def merge_array(left, right):
    left_len = len(left)
    right_len = len(right)
    
    soln_array = left_len*right_len*[-1]
    right_indx, left_indx = 0, 0
    
    while(right_indx + left_indx < (right_len+left_len)):
        if (left_indx < left_len and right_indx < right_len):
            if(left[left_indx] <= right[right_indx]):
                soln_array[left_indx + right_indx] = left[left_indx]
                left_indx += 1
            elif(left[left_indx] > right[right_indx]):
                soln_array[left_indx + right_indx] = right[right_indx]
                right_indx += 1
        elif(left_indx == left_len):
            if(right_indx < right_len):
                soln_array[right_indx + left_indx:] = right[right_indx:]
                right_indx = right_len
        elif(right_indx == right_len):
            if(left_indx < left_len):
                soln_array[left_indx + right_indx:] = left[left_indx:]
                left_indx = left_len
    
    return soln_array
merge_array([1, 5], [3, 6])



def merge_sort(input_array):
    if len(input_array)<=1:
        return input_array
    left_array = input_array[:len(input_array)//2]
    right_array = input_array[len(input_array)//2:]
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    return merge_array(left, right)
    

print(merge_sort([3, 5, 10, 345]))
print(merge_sort([1000, 30, 0.5, 10, 345]))
