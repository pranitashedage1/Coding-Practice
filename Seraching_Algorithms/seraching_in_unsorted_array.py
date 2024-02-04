# Searching in unsorted array -
from typing import Any


def search_unsorted(arr: Any, ele: Any ) -> bool:
    for i in arr:
        if i == ele:
            return True     
    return False

arr1 = [3, 56, 7, 90, 34, 21, 2]
ele1 = 34
print(search_unsorted(arr1, ele1))

