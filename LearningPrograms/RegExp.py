'''
***** REGULAR EXPRESSIONS *****
-> A regular expression is a special sequence of characters that help you to match or 
find other strings or sets of strings using specialized syntex held in pattern
-> The module re provides full support for RE. if any error occurs module raises the exception re.error
Single line match characters pattern : 
1) a, e, x, < - Exactly matches the same character 
2) .(a period) - matches any single character except newline
3) \w - matches a word Character : a letter or a digit or underbar [a-zA-Z0-9_]
4) \W - matches a non-word character
5) \b - boundry between word and non-word
6) \s - matches a single white space character. Space, Newline, tab and return
7) \S - matches a any non-whitespace character
8) \t, \n, \r - Tab, Newline, Return
9) \d - Decimal digit [0-9]
10) ^ - matches start of the string
11) $ - matches end of the string
12) \ - inhibit the specialness of character

Compilation FLAGS :
-> Compilation flags let you modify some aspects of RE works. It has two names under re module 
1. Longname - "IGNORECASE" 2. smallname - "I"

1) ASCII, A = Make several escapes like \w, \s, \b and \d match only on ASCII character.
2) DOTALL, S = Make, match any characters, including newline
3) IGNORECASE, I = make case-insensitive matches
4) LOCALE, L = Do a local-aware match
5) MULTILINE, M = Multi-line matching, affecting ^ and $
6) VERBOSE, X (for extended) -  Enable verbose REs, which can be organized more cleanly and understandably 

Functions :
re.match(pattern, string, flags=0) - match checks the match in the begining of the line
re.search(pattern, String, flags=0) - Search checks the match anywhere in the line

pattern - Pattern of RE to be matched
String - This is the string have to be checked the pattern is available or not
flags - You can use different flags using bitwise OR |

groups() - This method returns all matching sub-groups
group(num=0) - This method returns entire match on the specific group

search and replace :
re.sub(pattern,repl,string,max=0)

Patterns:
^ - Matches begining of a line
$ - Matches end of a line
. - Matches any single char except a new line
[...] - matches any single char inside a squre bracket
[^...] - matches any single char outside a squre bracket
re* - matches 0 or more occurrences of preceding expression
re+ - matches 1 or more occurrences of preceding expressions
re? - matches 0 or 1 occurrence of preceding expressions
re{n) - matches exactly n number of occurrences of preceding expressions
re{n,} - matches n or more occurrences of preceding expressions
re{n,m} - matches atleast n and atmost m occurences of preceding expressions
a|b - matches either a or b
(re) - Groups a regular expressions and remembers matched text
(?imx) - Temporarily toggles on i, m  or x options within a regular expressions. If in parenthesis only that area is affected
(?-imx) - Temporarily toggles off i, m or x options within a regular expressions. If in parenthesis only that area is affected.
(?: re) - Groups regular expressions without remembering matched text
(?imx: re) - Temporarily toggles on i, m or x options within parenthesis
(?-imx: re) - Temporarily toggles off i, m or x options within parenthesis
(?#...) - Comment
(?= re) - Specify position using a pattern. does not have a range
(?! re) - Specify position pattern negation. does not have a range
(?> re) - matches independent pattern without backtracking
\w - Matches a word character
\W - Matches a non-word character
\s - Matches a whitespace. equivalent to [\t\n\r\f]
\S - Matches a nonwhitespace
\d - matches digits. [0-9]
\D - matches nondigits [^0-9]
\A - Matches a begining of a string
\Z - Matches a end of a string. If a newline exists, it match just before a newline
\z - matches a end of string
\G - matches a point where last match finished
\b - matches word boundaries when outside brackets. matches backspace(0x08) when inside bracket
\B - matches nonword boundaries
\n, \t, etc. - matches newline, carriage returns, tabs and etc.
\1...\9 - matches the nth grouped subexpressions
\10 - matches the nth grouped subexpression if it already matched. Otherwise it refers to the octal representation of a char code

 


'''
import re
#Replace of string
phone = "91765-91765 # Phone number"
#Delete python style comments
num = re.sub(r'#.*$',"",phone)
print("Num : ",num)

#Removing all character except number
num1 = re.sub(r'\D',"",phone)
print("Num1 : %s"%num1)

#Match and Search Group
line = "Cats are smarter than a dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line , re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("No match")

searchObj = re.search(r'(.*) are (.*?) .*', line , re.M | re.I)
if matchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("searchObj.groups() : ", searchObj.groups())
else:
    print("No match")

#Differend b/w match and search
matchObj1 = re.match(r'dogs', line, re.M|re.I)
if matchObj1:
    print("matchObj1.group() : ", matchObj1.group())
else:
    print("No match")

searchObj1 = re.search(r'dogs', line, re.M|re.I)
if searchObj1:
    print("searchObj1.group() : ",searchObj1.group())
else:
    print("No match")