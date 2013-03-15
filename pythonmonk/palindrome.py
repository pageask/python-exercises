class CustomString(str):

    def palindrome(self):
        no_space_lower = "".join(self.split()).lower()
        return no_space_lower == no_space_lower[::-1]
