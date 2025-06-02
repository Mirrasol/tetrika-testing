import pytest

from task3.solution import (
    appearance,
    get_lesson_appearance,
    merge_intervals_lists,
    sort_intervals,
)


def test_sort_intervals_with_merge():
    intervals = [100, 220, 180, 222]
    result = sort_intervals(intervals)
    assert result == [100, 222]


def test_sort_intervals_without_merge():
    intervals = [100, 200, 300, 400, 500, 600]
    result = sort_intervals(intervals)
    assert result == [100, 200, 300, 400, 500, 600]


def test_get_lesson_appearance_with_disconnects():
    intervals = [100, 150, 160, 180, 190, 210]
    result = get_lesson_appearance(155, 200, intervals)
    assert result == [[160, 180], [190, 200]]


def test_get_lesson_appearance_without_disconnects():
    intervals = [100, 170]
    result = get_lesson_appearance(120, 160, intervals)
    assert result == [[120, 160]]


def test_get_lesson_appearance_no_appearance():
    intervals = [100, 110, 210, 220]
    result = get_lesson_appearance(120, 200, intervals)
    assert result == []


def test_merge_intervals_lists_with_intersection():
    intervals1 = [[10, 50], [70, 100]]
    intervals2 = [[20, 30], [60, 90]]
    result = merge_intervals_lists(intervals1, intervals2)
    assert result == [[20, 30], [70, 90]]


def test_merge_intervals_lists_without_intersection():
    intervals1 = [[10, 20], [40, 50]]
    intervals2 = [[25, 30], [55, 60]]
    result = merge_intervals_lists(intervals1, intervals2)
    assert result == []


def test_appearance_case1():
    data = {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390,
                       1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
    result = appearance(data)
    assert result == 3117


def test_appearance_case2():
    data = {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                       1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009,
                       1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480,
                       1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749,
                       1594705148, 1594705149, 1594706463]}
    result = appearance(data)
    assert result == 3577


def test_appearance_case3():
    data = {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}
    result = appearance(data)
    assert result == 3565


def test_appearance_case_no_pupil_appearance():
    data = {'lesson': [1594702800, 1594706400],
             'pupil': [],
             'tutor': [1594700035, 1594700364, 1594702749,
                       1594705148, 1594705149, 1594706463]}
    result = appearance(data)
    assert result == 0


def test_appearance_case_no_teacher_appearance():
    data = {'lesson': [1594702800, 1594706400],
             'pupil': [1594692033, 1594696347],
             'tutor': []}
    result = appearance(data)
    assert result == 0


def test_appearance_case_no_common_appearance():
    data = {'lesson': [100, 600],
             'pupil': [99, 110, 120, 122],
             'tutor': [115, 117, 590, 600]}
    result = appearance(data)
    assert result == 0
