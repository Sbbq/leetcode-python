class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sPtr,pPtr,lastS,lastP=0,0,-1,-1
        while(sPtr<len(s)):
            if pPtr<len(p) and (s[sPtr]==p[pPtr] or p[pPtr]=='?'):
                sPtr+=1
                pPtr+=1
            elif pPtr<len(p) and p[pPtr]=='*':
                lastP=pPtr+1
                pPtr+=1
                lastS=sPtr
            elif lastP!=-1:
                lastS+=1
                sPtr=lastS
                pPtr=lastP
            else :
                return False
        while(pPtr<len(p) and p[pPtr]=='*'):
            pPtr+=1
        return pPtr==len(p)
