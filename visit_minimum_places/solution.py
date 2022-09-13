def solution(A):
    trips = {val: 1 for val in set(A)}
    num_trips = len(trips)

    cur_i = result_i = result_j = 0
    for cur_j, num in enumerate(A, 1):
        if trips[num] > 0:
            num_trips -= 1

        trips[num] -= 1

        if not num_trips:
            while cur_i < cur_j and trips[A[cur_i]] < 0:
                trips[A[cur_i]] += 1
                cur_i += 1

            if not result_j or cur_j - cur_i <= result_j - result_i:
                result_i, result_j = cur_i, cur_j
    return result_j - result_i
    