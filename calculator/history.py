class History:
    def __init__(self, history_file="history.txt"):
        self.history_file = history_file
        self.history = []
        self.load_history()

    def add_to_history(self, expression: str):
        self.history.append(expression)
        with open(self.history_file, 'a') as file:
            file.write(expression + "\n")

    def load_history(self):
        try:
            with open(self.history_file, 'r') as file:
                self.history = [line.strip() for line in file]
        except FileNotFoundError:
            pass

    def clear_history(self):
        self.history = []
        with open(self.history_file, 'w'):
            pass

    def get_history(self):
        return self.history
