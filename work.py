import sys
import time

# increase the maximum recursion depth
sys.setrecursionlimit(10000)


def conquer(array: [], tmp: [], left: int, mid: int, right: int) -> int:
    """
    conquer step, collect all result
    :param array: array of integer
    :param tmp: temporary array
    :param left: left index
    :param mid: mid index
    :param right: right index
    :return: number of insertion
    """
    count = 0
    ll = left
    mm = mid
    tt = left

    # until reaching one of 2 ending
    while ll < mid and mm <= right:
        # a[i  < a[j], no rul is broken
        if array[ll] <= array[mm]:
            tmp[tt] = array[ll]
            tt += 1
            ll += 1
            pass
        else:
            # a[i] > a[j]  , j > i
            tmp[tt] = array[mm]
            tt += 1
            mm += 1
            # sum up the
            count += mid - ll
            pass
        pass

    # copy the rest to tmp array
    while ll < mid:
        tmp[tt] = arr[ll]
        tt += 1
        ll += 1
        pass

    # copy the rest to tmp array
    while mm <= right:
        tmp[tt] = arr[mm]
        tt += 1
        mm += 1
        pass

    # copy tmp arry to the array
    ll = left
    while ll <= right:
        array[ll] = tmp[ll]
        ll += 1
        pass

    return count
    pass


def divide(array: [], tmp: [], left: int, right: int) -> int:
    """
    divide array and collect insertion number
    :param array: the array
    :param tmp: the temporary array
    :param left: left index
    :param right: right index
    :return:
    """
    count = 0
    if left < right:
        # get mid index
        mid = int((left + right) / 2)

        # work on left sub array
        count += divide(array, tmp, left, mid)
        # work on right sub array
        count += divide(array, tmp, mid + 1, right)

        # collect the rest of insertion while merging 2 sub arrays
        count += conquer(array, tmp, left, mid + 1, right)
        pass
    return count
    pass


def inversion_count(array: []) -> int:
    """
        count number of inversion
    :param array: the array
    :return:  number of inversion
    """
    # temporary array
    tmp = [None] * len(array)

    # call the function
    return divide(array, tmp, 0, len(array) - 1)
    pass


if __name__ == '__main__':
    # read file line by line
    # then convert each line to an integer
    arr = [int(line.rstrip('\n')) for line in open('IntegerArray.txt')]
    #arr = [2, 4, 1, 3, 5]
    # print result
    start_time = time.time()
    print('inversion count:', inversion_count(arr))
    print("Running time: %s seconds" % (time.time() - start_time))

    #  sorted array is saved in output.txt
    with open('output.txt', 'w') as output:
        for item in arr:
            output.write("%d\n" % item)
        pass

    pass
