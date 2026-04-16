class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        current1 = 0
        left = 0
        right = len(numbers) - 1
        summ = 0
        answer = []
        while left < right:
            summ = numbers[left] + numbers[right]
            if summ < target:
                left += 1
            elif summ > target:
                right -= 1
            else:
                answer.append(left + 1)
                answer.append(right + 1)
                break
        return answer



        