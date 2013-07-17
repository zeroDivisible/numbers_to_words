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
   print(to_words(123456789))

if __name__ == "__main__":
   main()
