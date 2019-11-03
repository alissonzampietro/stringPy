class String:
    def __init__(self, string):
        self.string = string

    def group(self):
        old = self.string[0]
        compressedString = ''
        count = 0
        for letter in self.string:
            if letter != old:
                compressedString += old+str(count)
                old = letter
                count = 0
            count += 1
        return compressedString