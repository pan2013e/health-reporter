class Logger:
    def __init__(self) -> None:
        self.content : str = ''

    def writeln(self, txt):
        print(txt)
        self.content += '{}'.format(txt) + '\n'

    def println(self):
        print(self.content)
    
    def console(self, txt):
        print(txt)

    def __str__(self) -> str:
        return self.content