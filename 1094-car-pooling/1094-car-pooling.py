class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [trip[2] for trip in trips]
        max_location = max(locations)
        delta = [0]*(max_location + 1)

        for passengers, start, end in trips:
            delta[start] += passengers
            delta[end] -= passengers


        current_pass = 0
        for change in delta:
            current_pass += change
            if current_pass > capacity : return False

        return True
        