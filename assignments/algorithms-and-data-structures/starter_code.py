from typing import List, Optional, Any
import random


def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def merge_sort(arr: List[int]) -> List[int]:
    """Return a new sorted list using merge sort."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: List[int]) -> List[int]:
    """Return a new sorted list using quick sort (randomized pivot)."""
    if len(arr) <= 1:
        return arr[:]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]
    return quick_sort(lows) + pivots + quick_sort(highs)


class SimpleHashMap:
    """A very small hash map using chaining for collisions."""

    def __init__(self, capacity: int = 16):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket_index(self, key: Any) -> int:
        return hash(key) % len(self._buckets)

    def set(self, key: Any, value: Any) -> None:
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key: Any) -> Optional[Any]:
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: Any) -> bool:
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False


if __name__ == "__main__":
    arr = [5, 1, 3, 2, 4]
    print("merge_sort:", merge_sort(arr))
    print("quick_sort:", quick_sort(arr))
    s = sorted(arr)
    print("binary_search 3 ->", binary_search(s, 3))
    m = SimpleHashMap()
    m.set("a", 1)
    print("get a ->", m.get("a"))