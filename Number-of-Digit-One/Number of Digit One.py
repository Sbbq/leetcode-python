def numsOfK(self,n,k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m=1
        counts=0
        while(m<=n):
        #m为数位，当这个位大于k时，有(n/m+10-k-1)/10*m多个包含k的数字，当这个位等于k时就加上(n/m%10==k)*(n%m+1)
        #178，求个位上有0-17，18个数，求十位上有1*10个，注意0另外算，70-78个
            counts+=(n/m+10-k-1)/10*m+(n/m%10==k)*(n%m+1)
            m*=10
        return counts
