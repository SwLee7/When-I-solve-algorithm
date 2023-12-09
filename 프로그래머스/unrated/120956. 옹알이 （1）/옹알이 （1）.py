def solution(babbling):
    ans = 0
    for b in babbling:
        cur = b[:]
        for w in ('aya', 'ye', 'woo', 'ma'):
            if w in b:
                cur = cur.replace(w, ' ')
        if not cur.strip(): 
            ans += 1
    return ans