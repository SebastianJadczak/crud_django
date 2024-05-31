**Cel zadania:**

   - Stworzenie prostego serwisu RESTful API do zarządzania listą produktów. Aplikacja powinna umożliwiać dodawanie, edytowanie, usuwanie oraz przeglądanie produktów.

 

**Wymagania funkcjonalne:**

 

**Dodawanie produktu:**
 

   - Użytkownik powinien móc dodać nowy produkt, dostarczając nazwę, opis, cenę oraz ilość dostępnych sztuk.
      
   - Każdy produkt powinien mieć unikalny identyfikator, datę dodania oraz kategorię.

 

**Edytowanie produktu:**
 

   - Użytkownik powinien mieć możliwość edycji istniejącego produktu, zmieniając jego nazwę, opis, cenę, ilość dostępnych sztuk lub kategorię.

 

**Usuwanie produktu:**
 

   - Użytkownik powinien móc usunąć produkt na podstawie jego identyfikatora.

 

**Przeglądanie produktów:**
 

   - Użytkownik powinien móc przeglądać wszystkie produkty.

   - Powinna istnieć opcja filtrowania produktów według kategorii.

   - Dodaj paginację do przeglądania produktów.

 

**Wymagania techniczne:**

      - Użyj frameworka FastAPI lub Django REST framework.

      - Dane powinny być przechowywane w pamięci (np. w słowniku lub w bazie danych SQLite).

      - Zaimplementuj uwierzytelnianie przy użyciu klucza API.
