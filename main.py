import openai


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_html(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def get_user_input_for_images(article):
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

    save_to_html(output_filepath, html_content)
    print(f"Result saved to: {output_filepath}")


if __name__ == "__main__":
    main()
