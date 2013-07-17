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

bignums = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

def to_words(number): 
   stack, wordstack, word_num = [], [], []
   while number:
      stack.append(number % 1000)
      number = number / 1000
   stack.reverse()

   while stack:
      wordstack.append(describe_triplet(stack.pop()))

   while wordstack:
      description = wordstack.pop()
      if len(description) == 0:
         continue

      if wordstack:
         which_bignum = len(wordstack) - 1
         word_num.append(description + " " + bignums[which_bignum])
      else:
         word_num.append(description)

   solution = ""
   while word_num:
      solution += word_num.pop(0)
      if len(word_num) == 1:
         solution += " and "
      else:
         solution += " "

   return solution
   

def describe_triplet(num):
   hundreds = num / 100
   num = num % 100
   tens = num / 10
   reminder = num % 10

   word_num = []

   if hundreds:
      word_num.append("%s hundred" % (nums[hundreds],))
   if num and hundreds:
      word_num.append("and")

   if 10 < (num) < 20:
      word_num.append("%s" % (nums[num],))
   else:
      if tens:
         word_num.append("%s" % (nums[tens * 10],))
      if reminder:
         word_num.append("%s" % (nums[reminder],))
   return " ".join(word_num)
   

def main():
   tests = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
         30,32,40,43,50,54,60,65,70,76,80,87,90,98,101,100,199,1000,1001,1099,10000,10001,10099,
         100000,100001,1000000,1000001,1000099,1001001,1099001,1010001,101000001,999999999]
   for test in tests:
      print("%s=%s" % (test, to_words(test)))

if __name__ == "__main__":
   main()
