# -*- coding: utf-8 -*-
#注意出递归条件，k==1和len(nums1)==0,k/2会最后变为1.
#每次可以排除的部分是小于的部分
class Solution:
    def findKthSortArray(self,nums1,nums2,k):
        m=len(nums1)
        n=len(nums2)
        if m>n:
            nums1,nums2=nums2,nums1
        if len(nums1)==0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        pa=min(len(nums1),k/2)
        pb=k-pa
        if nums1[pa-1]>nums2[pb-1]:
            return self.findKthSortArray(nums1,nums2[pb:],k-pb)
        elif nums1[pa-1]<nums2[pb-1]:
            return self.findKthSortArray(nums1[pa:],nums2,k-pa)
        else:
            return nums1[pa-1]

    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1)+len(nums2))%2==1:
            return self.findKthSortArray(nums1,nums2,(len(nums1)+len(nums2))/2+1)
        else :
            return (self.findKthSortArray(nums1,nums2,(len(nums1)+len(nums2))/2)+
            self.findKthSortArray(nums1,nums2,(len(nums1)+len(nums2))/2+1))/2.0
