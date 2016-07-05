#核心思想，先分块，找到递增的那部分，判断是否在递增部分里面，然后缩小范围
class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left+(right-left)/2
            if nums[mid]==target:
                return True
            if nums[mid]>nums[left]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[right]>=target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                left+=1
        return False
