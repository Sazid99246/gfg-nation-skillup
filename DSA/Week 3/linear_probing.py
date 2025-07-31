class Solution:
    def linearProbing(self, arr, m):
        result_arr = [-1] * m
        for value in arr:
            index = value % m
            # If it's already placed at correct spot (duplicate), skip
            if result_arr[index] == value:
                continue
            # If the index is empty, insert directly
            elif result_arr[index] == -1:
                result_arr[index] = value
            else:
                # Collision with a different value — linear probing
                start_index = index
                while True:
                    index = (index + 1) % m
                    if result_arr[index] == -1:
                        result_arr[index] = value
                        break
                    elif result_arr[index] == value:
                        # Already inserted as duplicate
                        break
                    elif index == start_index:
                        # We've looped the whole table, no space left
                        break
        return result_arr
