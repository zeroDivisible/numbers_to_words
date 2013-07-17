#!/usr/local/bin/python

nums = { 1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
         10: "ten",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety" }

teens = { 11: "eleven",
          12: "twelve",
          13: "thirteen",
          14: "fourteen",
          15: "fifteen",
          16: "sixteen",
          17: "seventeen",
          18: "eighteen",
          19: "nineteen" }

bignums = ["quintillion", "quadrillion", "trillion", "billion", "million", "thousand"]

def to_words(number): 
   stack = []
   wordstack = []
   word_num = ""
   while number:
      stack.append(number % 1000)
      number = number / 1000

   while stack:
      num = stack.pop()
      wordstack.append(compute_triple(num))
   wordstack2 = []
   while wordstack:
      wordstack2.append( wordstack.pop() )
      if wordstack:
         wordstack2.append(bignums.pop())
   wordstack2.reverse()
   return " ".join(wordstack2)

def compute_triple(num):
   word_num = ""
   if num / 100:
      word_num += nums[num / 100] + " hundred"
      num = num % 100

   if num in teens or num in nums:
      if word_num is not None:
         word_num += " and "
      try:
         word_num += nums[num]
      except KeyError:
         word_num += teens[num]
      return word_num

   if num / 10:
      if word_num is not None:
         word_num += " and "
      word_num += nums[(num / 10) * 10]
      num = num % 10
   
   if word_num is not None:
      word_num += " " + nums[num]
   return word_num
   
def main():
   tests = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
         30,32,40,43,50,54,60,65,70,76,80,87,90,98,100,101,199,1000,1001,1099,10000,10001,10099,
         100000,100001,1000000,1000001,1000099,1001001,1099001,1010001,101000001,999999999]
   for test in tests:
      print("%s=%s" % (test, to_words(test)))

if __name__ == "__main__":
   main()
