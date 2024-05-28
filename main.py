from tkinter import Tk
from gui.calculator_gui import CalculatorGUI

def main():
    """Główna funkcja uruchamiająca aplikację kalkulatora."""
    root = Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
