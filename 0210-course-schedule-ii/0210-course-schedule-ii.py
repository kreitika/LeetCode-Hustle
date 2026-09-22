class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graphs = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites :
            graphs[course].append(prereq)

        order = []
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE]*numCourses

        def has_cycle(course):
            if color[course] == GRAY : return True
            if color[course] == BLACK : return False

            color[course] = GRAY

            for prereq in graphs[course]:
                if has_cycle(prereq): return True

            color[course] = BLACK
            order.append(course)

            return False


        for course in range(numCourses):
            if has_cycle(course): return []

        return order
        