"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dict = {}
        for emp in employees:
            emp_dict[emp.id] = emp

        def dfs(curr_id):
            worker = emp_dict[curr_id]

            total = worker.importance

            for sub_id in worker.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)
