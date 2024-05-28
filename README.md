Imię i nazwisko - Mateusz Orłowski

Numer indeksu - s26110

DOKUMENTACJA KALKULATORA

OPIS PROJEKTU

Projekt kalkulatora to interaktywna aplikacja, która umożliwia użytkownikom wygodne wykonywanie różnorodnych operacji matematycznych za pomocą prostego,
ale funkcjonalnego interfejsu graficznego. Projekt ten ma na celu dostarczenie narzędzia, które będzie użyteczne zarówno dla początkujących użytkowników, 
jak i dla tych bardziej zaawansowanych w dziedzinie matematyki. Kalkulator został zaimplementowany w języku Python przy użyciu biblioteki Tkinter.

STRUKTURA PROJEKTU

Projekt składa się z kilku pakietów oraz plików:

  1.	Pakiet ‘calculator’:

  •	calc_operations.py – moduł zawierający definicje podstawowych operacji matematycznych oraz funkcji pomocniczych,
      takich jak podstawowe działania arytmetyczne (dodawanie, odejmowanie, mnożenie oraz dzielenie),
      pierwiastki, potęgi, operacje trygonometryczne (sin, cos, tan, ctg), silnia, logarytm naturalny,
      logarytm o określonej przez użytkownika podstawie, obliczanie zarówno obwodu koła jak i prostokąta,
      obliczanie zarówno funkcji liniowej jak i kwadratowej, wartość bezwzględna, funkcja modulo,
      logarytm dziesiętny oraz zamiana systemu dziesiętnego na binarny, ósemkowy oraz heksadecymalny.
  
  •	calculator.py – moduł definiujący główną klasę ‘Calculator’, która zarządza historią operacji kalkulatora
    
  •	history.py – moduł zawierający klasę ‘History’, która obsługuje zapisywanie historii operacji kalkulatora do pliku tekstowego
    
  2.	Pakiet ‘gui’:

•	calculator_gui.py – moduł odpowiedzialny za interfejs graficzny kalkulatora.
      Zawiera klasy „InputField”, „HistoryPanel”, „ButtonPanel” oraz „CalculatorGUI”, które tworzą elementy interfejsu użytkownika i obsługują ich zachowanie
  
  3.	Plik main.py – plik główny, który jest odpowiedzialny za uruchomienie aplikacji kalkulatora
  
  FUNKCJONALNOŚCI
  
  •	Wykonywanie podstawowych operacji matematycznych: dodawanie, odejmowanie, mnożenie i dzielenie
  
  •	Wykonywanie zaawansowanych operacji matematycznych: obliczanie pierwiastka kwadratowego, potęgi o dowolnym wykładniku, 
      logarytmu naturalnego, logarytmu o określonej przez użytkownika podstawie, logarytmu dziesiętnego
      
  •	Wykonywanie funkcji trygonometrycznych (sin, cos, tg, ctg), silnii, wartości bezwzględnej oraz funkcji modulo
  
  •	Wykonywanie obliczeń na obwód zarówno koła jak i prostokąta
  
  •	Wykonywanie obliczeń na funkcję kwadratową oraz liniową
  
  •	Wykonywanie zamiany systemu dziesiętnego na binarny, ósemkowy oraz heksadecymalny
  
  •	Zapisanie historii operacji kalkulatora do pliku tekstowego
  
  •	Interakcyjny interfejs użytkownika umożliwiający wprowadzanie wyrażeń matematycznych za pomocą przycisków lub klawiatury

OBSŁUGA APLIKACJI
  1.	Uruchomienie aplikacji – aplikację można uruchomić poprzez uruchomienie pliku ‘main.py’.
  2.	Interfejs graficzny – po uruchomieniu aplikacji użytkownikowi pojawi się główne okno kalkulatora z wyświetlaczem oraz przyciskami do wprowadzania operacji.
  3.	Wykonywanie operacji – użytkownik może wykonywać operacje matematyczne, klikając odpowiednie przyciski lub używając klawiatury. Wynik będzie wyświetlany na odpowiednim wyświetlaczu.
  4.	Historia operacji – użytkownik może wyświetlić historię operacji, klikając przycisk ‘Pokaż historię’.
      Historia operacji będzie wyświetlana w osobnym oknie. Historia jest ograniczona do 5 ostatnich operacji, jeśli chodzi o jej wyświetlenie.
  5.	Zamykanie aplikacji – aplikację można zamknąć, klikając przycisk zamknięcia okna lub używając skrótu klawiszowego Alt+F4.

ZALECENIA

  •	Proszę się upewnić, że wprowadzane wyrażenia matematyczne są poprawne, aby uniknąć błędów podczas obliczeń
  
  •	Proszę korzystać z interaktywnego interfejsu graficznego dla lepszej wygody użytkowania

ZAKOŃCZENIE

  Projekt Kalkulatora w Tkinter to nie tylko prosty kalkulator, ale również doskonała okazja do nauki i eksperymentowania z interfejsem graficznym w języku Python. 
  Projekt ten pokazuje, jak można z łatwością tworzyć interaktywne aplikacje przy użyciu biblioteki Tkinter, 
  nawet bez wcześniejszego doświadczenia w programowaniu graficznym. Dzięki modularnej strukturze kodu oraz czytelnej dokumentacji projekt jest łatwy do zrozumienia, 
  rozwijania i dostosowywania do własnych potrzeb.
  Projekt Kalkulatora w Tkinter stanowi doskonałą podstawę do dalszego rozwoju i rozbudowy, na przykład poprzez dodanie nowych funkcji matematycznych, 
  ulepszenie interfejsu graficznego lub rozszerzenie możliwości zarządzania historią operacji.
