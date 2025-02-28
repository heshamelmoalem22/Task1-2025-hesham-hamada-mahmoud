def insertion_sort(scores):
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key


student_scores = [85, 92, 78, 90, 88, 76, 95, 89]
print("Original scores:", student_scores)


insertion_sort(student_scores)
print("Sorted scores:", student_scores)
