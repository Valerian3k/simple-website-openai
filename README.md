# Prostra Strona OpenAI [PL]

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

1. **Utwórz środowisko wirtualne**:
   - Na Windows:
     ```bash
     python -m venv venv
     ```
   - Na macOS/Linux:
     ```bash
     python3 -m venv venv
     ```

2. **Aktywuj środowisko wirtualne**:
   - Na Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Na macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Zainstaluj wymagane biblioteki**:
   Użyj poniższego polecenia, aby zainstalować wszystkie wymagane zależności:
   ```bash
   pip install -r requirements.txt

4. **Dodaj klucz API OpenAI**:
   Wprowadź klucz API do zmiennej `api_key` w kodzie.

5. **Uruchom aplikację**:
   Zainstalowane biblioteki i dodanie klucza pozwoli na uruchomienie aplikacji.

6. **Generowanie plików HTML**:
   Aplikacja automatycznie wygeneruje pliki HTML, które można wykorzystać do podglądu artykułu w przeglądarce.

<br><br>

# Simple Page OpenAI [EN]

## Features

- **OpenAI API Integration**: The application sends the article and prompt to the OpenAI API to receive a response in the form of HTML code.
- **Adding Images**: Users can specify where they want to add images in the article and provide an alt description for each image.
- **HTML Template**: The program creates an empty HTML template, which is then customized to the final page appearance.
- **Preview Generation**: The application generates a preview of the final article using the empty HTML template.

## How to Use

### Requirements

- **Python 3.x**: The application runs on Python version 3.
- **OpenAI Library**: You need to install the OpenAI library for the application to connect to the API.
  
### Instructions:

1. **Create a Virtual Environment**:
   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Libraries**:
   Use the following command to install all required dependencies:
   ```bash
   pip install -r requirements.txt


4. **Add OpenAI API Key**:
   Enter your OpenAI API key into the `api_key` variable in the code.

5. **Run the Application**:
   Once the libraries are installed and the API key is added, you can run the application.

6. **Generate HTML Files**:
   The application will automatically generate HTML files that can be used to preview the article in a web browser.

