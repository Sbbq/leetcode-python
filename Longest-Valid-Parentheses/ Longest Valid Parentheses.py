#很典型知道算法都会被边界搞死的问题，算法：每次加入i的索引，当可以消去括号时pop，最后剩下来的就是不符合的，找到最长的不符合的
#很好的加一个边界的算法
def longestValidParentheses(self, s):
#解决了堆栈全消保持0值，和s加人')'保证长度符合要求
         stack, res, s = [0], 0, ')'+s
         for i in xrange(1, len(s)):
             if s[i] == ')' and s[stack[-1]] == '(':
                 stack.pop()
                 res = max(res, i - stack[-1])
             else:
                 stack.append(i)
         return res
