from pathlib import Path
import pytest
from gendiff_tk import gendiff


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_same_length_text():
    file1 = get_path('text1.txt')
    file2 = get_path('text2.txt')
    expected = get_path('expected.txt')

    result = gendiff.gendiff(file1, file2)
    assert open(expected).read() == result


def test_empty():
    file1 = get_path('empty1.txt')
    file2 = get_path('empty2.txt')

    result = gendiff.gendiff(file1, file2)
    assert '' == result


def test_empty_and_pull():
    file1 = get_path('empty1.txt')
    file2 = get_path('text2.txt')
    expected = get_path('expected2.txt')

    result = gendiff.gendiff(file1, file2)
    assert open(expected).read() == result


def test_diff_lengths():
    file1 = get_path('diff_text1.txt')
    file2 = get_path('diff_text2.txt')
    expected = get_path('expected3.txt')

    result = gendiff.gendiff(file1, file2)
    assert open(expected).read() == result
