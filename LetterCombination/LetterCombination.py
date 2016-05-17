#简单的递归，怎么习惯怎么写最好了，不过把输入改为lit+j挺好的
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps={'0':' ','1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        outs=[]
        if digits=='':
            return []
        lit=''
        def outputs(digits,i,lit):
            if i==len(digits):
                outs.append(lit)
            else:
                for j in maps[digits[i]]:
                    outputs(digits,i+1,lit+j)
        outputs(digits,0,lit)
        return outs
