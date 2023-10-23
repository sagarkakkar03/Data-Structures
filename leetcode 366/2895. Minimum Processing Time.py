class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        max_time = 0
        processorTime.sort()
        n = len(processorTime)
        tasks.sort(reverse = True)
        for i in range(n):
            max_time = max(max_time , processorTime[i] + tasks[i*4])
        return max_time
