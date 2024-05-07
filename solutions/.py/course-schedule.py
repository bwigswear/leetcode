class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        possible = set()
        prereqs = {}
        for a in prerequisites:
            if a[0] in prereqs:
                prereqs[a[0]].append(a[1])
            else:
                prereqs[a[0]] = [a[1]]
        
        def dfs(visited, course):
            if course in visited:
                return False
            if course in possible:
                for a in visited:
                    possible.add(a)
                return True
            if course not in prereqs:
                possible.add(course)
                for a in visited:
                    possible.add(a)
                return True
            visited.add(course)
            ret = True
            for prereq in prereqs[course]:
                ret = ret and dfs(visited, prereq)
            visited.remove(course)
            return ret
        ret = True
        for course in prereqs:
            ret = ret and dfs(set(), course)
        return ret