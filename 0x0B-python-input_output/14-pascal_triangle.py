#!/usr/bin/python3
def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return([])
    else:
        tmp = []
        final_list = []
        # Begin to traverse into triangle
        for i in range(n):
            # Initialize List with 1 value = 1
            if i == 0:
                # [1]
                tmp.append(1)
                # [[1]]
                final_list.append(tmp)
            elif i == 1:
                # [1, 1]
                tmp = tmp + [1]
                # [[1]. [1, 1]]
                final_list.append(tmp)
            else:
                # New list to append with tmp
                new = []
                # [1]
                new.append(tmp[0])
                # Traverse into length of tmp
                for h in range(len(tmp) - 1):
                    add = 0
                    # [1] + [1]
                    add = tmp[h] + tmp[h + 1]
                    # [1, 2]
                    new.append(add)
                # [1, 2, 1]
                new.append(tmp[-1])
                # [1] = [1, 2, 1]
                tmp = new
                # [[1], [1, 1], [1, 2, 1]]
                final_list.append(tmp)
    return final_list
