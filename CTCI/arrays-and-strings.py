# Arrays and strings problems work through
'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

def isUnique(str) :
  isPresent = [False] * 128

  for i in str :
    if (isPresent[ord(i)] == True) : # this ord() is important!!
      return False
    else :
      isPresent[ord(i)] = True
  return True

print(isUnique("hello"))
print(isUnique("cat"))

'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

def checkPermutation(str1, str2) :
  if (len(str1) != len(str2)) :
    return False
  
  str1 = sorted(str1)
  str2 = sorted(str2)

  if (str1 != str2) :
    return False
  
  return True

print(checkPermutation("hello", "hewwo"))
print(checkPermutation("", ""))

'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
", 13
Input: "Mr John Smith
Output: "Mr%20John%20Smith"
'''
def URLify(str) :
  modified = ""
  for i in str :
    if (i == " ") :
      modified += "%20"
    else :
      modified += i
  
  return modified

print(URLify("Mr John Smith"))

'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is an arrangement of letters.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
'''
def isPalindromePerm(str) :
  if (len(str) == 0) :
    return True
  
  str = str.replace(" ", "").lower()
  chardict = {}

  for i in str :
    if i in chardict :
      chardict[i] += 1
    else :
      chardict[i] = 1
  
  countOddOccurrences = 0

  for key in chardict :
    if (chardict[key] % 2 == 1) :
      countOddOccurrences += 1
  
  if (countOddOccurrences > 1) :
    return False
  return True

print(isPalindromePerm("Tact Coa"))

'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''
def isOneAway(str1, str2) :
    if (abs(len(str1) - len(str2)) > 1) :
        return False
    
    str1chars = {}
    str2chars = {}

    for i in str1 :
        if i in str1chars :
            str1chars[i] += 1
        else :
            str1chars[i] = 1

    for j in str2 :
        if j in str2chars :
            str2chars[j] += 1
        else :
            str2chars[j] = 1
    
    countDiff = 0
    for key in str1chars :
        if key in str2chars :
            if (abs(str1chars[key] - str2chars[key]) == 1) :
                countDiff += 1
        else :
            countDiff += 1
    
    if (countDiff > 1) :
        return False
    
    return True

print(isOneAway("pales", "pale"))
print(isOneAway("pale", "bale"))
print(isOneAway("pale", "pal"))
print(isOneAway("pale", "bake"))
print(isOneAway("hello", "it's me"))

'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def compressStr(str1) :
    newStr = ""
    lens = len(str1)

    i = 0
    currCount = 1

    while i < lens :
        newStr += str1[i]
        for j in range(i + 1 , lens, 1) :
            if (str1[j] == str1[i]) :
                currCount += 1
            else :
                break
        
        newStr += str(currCount)
        i += currCount
        currCount = 1
    
    if (len(newStr) > len(str1)) :
        return str1
    else :
        return newStr

print(compressStr("aabcccccaaa"))
print(compressStr("friends romans countrymen"))
        

