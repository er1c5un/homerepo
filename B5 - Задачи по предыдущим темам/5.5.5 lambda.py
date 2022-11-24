a = ["asd", "bbd", "ddfa", "mcsa"]

print(*list(map(len, a)))
print(*list(map(lambda x: len(x), a)))

