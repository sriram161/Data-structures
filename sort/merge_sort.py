def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2
        left_list = list_[:mid]
        right_list = list_[mid:]
        l = merge_sort(left_list)
        r = merge_sort(right_list)
        return merge(l, r)
    return list_
    

def merge(list1, list2):
    merge_list = []
    i=0
    j=0
    l1, l2 = len(list1)-1, len(list2)-1
    while(i+j <= l1+l2):
            if list1[i] < list2[j]:
                    merge_list.append(list1[i])
                    i+=1
            elif list1[i] > list2[j]:
                    merge_list.append(list2[j])
                    j+=1
            else:
                    merge_list.append(list1[i])
                    merge_list.append(list2[j])
                    i+=1
                    j+=1
    while(i <= l1):
            merge_list.append(list1[i])
            i+=1
    while(j <= l2):
            merge_list.append(list2[j])
    return merge_list 


if __name__ == '__main__':
        a = [5, 4, 3, 1, 2]
        b = merge_sort(a)
        print(b)
