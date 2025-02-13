# Menghapus satu persatu integer dalam array
nums = list(map(int, input().split()))
ls = []
for i in nums:
    ls.append(i)
print(ls)
for i in nums:
    ls.remove(i)
    print(ls)
