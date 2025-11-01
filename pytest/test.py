r = "aaasaaa"
words = r.split("aa")
print(words)  # Output: ['', '', '1', '']
print(len(words) - 1)  # Output: 2

pref = [0] * (5 + 1)
print(pref)  # Output: [0, 0, 0, 0, 0, 0]
