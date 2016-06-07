#ok[i] tells whether s[:i] can be built
def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
    #这个any用的服，只要有一个存在，就为True
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]
