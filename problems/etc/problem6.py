def sec(s):
    t = s.split(":")
    seconds = int(t[0]) * 60 * 60 + int(t[1]) * 60 + int(t[2])
    return seconds


tickets = 2000
logs = [
    'w request 09:12:29',
    'b request 09:23:11',
    'b leave 09:23:44',
    'ja request 09:33:51',
    'ju request 09:33:56',
    'c request 09:34:02'
]
res = []

for log in logs:
    t = log.split()
    name = t[0]
    action = t[1]
    time = sec(t[2])

    if len(res) == 0:
        if time < sec('09:59:00'):
            res.append((name, action, time))
    else:
        if action == 'request':
            if time > res[-1][2] + 60:
                res.append((name, action, time))
        elif action == 'leave':
            res.pop()

ans = []

for x in res:
    if tickets == 0:
        break

    if x[0] not in ans:
        ans.append(x[0])
        tickets -= 1

ans.sort()
print(ans)
