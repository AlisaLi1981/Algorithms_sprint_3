# ID 93774488

import random


class Competitor:
    def __init__(self, login: str, tasks_solved: int, penalty: int):
        self.login = login
        self.tasks_solved = tasks_solved
        self.penalty = penalty

    def __lt__(self, other: 'Competitor') -> bool:
        if isinstance(other, Competitor):
            return (
                (-self.tasks_solved, self.penalty, self.login) <=
                (-other.tasks_solved, other.penalty, other.login)
            )

    def __str__(self) -> str:
        return self.login


def quick_sort(arr: list, start: int, end: int) -> None:
    if start >= end:
        return

    pivot_idx = random.randint(start, end)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]

    left = start
    for right in range(start, end):
        if arr[right] < pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    arr[left], arr[end] = arr[end], arr[left]

    quick_sort(arr, start, left-1)
    quick_sort(arr, left+1, end)


if __name__ == '__main__':
    n = int(input())
    participants = []
    for _ in range(n):
        login, tasks_solved, penalty = input().split()
        participants.append(Competitor(login, int(tasks_solved), int(penalty)))

    quick_sort(participants, 0, n-1)

    for competitor in participants:
        print(competitor)
