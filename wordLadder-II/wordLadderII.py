#double-bfs and dfs find path
#the hold target is to find maps
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        #here i use defaultdict to append other values
        maps=collections.defaultdict(list)
        maps[beginWord]=[]
        res=[]
        #print path
        def outputPath(word,path,res):
            if  word==beginWord:
                res+=(path+[word])[::-1],
            else:
                for i in range(len(maps[word])):
                    outputPath(maps[word][i],path+[word],res)
        if beginWord==endWord:
            return [beginWord]
        res=[]
        set1=set([])
        set2=set([])
        set1.add(beginWord)
        set2.add(endWord)
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        direct=True
        flag=False
        while(set1 and not flag):
            if len(set1)>len(set2):
                set1,set2=set2,set1
                direct=not direct
            #清除过去的路径很重要,direct指明方向很重要
            for i in set1:
                wordlist.discard(i)
            for i in set2:
                wordlist.discard(i)
            nextlist=set([])
            #选择少分支的路径，寻找下一个节点
            for word in set1:
                for i in range(len(word)):
                    for j in map(lambda x:chr(x),range(97,123)):
                        temp=word[:i]+j+word[i+1:]
                        if temp in set2:
                            if direct:
                                maps[temp].append(word)
                            else:
                                maps[word].append(temp)
                            flag=True
                        if word[i]!=j and temp in wordlist:
                            nextlist.add(temp)
                            if direct:
                                maps[temp].append(word)
                            else:
                                maps[word].append(temp)
            更新set1输入
            set1=nextlist
        outputPath(endWord,[],res)
        return res
