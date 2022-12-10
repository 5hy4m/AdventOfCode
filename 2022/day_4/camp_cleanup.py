def solution(input):
    pairs = input.split("\n")
    full_overlap_count = 0
    overlap_count = 0
    for pair in pairs:
        a = pair.split(",")[0]
        b = pair.split(",")[1]
        if is_full_overlap(a, b):
            full_overlap_count += 1

        if is_overlap(a, b):
            overlap_count += 1

    return full_overlap_count, overlap_count


def is_overlap(a, b):
    a_start = int(a.split("-")[0])
    a_end = int(a.split("-")[1])
    b_start = int(b.split("-")[0])
    b_end = int(b.split("-")[1])
    return (
        False
        if ((a_start > b_end and a_end > b_end) or (a_end < b_start and a_end < b_end))
        else True
    )


def is_full_overlap(a, b):
    a_start = int(a.split("-")[0])
    a_end = int(a.split("-")[1])
    b_start = int(b.split("-")[0])
    b_end = int(b.split("-")[1])
    return (
        True
        if (a_start <= b_start and a_end >= b_end)
        or (b_start <= a_start and b_end >= a_end)
        else False
    )
