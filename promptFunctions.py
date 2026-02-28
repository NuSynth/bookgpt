import os
import re
from openai import OpenAI
from google import genai
from google.genai import types # Required for Advanced Config


# Replace 'YOUR_API_KEY' with your actual key
#For google Gemini
client_gemini = genai.Client(api_key="YOUR_API_KEY_HERE")

#For ChatGPT
client_gpt = OpenAI(
  api_key = "YOUR_API_KEY_HERE",
)





#openai.api_key = os.getenv('OPENAI_API_KEY')  # Assume you set this environment variable


# Generates the name of the book
def name_book(design_author, category_variable):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Generate a very breif title for a book in the style of {design_author}. It is a {category_variable} book."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        book_name = response.output_text
        return book_name.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def custom_name_book(custom_text_input, design_author, category_variable):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Make a very breif title for a book in the style of {design_author}. The book should use this for the idea: {custom_text_input}. It is a {category_variable} book."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        book_name = response.output_text
        return book_name.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Generates the main plot of the book
def book_plot(design_author, category_variable, book_name):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Make a main plot for a book written in the style of {design_author}. It is a {category_variable} book. The title of the book is {book_name}."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        book_plot = response.output_text
        return book_plot.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def custom_book_plot(custom_text_input, design_author, category_variable, book_name):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Make a main plot for a book written in the style of {design_author}. The book should use this for the idea: {custom_text_input}. It is a {category_variable} book. The title of the book is {book_name}"}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        book_plot = response.output_text
        return book_plot.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def characters_in_book(book_plot):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            #{"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nI need a couple of protagonists and supporting characters, along with their descriptions, for a book with that plot. Make an antagonist for the book as well, if it would be good to have one for a book with that plot. The book has 12 chapters, so don't do too many protagonists."}
            {"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nI need a couple of protagonists and supporting characters, along with their descriptions and inventories, for a book with that plot. Make an antagonist with an inventory for the book as well, if it would be good to have one for a book with that plot. The book has 12 chapters, so don't do too many protagonists."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        characters = response.output_text
        return characters.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Generates the template of the book
def book_template(characters, design_author, category_variable, book_plot, chapter_quantity):
    try:
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nIt has these characters:\n\n{characters}\n\n\n\nI need a template for this book in the 3 act structure. List {chapter_quantity} chapters within the 3 act structure, and each chapter needs to have a brief plot, along which characters are in the chapters from the list of characters I provided. It is a {category_variable} book. Write it in the style of {design_author}."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        template_var = response.output_text
        return template_var.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



#Write the template to a file so a human can just write the book out.
# Write chapters to files
def write_to_template(design_author, characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, chapter_quantity, template):
    directory = "book"
    if not os.path.exists(directory):
        os.makedirs(directory)

    stars = "*********************************************************"
    template_file = f"Book Category:\n\n{category_variable}\n\n\n{stars}\n\n\nBook Idea Author:\n\n{design_author}\n\n{stars}\n\n\nAuthor Writing Style:\n\n{chapter_author}\n\n{stars}\n\n\nNumber of chapters:\n\n{chapter_quantity}\n\n\n{stars}\n\n\nCustom Text Input:\n\n{custom_text_input}\n\n\n{stars}\n\n\nBook Name:\n\n{book_name}\n\n{stars}\n\n\nBook Plot:\n\n{book_plot}\n\n{stars}\n\n\nCharacters:\n\n{characters}\n\n{stars}\n\n\nBook Template:\n\n{book_template}"
    filename = f"book_template_file.txt"
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
            file.write(template_file)
    
    loop_count = 0
    chapter_number = 1
    chapter_count = chapter_quantity

    while loop_count < chapter_count:
        character_list = chapter_characters(book_template, chapter_number, characters)
        chapter_template = make_chapter_templates(category_variable, book_template, chapter_author, chapter_number, character_list)
        #chapter = "test"

        FALSE = 0
        if template == FALSE:
            chapter_written = write_chapter(chapter_template, chapter_author, chapter_number)
        else:
            chapter_written = "."


        #Template section
        #define template file name based on loop iteration
        template_filename = f"o{chapter_number}.txt"
        template_file_path = os.path.join(directory, template_filename)

        # Write chapter_template to the file
        with open(template_file_path, "w") as file:
            file.write(chapter_template)

        #Written chapter section
        #define chapter file name based on loop iteration
        chapter_filename = f"c{chapter_number}.txt"
        chapter_file_path = os.path.join(directory, chapter_filename)

        # Write chapter_template to the file
        with open(chapter_file_path, "w") as file:
            file.write(chapter_written)
        


        loop_count = loop_count + 1
        chapter_number = chapter_number + 1

#Get characters
def chapter_characters(book_template, chapter_number, characters):
    try:
        #Get characters list
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"{book_template}\n\n I need you to output only the list of characters listed as being in chapter {chapter_number}. It should just be a list. Do not include characters from other chapters. Just output what I told you."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        character_list = response.output_text

        #Get characters information
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Here is a list of characters:\n\n{character_list}\n\nI need you to list those specific characters AND THEIR INFORMATION from this character sheet:\n\n{characters}\n\nDo NOT INCLUDE ANY OTHER CHARACTERS!! Just output what I told you."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        character_list = response.output_text
        
        return character_list.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

# Make chapter summaries for the template
def make_chapter_templates(category_variable, book_template, chapter_author, chapter_number, character_list):
    try:
        # Structure chapter
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"{book_template}\n\n I need an outline of chapter {chapter_number}. It should be written in the style of {chapter_author}, and the category is {category_variable}. Here is the character information for the chapter:\n\n{character_list}\n\nDo not include the other chapters. Just output what I told you."}
        ]
        response = client_gpt.responses.create(
            model="gpt-5.2",
            input = messages
        )
        chapter_summary = response.output_text

        chapter_variable = f"\n\n\nChapter: {chapter_number}\n\nChapter Summary: {chapter_summary}\n\n\n****************************"
        return chapter_variable.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    


def write_chapter(chapter_template, chapter_author, chapter_number):
    try:
        # Prompt construction
        prompt = f"Write a chapter in the style of {chapter_author} based on this outline:\n\n{chapter_template}"

        # API Call using the 2026 'google-genai' SDK
        response = client_gemini.models.generate_content(
            model='gemini-3.1-pro-preview', 
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a professional novelist. You must strictly write in the third-person. Never use first-person narration. Focus on 'showing, not telling.'",
                # The 2026 way to handle "Thinking"
                thinking_config=types.ThinkingConfig(
                    include_thoughts=False, # Set to True if you want to see the AI's internal notes
                    thinking_level=types.ThinkingLevel.HIGH 
                ),
                temperature=1.0
            )
        )
        
        if not response or not response.text:
            return ""

        chapter_written = response.text
        chapter_variable = f"\n\n\nChapter: {chapter_number}\n\nChapter Written:\n\n {chapter_written}\n\n\n****************************"
        return chapter_variable.strip()

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "" # Keep the GUI from crashing
