class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites :
            graph[course].append(prereq )

        WHITE, GRAY, BLACK = 0,1,2
        color = [WHITE]*numCourses

        def has_cycle(course):
            if color[course] == GRAY:
                return True

            if color[course] == BLACK:
                return False

            color[course] = GRAY

            for prereq in graph[course]:
                if has_cycle(prereq): return True
            
            color[course] = BLACK

            return False




        
        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True

        