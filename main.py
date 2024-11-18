import openai


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_html(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def process_text(api_key, prompt):
    openai.api_key = api_key
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7
    )
    return response.choices[0].message.content


def main():
    api_key = ""
    input_filepath = "artykul.txt"
    output_filepath = "artykul.html"

    article = read_file(input_filepath)

    prompt = f"Convert the following article into well-formatted HTML code:\n\n{article}"

    print("Sending data to the API...")
    html_content = process_text(api_key, prompt)

    save_to_html(output_filepath, html_content)
    print(f"Result saved to: {output_filepath}")


if __name__ == "__main__":
    main()
