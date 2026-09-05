class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        stack = []
        answer = [0] * n
        for i,t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                past_index = stack.pop()
                answer[past_index] = i - past_index
            stack.append(i)   

        return answer   



        