from collections import deque
# deque provides you with a double ended queue
# which means that you can append and delete elements from either side of the queue

q = deque(range(5))
print q  # deque([0, 1, 2, 3, 4])

q.append(5)
q.appendleft(6)

print q  # deque([6, 0, 1, 2, 3, 4, 5])

print q.pop()
print q  # deque([6, 0, 1, 2, 3, 4])

q.rotate(3)
print q  # deque([2, 3, 4, 6, 0, 1])

q.rotate(-1)
print q  # deque([3, 4, 6, 0, 1, 2])
