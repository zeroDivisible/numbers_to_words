#!/usr/local/bin/python
nums = { 0: "zero",
         1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         14: "fourteen",
         15: "fifteen",
         16: "sixteen",
         17: "seventeen",
         18: "eighteen",
         19: "nineteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety" }

bignums = ["quintillion", "quadrillion", "trillion", "billion", "million", "thousand"]

def to_words(number): 
   stack = []
   wordstack = []
   word_num = ""
   while number:
      stack.append(number % 1000)
      number = number / 1000
   stack.reverse()

   while stack:
      num = stack.pop()
      wordstack.append(describe_triplet(num))

   print(wordstack)
   index = -1
   while wordstack:
      word_num += wordstack.pop()
      if wordstack:
         word_num += " " + bignums[index] + " "
         index -= 1
   return word_num

def describe_triplet(num):
   # 123
   # 120
   h = num / 100
   num = num % 100
   d = num / 10
   r = num % 10

   print ("%s | %s | %s" % (h, d, r))
   word_num = ""

   if h:
      word_num += "%s hundred" % (nums[h],)

   if h and (d or r):
      word_num += " and "

   if 10 < (d * 10 + r) < 20:
      word_num += "%s" % (nums[d * 10 + r],)
   else:
      if d:
         word_num += "%s" % (nums[d * 10],)
      if (h or d):
         word_num += " "
      if r:
         word_num += "%s" % (nums[r],)

   return word_num
   
def main():
   tests = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
         30,32,40,43,50,54,60,65,70,76,80,87,90,98,101,100,199,1000,1001,1099,10000,10001,10099,
         100000,100001,1000000,1000001,1000099,1001001,1099001,1010001,101000001,999999999]
   for test in tests:
      print("%s=%s" % (test, to_words(test)))
      print('\n')

if __name__ == "__main__":
   main()
