# Prostra strona OpenAI [PL]

## Funkcje

- **Połączenie z API OpenAI**: Aplikacja wysyła artykuł oraz prompt do API OpenAI, aby uzyskać odpowiedź w formie kodu HTML.
- **Dodawanie obrazków**: Użytkownicy mogą wskazać miejsce w artykule, w którym chcą dodać obrazek oraz muszą podać opis alternatywny (alt) do obrazka.
- **Szablon HTML**: Program tworzy pusty szablon HTML, który zostaje dostosowany do finalnego wyglądu strony.
- **Generowanie podglądu**: Generuje podgląd końcowego artykułu z wykorzystaniem pustego szablonu HTML.

## Jak używać

### Wymagania

- **Python 3.x**: Aplikacja działa w wersji Pythona 3.
- **Biblioteka OpenAI**: Należy zainstalować bibliotekę OpenAI, aby aplikacja mogła łączyć się z API.
  
### Instrukcje:

1. **Zainstaluj wymagane biblioteki**:
   Użyj `pip install openai` w terminalu, aby zainstalować bibliotekę OpenAI.

2. **Dodaj klucz API OpenAI**:
   Wprowadź klucz API do zmiennej `api_key` w kodzie.

3. **Uruchom aplikację**:
   Zainstalowane biblioteki i dodanie pliku artykułu (`artykul.txt`) pozwolą na uruchomienie aplikacji poprzez `python app.py`.

4. **Generowanie plików HTML**:
   Aplikacja automatycznie wygeneruje pliki HTML, które można wykorzystać do podglądu artykułu w przeglądarce.
