s="beabeefeab"

if(len(s) == 0 or len(s) == 1):
    print(9)

if(len(s) == 2):
    print(len(s))

unique_s = list(set(s))
#print(unique_s)

two_char_set = []
for i in range(len(unique_s)):
    for j in range(i + 1, len(unique_s)):
        two_char_set.append(unique_s[i] + unique_s[j])

# print(two_char_set)

a = []
for i in range(len(two_char_set)):
    a.append((s.replace(two_char_set[i][0], '').replace(two_char_set[i][1], '')))
# print(a)

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

max = 0
for i in range(len(a)):
    n = list(find(a[i], a[i][0]))
    if(all(n[p] % 2 == 0 for p in range(len(n)))):
        if(len(n) * 2 - 2 == n[len(n) - 1]):
            if(len(n) > max):
                max = len(n)
                # print(n)
                #print(max)
                print(int(n.pop() + 1))
