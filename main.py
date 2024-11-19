import openai


def read_file(filepath):
    # Reads the contents of a text file.
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_html(filename, content):
    # Saves a string to an HTML file.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def get_user_input_for_images(article):
    # Allows the user to specify where to insert images into the article.
    images_info = []

    while True:
        add_image = input("Do you want to add an image to the article? (yes/no): ").lower()

        if add_image == "no":
            print("No image will be added. Saving the article without images.")
            break

        if add_image == "yes":
            paragraphs = article.split("\n\n")
            print("\nArticle has been split into the following paragraphs:\n")

            for i, paragraph in enumerate(paragraphs):
                print(f"{i+1}. {paragraph[:100]}...")

            paragraph_choice = int(input("\nEnter the number of the paragraph after which you want to add an image: ")) - 1
            if paragraph_choice < 0 or paragraph_choice >= len(paragraphs):
                print("Invalid choice. Please try again.")
                continue

            image_description = input("Enter a description for the image (to be used in alt and caption): ")

            images_info.append({
                "paragraph": paragraph_choice,
                "description": image_description
            })

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

    return images_info


def process_text(api_key, prompt):
    # Sends a prompt to the OpenAI API and retrieves the generated content.
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


def create_empty_template(output_path):
    # Creates an empty HTML template with basic styling for the article.

    template = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Szablon Artykułu</title>
    <style>
        body {
            font-family: Lato, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f9;
            color: #333;
            padding: 0 5%;
        }
        
        h1, h2, h3, h4 {
            color: #1e90ff;
            text-align: center;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
        
        figure {
            text-align: center;
            margin: 20px 0;
        }
        
        figcaption {
            font-size: 0.9em;
            color: #555;
        }
        
        p {
            margin: 10px 0;
            text-align: justify;
        }
        
        ul, ol {
            margin: 10px 0 10px 20px;
        }
    </style>
</head>
<body>

</body>
</html>"""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(template)
    print(f"Empty template saved to: {output_path}")


def generate_full_preview(template_path, article_path, output_path):
    # Combines an article with an HTML template to create a full preview.

    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    with open(article_path, 'r', encoding='utf-8') as article_file:
        article_content = article_file.read()

    placeholder = "<body>"
    if placeholder in template:
        preview_content = template.replace(
            placeholder, f"<body>\n\n{article_content}"
        )
    else:
        raise ValueError("Placeholder not found in the template!")

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(preview_content)

    print(f"Full preview generated and saved to: {output_path}")


def main():
    api_key = ""
    input_filepath = "artykul.txt"
    article_output_filepath = "artykul.html"
    template_output_filepath = "szablon.html"
    preview_output_filepath = "podglad.html"

    article = read_file(input_filepath)

    images_info = get_user_input_for_images(article)

    prompt = f"""
        Convert the following article into well-structured HTML code. 
        - Use appropriate HTML tags such as <h1>, <h2>, <p>, <ul>, <li>, etc. to organize the content.
        - Add <img> tags where the user has indicated, with the 'src' attribute set to "image_placeholder.jpg" 
          and the 'alt' attribute set to the provided title for each image.
        - Add captions under images using the <figcaption> tag, describing the image context.
        - Ensure the images are contextually relevant to the article, based on the user's input.
        - Return only the HTML content between the <body> and </body> tags, do not include <html>, <head>, or <body> tags.
        - Maintain a clean and readable structure for the HTML document.

        Here is the article to convert:

        {article}

        Images to add:
        {images_info}
        
        Ensure that the images are inserted after the specified paragraphs or sections, as mentioned in the images_info section.
        """

    print("Sending data to the API...")
    html_content = process_text(api_key, prompt)

    save_to_html(article_output_filepath, html_content)
    print(f"Result saved to: {article_output_filepath}")

    create_empty_template(template_output_filepath)

    generate_full_preview(template_output_filepath, article_output_filepath, preview_output_filepath)


if __name__ == "__main__":
    main()
