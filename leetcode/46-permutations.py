# Given a collection of distinct integers, return all possible permutations.
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        else:
            first_num = nums[0]
            rest_of_nums = nums[1:]
            permutations_of_rest = self.permute(rest_of_nums)

            answer = []
            for permutation in permutations_of_rest:
                print("permutation: " + str(permutation))
                for index in range(len(rest_of_nums) + 1):
                    perm_to_add = permutation[:index] + [first_num] + permutation[index:]
                    answer.append(perm_to_add)

            return answer

n = [1, 2, 3]

print(Solution().permute(n))
