# ID 93703369

import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_idx = random.randint(0, len(arr)-1)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]

    i = 0
    for j in range(len(arr)-1):
        if compare(arr[j], pivot) < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[-1] = arr[-1], arr[i]

    return quick_sort(arr[:i]) + [arr[i]] + quick_sort(arr[i+1:])


def compare(a, b):
    login_a, tasks_solved_a, penalty_a = a
    login_b, tasks_solved_b, penalty_b = b

    if tasks_solved_a == tasks_solved_b:
        if penalty_a == penalty_b:
            return -1 if login_a < login_b else 1
        return -1 if penalty_a < penalty_b else 1
    return -1 if tasks_solved_a > tasks_solved_b else 1


if __name__ == '__main__':
    n = int(input())
    participants = []
    for _ in range(n):
        login, tasks_solved, penalty = input().split()
        participants.append((login, int(tasks_solved), int(penalty)))

    for login, _, _ in quick_sort(participants):
        print(login)
