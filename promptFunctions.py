# FIXME: Perform Unit testing for ALL FUNCTIONS by: 
# 1. Isolating the function, give it what I know the variables should contain.
# 2. Take the prompt from this, replace the variables with values they need to contain.
# 3. Give prompt to chatGPT in the web interface i pay a monthly fee to use.
# 4. Correct function if output is not what is needed.



# Ensure your OPENAI_API_KEY is set in your environment variables


from openai import OpenAI

client = OpenAI(
  api_key = "YOUR API KEY HERE",
)


import os
import re


#openai.api_key = os.getenv('OPENAI_API_KEY')  # Assume you set this environment variable


# Generates the name of the book
def name_book(design_author, category_variable):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Generate a very breif title for a book in the style of {design_author}. It is a {category_variable} book."}
            ]
        )
        book_name = response.choices[0].message.content
        return book_name.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def custom_name_book(custom_text_input, design_author, category_variable):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Make a very breif title for a book in the style of {design_author}. The book should use this for the idea: {custom_text_input}. It is a {category_variable} book."}
            ]
        )
        book_name = response.choices[0].message.content
        return book_name.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Generates the main plot of the book
def book_plot(design_author, category_variable, book_name):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Make a main plot for a book written in the style of {design_author}. It is a {category_variable} book. The title of the book is {book_name}."}
            ]
        )
        book_plot = response.choices[0].message.content
        return book_plot.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def custom_book_plot(custom_text_input, design_author, category_variable, book_name):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Make a main plot for a book written in the style of {design_author}. The book should use this for the idea: {custom_text_input}. It is a {category_variable} book. The title of the book is {book_name}"}
            ]
        )
        book_plot = response.choices[0].message.content
        return book_plot.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def characters_in_book(book_plot):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                #{"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nI need a couple of protagonists and supporting characters, along with their descriptions, for a book with that plot. Make an antagonist for the book as well, if it would be good to have one for a book with that plot. The book has 12 chapters, so don't do too many protagonists."}
                {"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nI need a couple of protagonists and supporting characters, along with their descriptions and inventories, for a book with that plot. Make an antagonist with an inventory for the book as well, if it would be good to have one for a book with that plot. The book has 12 chapters, so don't do too many protagonists."}
            ]
        )
        characters = response.choices[0].message.content
        return characters.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None




# Generates the template of the book
def book_template(characters, design_author, category_variable, book_plot, chapter_quantity):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Here is a plot of a book I'm making:\n\n{book_plot}\n\n\n\nIt has these characters:\n\n{characters}\n\n\n\nI need a template for this book in the 3 act structure. List {chapter_quantity} chapters within the 3 act structure, and each chapter needs to have a brief plot, along which characters are in the chapters from the list of characters I provided. It is a {category_variable} book. Write it in the style of {design_author}."}
            ]
        )
        template_var = response.choices[0].message.content
        return template_var.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Write chapters to files
def write_to_book(characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, chapter_quantity, check_numchaps):
    directory = "book"
    if not os.path.exists(directory):
        os.makedirs(directory)

    name_plot = f"{book_name}\n\n\n{book_plot}\n\n\n{book_template}"
    filename = f"book_name.txt"
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
            file.write(name_plot)

            
    loop_count = 0
    chapter_number = 1
    chapter_count = chapter_quantity

    while loop_count < chapter_count:
        if not check_numchaps:
            chapter = make_chapter2(characters, category_variable, book_template, chapter_author, chapter_number)
        else:
            chapter = make_custom_chapter(characters, custom_text_input, book_plot, category_variable, book_template, chapter_author, chapter_number)

        #define file name based on loop iteration
        filename = f"{chapter_number}.txt"
        file_path = os.path.join(directory, filename)

        # Write chapter to the file
        with open(file_path, "w") as file:
            file.write(chapter)

        loop_count = loop_count + 1
        chapter_number = chapter_number + 1
        # characters = character_inventories(chapter, characters) need to make this cheaper

# TODO - Modify this so that it keeps a file that it reads and writes to as the chapter is written. Showing the whole chapter at once uses too many tokens. This function will not be used until i do that.
def update_inventories(characters, chapter):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Here is a chapter you wrote: {chapter}\n\n\n\n These are the characters, descriptions, and their inventories, for the book I am writing: {characters}\n\n I need you to output that list of characters and all of their details, but if the inventories of any of the characters in that chapter need to be updated in the list of characters, then I need you to update the inventories in the list of characters."}
            ]
        )
        characters2 = response.choices[0].message.content

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Character Sheet 1:\n{characters}\n\n\nCharacter Sheet 2:\n{characters2}\n\n\nThe inventories in Character Sheet 2 may be different for some characters than in Character Sheet 1 because it might be updated. But if Character Sheet 2 is missing any characters from Character Sheet 1, then I need you to re-write Character Sheet 2 so that it has all characters and their information and inventories."}
            ]
        )
        characters = response.choices[0].message.content
        return characters.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# This might be pretty much doing the same as the function above it. Either way, its costing too many tokens and I had to disable its call. Find a cheaper way to do this.
def character_inventories(chapter, characters):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Here is a chapter that one or more of these characters in a book being made are involved in:\n\n{chapter}\n\n\n\nHere is the character sheet for the whole book:\n\n{characters}\n\nThe characters each have an inventory. If a character in the character sheet gained an item from the part of the chapter I showed you, then output the entire character sheet with the updated inventory of any character that gained an item do the same if an item is no longer in any of the characters inventories. If no item was added to or subtracted from any of the inventories, then simply output the same character sheet that I showed you, with no modifications."}
            ]
        )
        characters = response.choices[0].message.content
        return characters.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Generate chapters for the book - Just keeping this version here until I know the new function works how I want it to.
def make_chapter(characters, category_variable, book_template, chapter_author, chapter_number):
    try:
        # Structure chapter
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n I need chapter {chapter_number} and its plot from the above template divided into three parts, similar to a story arc. It should be written in the style of {chapter_author}, and the category is {category_variable}. Do not include the other chapters. Just output what I told you."}
            ]
        )
        chapter_acts = response.choices[0].message.content

        # Act 1
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n This is for chapter {chapter_number}, from the same chapter from the above template: \n\n{chapter_acts}\n\nHere are the characters in the book along with their inventories, so that you know what the ones used in the chapter have:\n{characters}\n\n\n Write part 1 of chapter {chapter_number} in around 3,000 words. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
            ]
        )
        act_one = response.choices[0].message.content

        # Act 2
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n This is for chapter {chapter_number}, from the same chapter from the above template: \n\n{chapter_acts}\n\nHere are the characters in the book along with their inventories, so that you know what the ones used in the chapter have:\n{characters}\n\n\n Write part 2 of chapter {chapter_number} in around 3,000 words. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
            ]
        )
        act_two = response.choices[0].message.content

        # Act 3
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n This is for chapter {chapter_number}, from the same chapter from the above template: \n\n{chapter_acts}\n\nHere are the characters in the book along with their inventories, so that you know what the ones used in the chapter have:\n{characters}\n\n\n Write part 3 of chapter {chapter_number} in around 3,000 words. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
            ]
        )
        act_three = response.choices[0].message.content

        chapter_variable = f"{act_one}\n\n*********************\n\n{act_two}\n\n*********************\n\n{act_three}"
        return chapter_variable.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Make Chapter 2
def make_chapter2(characters, category_variable, book_template, chapter_author, chapter_number):
    try:


        # Chapter Sumary
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n I need you to output only the sumary of chapter {chapter_number} from the above template."}
            ]
        )
        chapter_summary = response.choices[0].message.content

        # Chapter Characters
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n I need you to output only the characters that are in chapter {chapter_number} from the above template."}
            ]
        )
        chapter_characters = response.choices[0].message.content

        chap_summary_list = paragraph_to_sentences(chapter_summary)
        number_of_sentences = len(chap_summary_list)
        chapter = ""
        sentence_count = 0


        # Get the act number
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"{book_template}\n\n I need you to output only which act chapter {chapter_number} is in from the above template."}
            ]
        )
        act_number = response.choices[0].message.content
        
        # Write out section of summary
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nHere is a summary of a chapter I wrote:\n\n{act_number}\n{chap_summary_list[sentence_count]}\n\n\n\nBased on that, generate the chapter written in the style of {chapter_author}, and the category is {category_variable}."}
            ]
        )
        chapter = response.choices[0].message.content

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is what is in the chapter so far {chapter}\n\n\n\nContinue the chapter."}
            ]
        )
        part = response.choices[0].message.content
        chapter += f"\n\n\n{part}"

        # I need to reduce the number of tokens in the prompt. So I am having chatGPT summarize the entire chapter for each iteration of the loop, then having it build the chapter based on that.
        #summary
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"I am having you write a chapter. This is the chapter:\n{chapter}\n\nI need a summary of the chapter you have written so far."}
            ]
        )
        written_summary = response.choices[0].message.content


        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is what is in the chapter so far {chapter}\n\n\n\nContinue the chapter."}
            ]
        )
        part = response.choices[0].message.content
        chapter += f"\n\n\n{part}"

        #summary
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"I am having you write a chapter. This is the summary of the chapter so far:\n{written_summary}\n\nPlus here is what you just wrote:\n\n{part} I need an updated summary of the chapter you have written so far."}
            ]
        )
        written_summary = response.choices[0].message.content



        # build rest of required parts of chapter
        sentence_count = sentence_count + 1
        while sentence_count < number_of_sentences:
            # I need to reduce the number of tokens in the prompt. So I am having chatGPT summarize the entire chapter for each iteration of the loop, then having it build the chapter based on that.

            # Write Chapter Part from main chapter summary
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is a summary of what is in the chapter so far:\n\n{written_summary}\n\n\n Here is the part of the chapter that you just wrote {part}\n\n\n\nContinue the chapter. {chap_summary_list[sentence_count]}"}
                ]
            )
            part = response.choices[0].message.content
            chapter += f"\n\n\n{part}"
            
            #summary
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"I am having you write a chapter. This is the summary of the chapter so far:\n{written_summary}\n\nPlus here is what you just wrote:\n\n{part} I need an updated summary of the chapter you have written so far."}
                ]
            )
            written_summary = response.choices[0].message.content


            # Write Chapter Part
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is a summary of what is in the chapter so far:\n\n{written_summary}\n\n\n Here is the part of the chapter that you just wrote {part}\n\n\n\nContinue the chapter."}
                ]
            )
            part = response.choices[0].message.content
            chapter += f"\n\n\n{part}"
            

            #summary
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"I am having you write a chapter. This is the summary of the chapter so far:\n{written_summary}\n\nPlus here is what you just wrote:\n\n{part} I need an updated summary of the chapter you have written so far."}
                ]
            )
            written_summary = response.choices[0].message.content

            # Write Chapter Part
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is a summary of what is in the chapter so far:\n\n{written_summary}\n\n\n Here is the part of the chapter that you just wrote {part}\n\n\n\nContinue the chapter."}
                ]
            )
            part = response.choices[0].message.content
            chapter += f"\n\n\n{part}"

            sentence_count = sentence_count + 1


        

        # Continue writing until chapter is greater than 3000 words
        word_count = len(chapter.split())
        needed_count = 3000
        while word_count < needed_count:
            #summary
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"I am having you write a chapter. This is the summary of the chapter so far:\n{written_summary}\n\nPlus here is what you just wrote:\n\n{part} I need an updated summary of the chapter you have written so far."}
                ]
            )
            written_summary = response.choices[0].message.content



            # Write Chapter Part
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"These are the characters, descriptions, and their inventories, for a book I am writing: {characters}\n\nThe only characters in this chapter are {chapter_characters}\n\n\nThe chapter written in the style of {chapter_author}, and the category is {category_variable}.\n\n\nHere is a summary of what is in the chapter so far:\n\n{written_summary}\n\n\n Here is the part of the chapter that you just wrote {part}\n\n\n\nContinue the chapter."}
                ]
            )
            part = response.choices[0].message.content
            chapter += f"\n\n\n{part}"

            word_count = len(chapter.split())




        return chapter.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def paragraph_to_sentences(paragraph):
    """
    Splits a paragraph into a list of sentences.
    
    Parameters:
        paragraph (str): The input paragraph.
    
    Returns:
        list: A list where each element is a sentence from the paragraph.
    """
    # Use regex to split the paragraph into sentences
    sentences = re.split(r'(?<=[.!?]) +', paragraph)
    return sentences

def make_custom_chapter(characters, custom_text_input, book_plot, category_variable, book_template, chapter_author, chapter_number):
    try:
        # Structure chapter
        #response = client.chat.completions.create(
        #    model="gpt-4",
        #    messages=[
        #        {"role": "system", "content": "You are a creative assistant."},
        #        {"role": "user", "content": f"{book_template}\n\n Only output the plot of chapter {chapter_number} from the above template. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
        #    ]
        #)
        #chapter_overview = response.choices[0].message.content

        # Build Chapter
        # if not check_humor:
        #    response = client.chat.completions.create(
        #        model="gpt-4",
        #        messages=[
        #            {"role": "system", "content": "You are a creative assistant."},
        #            {"role": "user", "content": f"This is the plot of chapter {chapter_number} of a book:\n\n {chapter_overview}\n\n\n\n Write the actual chapter now with a word count of about 3,000. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
        #        ]
        #    )
        #    chapter_variable = response.choices[0].message.content
        #else:
        #    response = client.chat.completions.create(
        #        model="gpt-3",
        #        messages=[
        #            {"role": "system", "content": "You are a creative assistant."},
        #            {"role": "user", "content": f"This is the plot of chapter {chapter_number} of a book:\n\n {chapter_overview}\n\n\n\n Write the actual chapter now with a word count of about 3,000. It should be written in the style of {chapter_author}, and the category is {category_variable}. It needs to have crude humor and vulgar language to make it more funny."}
        #        ]
        #    )
        #    chapter_variable = response.choices[0].message.content
        
        # no vulger stuff yet
        #response = client.chat.completions.create(
        #    model="gpt-4",
        #    messages=[
        #        {"role": "system", "content": "You are a creative assistant."},
        #        {"role": "user", "content": f"This is the plot of chapter {chapter_number} of a book:\n\n {chapter_overview}\n\n\n\n Write the actual chapter now with a word count of about 3,000. It should be written in the style of {chapter_author}, and the category is {category_variable}."}
        #    ]
        #)
        #chapter_variable = response.choices[0].message.content

        # Chapter Creation
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                # {"role": "user", "content": f"A book plot was submitted from this idea: {custom_text_input}\n\nThis is the book plot from that idea:\n{book_plot}\n\nHere is the list of characters and their descriptions:\n\n{characters}.\n\nThis is the template of the book:\n{book_template}\n\n I need chapter {chapter_number} from the above template to be written with a 3,000 word count. Dont include characters that are not included for the chapter. It should be written in the style of {chapter_author}, and the category is {category_variable}. Make sure the characters have a good amount of dialog."}
                {"role": "user", "content": f"A book plot was submitted from this idea: {custom_text_input}\n\nThis is the book plot from that idea:\n{book_plot}\n\nThis is the template of the book:\n{book_template}\n\n I need chapter {chapter_number} from the above template to be written with a 3,000 word count. It should be written in the style of {chapter_author}, and the category is {category_variable}. Make sure the characters have a good amount of dialog."}

            ]
        )
        chapter_variable = response.choices[0].message.content

        return chapter_variable.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
