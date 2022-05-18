
def binarySearch(arr, x):
    l=0
    r=len(arr)-1
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Checar si el elemento se encuentra en el medio
        if arr[mid]['item_id'] == x:
            return arr[mid]
 
        # Si el elemento se encuentra en la segunda mitad, ignorar la primera mitad
        elif arr[mid]['item_id'] < x:
            l = mid + 1
 
        # Si el elemento se encuentra en la primera mitad, ignorar la segunda mitad
        else:
            r = mid - 1
 