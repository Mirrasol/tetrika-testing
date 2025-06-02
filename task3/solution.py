def sort_intervals(intervals: list) -> list:
    """Sort and merge if neccessary timestamps' intervals."""
    sorted_intervals = intervals[:2]

    if len(intervals) > 2:
        for i in range(3, len(intervals) + 1, 2):
            if sorted_intervals[-1] > intervals[i - 1]:
                sorted_intervals[-1] = max(sorted_intervals[-1], intervals[i])
            else:
                sorted_intervals.append(intervals[i - 1])
                sorted_intervals.append(intervals[i])
    
    return sorted_intervals


def get_lesson_appearance(lesson_start: int, lesson_end: int, 
                           intervals: list) -> list:
    """Break a single list of timestamps 
    into a list of time intervals lists,
    within a timeframe of a lesson.
    """
    lesson_intervals = [[
            max(intervals[i - 1], lesson_start),
            min(intervals[i], lesson_end),
        ]
        for i in range(1, len(intervals), 2) 
            if intervals[i - 1] <= lesson_end 
                and intervals[i] >= lesson_start]
    
    return lesson_intervals


def merge_intervals_lists(intervals_1: list, 
                          intervals_2: list) -> list:
    """Find intersections and merge two lists
    of timestamps intervals' lists.
    """
    result = []
    i1 = 0
    i2 = 0

    while i1 < len(intervals_1) and i2 < len(intervals_2):
        start = max(intervals_1[i1][0], intervals_2[i2][0])
        end = min(intervals_1[i1][1], intervals_2[i2][1])
        if start <= end:
            result.append([start, end])
        if intervals_1[i1][1] == end:
            i1 += 1
        if intervals_2[i2][1] == end:
            i2 += 1
    
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    """Find the total shared appearance
    for a pupil and a tutor during a lesson, in seconds.     
    """
    lesson_start = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]

    sorted_pupil_intervals = sort_intervals(intervals['pupil'])
    sorted_tutor_intervals = sort_intervals(intervals['tutor'])

    pupil_lesson_intervals = get_lesson_appearance(lesson_start, lesson_end, 
                                                    sorted_pupil_intervals)
    tutor_lesson_intervals = get_lesson_appearance(lesson_start, lesson_end, 
                                                    sorted_tutor_intervals)

    common_lesson_intervals = merge_intervals_lists(pupil_lesson_intervals, 
                                                    tutor_lesson_intervals)

    result = sum((end - start) for start, end in common_lesson_intervals)
    return result
