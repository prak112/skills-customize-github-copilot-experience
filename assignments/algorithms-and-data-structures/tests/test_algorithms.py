import importlib.util
import pathlib
import sys

tests_dir = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("starter_code", tests_dir / ".." / "starter_code.py")
starter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = starter
spec.loader.exec_module(starter)
sc = starter


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5]
    assert sc.binary_search(arr, 3) == 2


def test_binary_search_not_found():
    arr = [1, 2, 4, 5]
    assert sc.binary_search(arr, 3) == -1


def test_merge_sort():
    arr = [3, 1, 2]
    assert sc.merge_sort(arr) == [1, 2, 3]


def test_quick_sort():
    arr = [3, 1, 2]
    assert sc.quick_sort(arr) == [1, 2, 3]


def test_simple_hash_map():
    m = sc.SimpleHashMap()
    assert m.get('x') is None
    m.set('x', 10)
    assert m.get('x') == 10
    assert m.delete('x') is True
    assert m.get('x') is None