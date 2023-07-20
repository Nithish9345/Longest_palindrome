class Palindrome:

    def Longest_Palindromic_Substring(self, string):
        while True:
            if string == string[::-1]:
                return string
            else:
                string = string[1:]


object = Palindrome()
x=input()
print(object.Longest_Palindromic_Substring(x))
