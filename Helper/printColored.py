from termcolor import colored


class PrintColored:
    def __init__(self, text):
        self.text = text

    def success(self):
        print(colored(self.text, 'green'))

    def warning(self):
        print(colored(self.text, 'yellow'))

    def failed(self):
        print(colored(self.text, 'red'))

    def waiting(self):
        print(colored(self.text, 'blue'))
