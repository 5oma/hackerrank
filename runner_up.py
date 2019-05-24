
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list_scores = list(arr)
list_scores.sort()
max_score = list_scores[-1]
list_scores.pop(-1)

counter = 0

while counter < 10: 
    if list_scores[-1] < max_score:
        print(list_scores[-1])
        break
    if list_scores[-1] == max_score:
        list_scores.pop(-1)
    counter += 1


