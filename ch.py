def string_test(string):
   i = 0
   a = "A" and "Z"
   b = "a" and "z"
   count = 0
   count1 = 0
   while i < len(string):
      if string == a:
        count = count + i
      if string == b:
        count1 = count1 + i
      i = i + 1
print count
print count1

string_test("The quick Brow Fox")
