from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    queue = deque([(0, 0)])  # (current amount, number of coins used)
    visited = set([0])

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            new_amount = current_amount + coin

            if new_amount == total:
                return num_coins + 1

            if new_amount < total and new_amount not in visited:
                queue.append((new_amount, num_coins + 1))
                visited.add(new_amount)

    return -1
