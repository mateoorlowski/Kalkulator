from calculator.history import History

class Calculator:
    def __init__(self, history_file="history.txt"):
        self.history = History(history_file)
        try:
            self.history.load_history()
        except Exception as e:
            print(f"Error loading history: {e}")
