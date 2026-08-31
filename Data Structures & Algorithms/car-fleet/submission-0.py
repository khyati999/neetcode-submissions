class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(list(zip(position,speed)))
        for p, s in cars:
            time = (target - p) / s
            while stack and time >= stack[-1][-1]:
                stack.pop()
            stack.append([p, s, time])
        return len(stack)
