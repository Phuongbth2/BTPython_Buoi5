#Sorting - Sắp xếp điểm thi
#Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:
#m1 = midterm1
#m2 = midterm2
#e = endterm
#Cho một list gồm danh sách điểm thi của sinh viên 1 lớp.
# Viết chương trình Python để sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple (sắp xếp theo điểm cuối kỳ - endterm tăng dần).
#vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)]

def sort_list_last(list_point):
    list_sorted = sorted (list_point, key=lambda sort:sort[-1])
    return list_sorted
Point = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
print("Điểm thi sắp xếp theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple: ", sort_list_last(Point))