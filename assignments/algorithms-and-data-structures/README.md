# 📘 Assignment: Algorithms & Data Structures — Search, Sort, and Complexity

## 🎯 Objective

Implement fundamental algorithms (binary search, merge sort, quicksort) and a simple hash-based map/set, measure their runtime empirically, and write short complexity analyses.

## 📝 Tasks

### 🛠️ Implement core algorithms

#### Description
Implement the following functions in `starter_code.py`:

- `binary_search(arr, target)` — return index or -1
- `merge_sort(arr)` — return a new sorted list
- `quick_sort(arr)` — return a new sorted list
- `SimpleHashMap` — a small hash-backed map class with `set`, `get`, and `delete` methods

#### Requirements
Completed implementations should:

- Handle edge cases: empty inputs, single-element lists, duplicates
- Preserve immutability for the sorting functions (return new lists)
- For `SimpleHashMap`, use open addressing or chaining and support at least basic collision handling

### 🛠️ Benchmark and analyze

#### Description
Create a small benchmark harness that measures runtime of the sorts and binary search across varying input sizes and reports timing results. In `README.md` include a short section summarizing expected time complexity for each algorithm.

#### Requirements

- Provide a script or instructions to run the benchmarks
- Include short written complexity notes (expected time and space complexity)

### 🛠️ Tests

#### Description
Write unit tests that validate correctness of the algorithms on representative inputs.

#### Requirements

- Provide `pytest` tests that run quickly (keep input sizes small)
- Tests should cover edge cases and typical cases

## 📎 Files

- `starter_code.py` — function/class stubs and minimal examples
- `benchmarks.py` — simple timing harness (optional starter)
- `tests/test_algorithms.py` — pytest tests

## 📚 Instructor notes

Recommended time: 3–5 class periods. Students should be encouraged to discuss tradeoffs between algorithms and to present timing tables.
