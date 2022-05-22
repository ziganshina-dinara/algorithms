"""
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число отрезков. Каждая из последующих nn строк содержит по два числазадающих начало и конец отрезка.
Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек несколько, выведите любое из них.
"""
def set_point_cover_segments(list_segment):
    # sort segments by their ends
    list_segment.sort(key=lambda x: x[1])

    # collect points
    set_points = []
    i = 0
    while i < len(list_segment):
        point = list_segment[i][1]
        set_points.append(point)
        while list_segment[i][0] <= point:
            if i == len(list_segment) - 1:
                return set_points
            i += 1


    return set_points


def main():
    n = int(input())
    list_segment = []
    for i in range(n):
        list_segment.append(list(map(int, input().split(' '))))
    points = set_point_cover_segments(list_segment)
    print(str(len(points)) + '\n' + ' '.join(list(map(str, points))))


if __name__ == "__main__":
    main()