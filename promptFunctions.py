# FIXME: Perform Unit testing for ALL FUNCTIONS by: 
# 1. Isolating the function, give it what I know the variables should contain.
# 2. Take the prompt from this, replace the variables with values they need to contain.
# 3. Give prompt to chatGPT in the web interface i pay a monthly fee to use.
# 4. Correct function if output is not what is needed.



# Ensure your OPENAI_API_KEY is set in your environment variables


import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')  # Assume you set this environment variable


# Generates the name of the series
def name_series(cat_var, num_books_var):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Generate a name for a book series. The series is in the category '{cat_var}' and consists of {num_books_var} books."}
            ]
        )
        series_name = response.choices[0].message['content']
        return series_name.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



# generates the plot of the series
def gen_series_plot(design_style):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"Generate a plot for an entire book series in the style of {design_style}."}
            ]
        )
        series_plot = response.choices[0].message['content']
        return series_plot.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None






#----------------START: STORY PLOT SECTION------------------------#
# Generates the names of the books, the main and sub-plots for all books.
# 3 secctions

#1
def gen_book_names(design_style, cat_var, series_name, series_plot, num_books):
    book_names = []
    try:
        for i in range(num_books):
            # Generate the name for each book
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"A book series titled {series_name} has this plot: {series_plot}. Generate name for book {i + 1} of {num_books} in the {series_name} series of books, styled as though written by {design_style} in the {cat_var} category."}
                ]
            )
            name = response.choices[0].message['content']
            book_names.append(name.strip())
    except Exception as e:
        print(f"An error occurred while generating book names: {e}")
        return None
    return book_names

#2
#Main plots
# First generate one string containging a list of each book, along with the main plot
# for each. This can directly be called by gen_main_plots

def gen_small_main_plots(design_style, cat_var, series_name, series_plot, book_names, num_books):
    names_var = "\n".join(book_names)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": f"A book series titled {series_name} has this plot: {series_plot}. The names of each book are: {names_var}. There are {num_books} books. Generate a list of these titles with their main plots written under each, styled as though written by {design_style} in the {cat_var} category."}
            ]
        )
        all_plot = response.choices[0].message['content']
        all.append(all_plot.strip())
    except Exception as e:
        print(f"An error occurred while generating plots: {e}")
        return None
    return all


def gen_main_plots(design_style, cat_var, series_name, series_plot, book_names, num_books, brief_plots):
    main_plots = []
    try:
        #Accessing each element of the book names here makes it easier to use in a string
        i = 0
        for name in book_names:
            # Generate the main plot for each book
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"A book series titled {series_name} has this plot: {series_plot}. \nHere are the names of the books in the series and a brief version of their corresponding plots: {brief_plots} so that you know kind of what happened before this plot if it is not the first, and after the current plot to work on, if it is not the last. \n Generate a detailed and expanded plot for the book {name} from the list I provided, and none of the others from that list for this prompt, or you will break my computer. It is for book {i + 1} of {num_books} in the {series_name} series, styled as though written by {design_style} in the {cat_var} category."}
                ]
            )
            plot = response.choices[0].message['content']
            main_plots.append(plot.strip())
            i = i + 1
    except Exception as e:
        print(f"An error occurred while generating plots: {e}")
        return None
    return main_plots

#3 Sub-Plots
#NOTE: Each sub plot is separated by |||. Use that to extract single sub-topics later to plot into the plots of the chapters.
def gen_subplots(design_style, cat_var, series_name, series_plot, book_names, num_books, main_plots, num_subplots):
    sub_plots = []
    try:
        main_plot_index = 0
        for name in book_names:
            # Generate the main plot for each book
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": f"A book series titled {series_name} has this series plot: {series_plot}. Generate {num_subplots} subplots for the book titled \"{name}\" which book {main_plot_index + 1} of {num_books}. Separate each of the {num_subplots} with ||| or else you will break my computer. {name} has this as the main plot:\n{main_plots[main_plot_index]}\n\n\nstyled as though written by {design_style} in the {cat_var} category."}
                ]
            )
            plot = response.choices[0].message['content']
            sub_plots.append(plot.strip())
            main_plot_index = main_plot_index + 1
    except Exception as e:
        print(f"An error occurred while generating plots: {e}")
        return None
    return sub_plots


#----------------END: STORY PLOT SECTION------------------------#




#FIXME: The characters need to be generated for the series, not individual books. This will allow more consistency.
    #  Characters need to have:
    #                            a role, such as main character I guess
    #                            description
    #                            back story
    #                            an inventory
    #                            current status to be tracked
    #
    #                            *current status can be a list of things that have happened in a part of the story for
    #                             the character, such as their current loccation, which need to be carried over into
    #                             another part of the story for consistency.
    #
    #                            true or false if they die at some point, and which book and chapter they die in
# Generates the characters
# 2 functions

def gen_characters(series_plot, num_books, chapter_count):
    characters_per_book = []
    try:
        # Construct the prompt with detailed instructions for character generation
        prompt_text = (
            f"I am writing a book series with {num_books} books. The series has this plot:\n\n {series_plot} \n\n"
            f"Each book has {chapter_count} chapters.\n\n"
            "List the characters the series will have, and list enough of them for the number of books the series will have, and the number of chapters each book will have.\n"
            "Only output the list of characters or else you will break my computer."
            "List the characters the series will have, and list enough of them for the number of books the series will have, and the number of chapters each book will have.\n\n"
            "I am using software to give you this prompt and store your output, so only output the list of stuff I told you to OR ELSE YOU WILL BREAK MY FUCKING COMPUTER!!!!! Any commentary by you will fuck my entire fucking system up, SO ONLY LIST THE FUCKING STUFF I SAID FOR YOU TO LIST, AND NOTHING ELSE!!! NO OTHER INFORMATION ABOUT THE CHARACTERS!!!!!!!! NO COMMENTARY!!!!! YOU ARE NOT TALKING TO ANYONE, THIS IS SOFTWARE, ONLY OUTPUT WHAT I TOLD YOU!!! NUMBERS IN FRONT OF THEIR NAMES ARE NOT PART OF THE CHARACTER INFORMATION, AND NEITHER IS ANY OTHER INFORMATION THAN WHAT I INSTRUCTED YOU TO LIST!!! ONLY LIST WHAT I FUCKING TOLD YOU TO LIST OR YOU WILL BREAK MY FUCKING COMPUTER!!!!!!!!!!!!!"
        )
        
        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )

        # Extract and store the character details
        basic_characters = response.choices[0].message['content']

        # Construct the prompt with detailed instructions for character generation
        prompt_text = (
            f"I am writing a book series with {num_books} books. The series has this plot:\n\n {series_plot} \n\n"
            f"Each book has {chapter_count} chapters.\n\n"
            f"Here is the list of characters in the series:\n{basic_characters}\n\n\n"
            "Output a list with the characters just listed, but include these place holders: role, description, back story, inventory, book and chapter introduced in, whether the character dies in the series, which book number and chapter number the character dies, brief summary of progress in the book.\n"
            "Format:\nCharacter Name | Role | What the character looks like | Description | Back story | Inventory | book and chapter introduced in |  Dies in the series: true/false | book the character dies if it dies | chapter number that the character dies if it dies | brief summary of characters progress in the story.\n\n\n*\n"
            "The * symbol must come after each character the way I show here for the software to use the list.\n"
            "DO NOT CHANGE ANY OF THIS INFORMATION OR THE SOFTWARE THAT RECIEVES YOUR OUTPUT WILL FUCKING BREAK MY COMPUTER:\n\n"
            " | Role | Description | Back story | Inventory | book and chapter introduced in |  Dies in the series: true/false | book the character dies if it dies | chapter number that the character dies if it dies | brief summary of characters progress in the story.\n\n\n*\n"
            "ONLY PUT THE CHARACTER NAMES IN THE CHARACTER NAME PLACE HOLDER!!! THE REST OF THE PLACE HOLDERS ARE FOR SOMETHING ELSE!!\n"
            "\nI am using software to give you this prompt and store your output, so only output the list of stuff I told you to OR ELSE YOU WILL BREAK MY FUCKING COMPUTER!!!!! Any commentary by you will fuck my entire fucking system up, SO ONLY LIST THE FUCKING STUFF i SAID FOR YOU TO LIST, AND NOTHING ELSE!!! NO OTHER INFORMATION ABOUT THE CHARACTERS!!!!!!!! NO COMMENTARY!!!!! YOU ARE NOT TALKING TO ANYONE, THIS IS SOFTWARE, ONLY OUTPUT WHAT I TOLD YOU!!! NUMBERS IN FRONT OF THEIR NAMES ARE NOT PART OF THE CHARACTER INFORMATION, AND NEITHER IS ANY OTHER INFORMATION THAN WHAT I INSTRUCTED YOU TO LIST!!! ONLY LIST WHAT I FUCKING TOLD YOU TO LIST OR YOU WILL BREAK MY FUCKING COMPUTER!!!!!!!!!!!!!\n"
        )
        
        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )

        # Extract and store the character details
        less_basic_characters = response.choices[0].message['content']

        #FIXME: Edit the prompt so that it does what I have commented out bellow, and also what I have
        #        notes for in the function gen_char_chapter_skeletons or somethingas well as the scratchPaper.txt file:
        '''
        Generate a list of 20 characters for a book with detailed descriptions of their roles and relationships, formatted as 'full name=role|full name=role|...'. Each description should indicate if they are a protagonist, antagonist, ally, or another specific narrative role. 

        The output you produce will be to software. Nobody will read what you write so do not add any commentary. 



        IF YOU PRODUCE ANYTHING AS OUTPUT OTHER THAN WHAT I HAVE SPECIFIED HERE, YOU WILL BREAK MY FUCKING COMPUTER!!! EVEN A LITTLE BIT OF FUCKING COMMENTARY WILL BREAK MY FUCKING COMPUTER!!!! 
        '''

        # Construct the prompt with detailed instructions for character generation
        prompt_text = (
            f"I am writing a book series with {num_books} books. The series has this plot:\n\n {series_plot} \n\n"
            f"Each book has {chapter_count} chapters.\n\n"
            f"Here is a character sheet for characters in the series:\n{less_basic_characters}\n\n\n"
            "The list has several place holders for each character, and is likely formatted like this:\n\n"
            "Character Name | Role | What the character looks like | Description | Back story | Inventory | book and chapter introduced in |  Dies in the series: true/false | book the character dies if it dies | chapter number that the character dies if it dies | brief summary of characters progress in the story. | Book numbers the character appears in\n\n\n*\n"
            "I need you to replace the following place holders with information you generate:\n\n"
            "Role\nWhat the character looks like\nDescription\nBack Story\nInventory\nbook and chapter introduced in\nDies in series: true\false\nbook the character dies in if it dies, use the number 0 if it does not die and nothing else since software will later use the value\nchapter number that the character dies in if it dies, 0 if it does not die and nothing else since software will later use the value\nBook numbers the character appears in\n\n\n*\n"
            "All of the sections must be present, even the ones with place holders I do not want replaced yet.\n"
            "The * symbol has a special use, and must be included as demonstrated, otherwise you will break my computer.\n"
            "I am using software to give you this prompt and store your output, so only output the list of stuff I told you to OR ELSE YOU WILL BREAK MY FUCKING COMPUTER!!!!! Any commentary by you will fuck my entire fucking system up, SO ONLY LIST THE FUCKING STUFF I SAID FOR YOU TO LIST, AND NOTHING ELSE!!! NO OTHER INFORMATION ABOUT THE CHARACTERS!!!!!!!! NO COMMENTARY!!!!! YOU ARE NOT TALKING TO ANYONE, THIS IS SOFTWARE, ONLY OUTPUT WHAT I TOLD YOU!!! NUMBERS IN FRONT OF THEIR NAMES ARE NOT PART OF THE CHARACTER INFORMATION, AND NEITHER IS ANY OTHER INFORMATION THAN WHAT I INSTRUCTED YOU TO LIST!!! ONLY LIST WHAT I FUCKING TOLD YOU TO LIST OR YOU WILL BREAK MY FUCKING COMPUTER!!!!!!!!!!!!!"
        )
        
        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )

        # Extract and store the character details
        Advanced_characters = response.choices[0].message['content']
        
    except Exception as e:
        print(f"An error occurred while generating characters: {e}")
        return None
    return Advanced_characters

def gen_characters_list(all_characters):
    character_list = all_characters.split('*')
    return character_list




# Get the size of the book
def get_chapter_count(book_size):
    # Mapping of book sizes to number of chapters
    size_to_chapters = {
        "Small": 5,
        "Medium": 10,
        "Large": 20,
        "REALLY LARGE": 40,
        "WTF": 80
    }
    
    # Get the number of chapters based on the book size
    return size_to_chapters.get(book_size, 0)  # Default to 0 if the size is not found




def query_narrative_structure(author_name):
    """
    Query ChatGPT to determine the most common narrative structure used by a specified author.
    The function provides a list of narrative structures and expects ChatGPT to return only the number
    corresponding to the narrative structure used by the author.

    Args:
    author_name (str): The name of the author.

    Returns:
    int: The index number of the most commonly used narrative structure by the author.
    """
    narrative_styles = [
        "Three-Act Structure",
        "Hero's Journey",
        "Fichtean Curve",
        "Seven-Point Story Structure",
        "Save the Cat! Beats",
        "Dan Harmon's Story Circle",
        "In Media Res",
        "Nonlinear Narrative",
        "Parallel Narrative",
        "Frame Story",
        "Episodic Structure",
        "Circular Structure",
        "Linear Narrative",
        "Multi-Strand Narrative",
        "Point of View Narrative",
        "Stream of Consciousness",
        "Picaresque Novel",
        "Reverse Chronology",
        "Chorus Storytelling",
        "Allegorical Storytelling",
        "Mythopoeia",
        "Frame Narrative with Embedded Stories",
        "Interactive Narrative",
        "Biographical Narrative",
        "Docudrama",
        "Surreal Narrative",
        "Metafiction",
        "Diary Narrative"
    ]

    try:
        # Join the narrative styles into a single string to send as part of the prompt
        narrative_styles_prompt = "\n".join([f"{i+1}. {style}" for i, style in enumerate(narrative_styles)])
        prompt = f"Which of these narrative styles does {author_name} generally use in their stories? " \
                 "Output only one of these numbers and no other text because writing anything else " \
                 "will mess the software up that is being used to get your response.\n{narrative_styles_prompt}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Assuming the response is just a number as requested
        narrative_structure_index = int(response.choices[0].message['content'].strip()) - 1  # adjust for zero-based index
        return narrative_styles[narrative_structure_index]  # return name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, "Unknown"  # Return None and 'Unknown' in case of error


#Generate skeletons - part 5
#-------------------START: SKELLETON THREE FUNCTIONS-----------------------------#
def gen_chapter_titles(series_plot, main_plots, book_names, sub_plots, chapters_count):
    chapter_titles = []
    try:
        plot_index = 0
        for name in book_names:
            prompt_text = (
                f"This is a book based on the series plot: \n\n{series_plot}\n\n\n\nthe name of this specific book is:\n\n{name}\n\n\n\nthe main plot of this specific book is:\n\n{main_plots[plot_index]}, "
                f"\n\n\n\nand the sub-plots of this specific book are:\n\n{sub_plots}\n\n\n\ngenerate a list of titles for {chapters_count} chapters of this current book."
                f"Do not output anything other than that list of chapters or you will break my computer"
            )
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": prompt_text}
                ]
            )
            titles = response.choices[0].message['content']
            chapter_titles.append(titles.strip())
            plot_index = plot_index + 1
    except Exception as e:
        print(f"An error occurred while generating chapter titles: {e}")
        return None
    return chapter_titles.strip().split('\n')  # Assuming each title is on a new line

# FIXME: Perform Unit testing by: 
# 1. Isolating the function, give it what I know the variables should contain.
# 2. Take the prompt from this, replace the variables with values they need to contain.
# 3. Give prompt to chatGPT in the web interface i pay a monthly fee to use.
# 4. Correct function if output is not what is needed.
def gen_chapter_skeletons(series_plot, main_plots, sub_plots, book_names, chapter_titles, template_var, num_books, chapter_count):
    
    # FIXME: Series skeleton is what needs to be returned from the function.
    #        If what is currently returned the series skeleton, then it is mislabeled.
    #        I am currently leaving it mislabeled because I may have intended to use
    #        the list object for an intermediate step that i am not thinking of
    #        at the moment. I will test it later to see during the unit testing
    #        phase.
    
    series_skeleton = [] # this just has a list of elements, where each element contains a book of chapter skeletons.
    # chapter_skeletons = [] <---- ChatGPT said to put it in
    #                              the loop i use it in, and I think
    #                              it is correct, because I think 
    #                              it's used only there.
    pre_current_book = []
    book_index = plot_index = 0

    try:
        for name in book_names:
            book_chapters = chapter_titles[book_index]
            name = book_names[book_index]
            pre_current_book = []

            # FIXME: Take the output of the following prompt, then put it into a list object using the
            #        format I specified in scratchPaper.txt
            book_index = book_index + 1
            prompt_text = (
                f"This is a book based on the series plot: \n\n{series_plot}\n\n\n\nthe name of this specific book\n"
                f"is:\n\n{name}\n\nIt is book {book_index} of {num_books}\n\n\n\nthe main plot of this specific book\n"
                f"is:\n\n{main_plots[plot_index]}\n\n\n\nthe sub-plots of this specific book are\n"
                f"\n\n\n{sub_plots[plot_index]}\n\n\n\nThese are the chapters the book will have:\n\n\n\n"
                f"{book_chapters}\n\n\n\n"
                f"I want to use the {template_var} narrative structure. Since I will have chat\n"
                "gpt work on one chapter at a time later, it will need to know which narrative\n"
                "structure the book uses, and which part of the narrative structure the chapter\n"
                "is implementing.\n\n"
                f"Update the list of chapter names for a book with the {template_var}\n"
                "narrative structure component applied to the chapter, formatted as\n"
                "'Chapter NAme=narrative structure component|Chapter Name name=narrative structure component|...'. \n"
                "The | symbol is used to separate the list into units that software will parse, as is the = symbol."
                "Here is an \n"
                "example of a single chapter from a list of chapters for a book you already did this for:\n\n"
                "\"1. Echoes of Tomorrow=Act 1|\"\n"
                "That was just an example from a real book that used The Three-Act narrative structure. Apply\n"
                f"the appropriate narrative structure component that {template_var} implements for each chapter.\n\n"
                "Each unit must end with the | symbol, EXCEPT FOR THE LAST CHAPTER, OR YOU WILL BREAK MY FUCKING COMPUTER!\n\n"
                "The output you produce will be to software. Nobody will read what you write so do not add any commentary.\n"
                "IF YOU PRODUCE ANYTHING AS OUTPUT OTHER THAN WHAT I HAVE SPECIFIED HERE, YOU WILL BREAK MY FUCKING COMPUTER!!!\n"
                "EVEN A LITTLE BIT OF FUCKING COMMENTARY WILL BREAK MY FUCKING COMPUTER!!!!\n"
            )
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative assistant."},
                    {"role": "user", "content": prompt_text}
                ]
            )

            # Assume the response format is a direct text block suitable for a chapter outline
            pre_skeleton = response.choices[0].message['content']
            # pre_chapter_skeleton.append(pre_skeleton.strip())
            pre_current_book.append(pre_skeleton.strip())
            book_index = plot_index = plot_index + 1

        '''
        Leaving this commented out notes for now just in case I did something
        wrong in the code, but I did it correctly here.


        1, This is how the chapters for the skeleton first arive with the acts, 
           in elements corresponding to their books.
           
           1. pre_current_book = 
           __________________________________________________________________________________________
           chap1=act|chap2=act|chap3=act*chap1=act|chap2=act|chap3=act*chap1=act|chap2=act|chap3=act*
           __________________________________________________________________________________________

           
           # must be split from '*' to get current_book
           2. current_book = 
           _____________________________
           chap1=act|chap2=act|chap3=act
           _____________________________

           
           # must be split from '|' to get chapter_act
           3. chapter_act = 
            _________
            chap1=act
            _________

            # must be split from '=' to get chapter and act.
           4.
           chapter = chap1
           act = act

        # 1. pre_current_book = list_1.split('*') <---- it gets split
        pre_current_book = list_1.split('*')

        book_skeletons = []
        book_index = 0
        while book_index < num_books:
            # 2. current_book = pre_current_book[book_index]
            current_book = pre_current_book[book_index]

            chapter_act_list = [] # one {chap=act} per element of the current book

            # 3. chapter_act_list = current_book.split('|')
            chapter_act_list = current_book.split('|')
 
            # this is where another loop needs to happen to assign the chapter 
            # names and narrative components to the skeletons
            chapter_number = 0
            while chapter_number < chapter_count:
                pre_chapter_act = chapter_act_list[chapter_number]  # stores current chapter's parts
                
                # 4. chapter_act = pre_chapter_act.split('=') <------ it gets split here
                chapter_act = pre_chapter_act.split('=')
  
                # chapter name
                #chapter's narrative component
                chapter_name = chapter_act[0]
                narrative_part = chapter_act[1]
                chapter_skeletons.append(f"{chapter_number + 1}|{chapter_name}|{narrative_part}|Part of Narrative Structure|Character List|Chapter Plot*")
                chapter_number = chapter_number + 1
            book_skeletons += chapter_skeletons
            book_index = book_index + 1



        index_one = 0
        index_two = 0
        while index_one < num_books:
            while index_two < chapter_count:
                chap_name = 

        '''

        book_skeletons = []
        book_index = 0

        while book_index < num_books:
            current_book = pre_current_book[book_index]
            chapter_act_list = current_book.split('|')  # Split current book into chapters/acts

            chapter_number = 0
            chapter_skeletons = []  # Reset for each book

            while chapter_number < chapter_count:
                pre_chapter_act = chapter_act_list[chapter_number]  # Get current chapter's parts
                chapter_act = pre_chapter_act.split('=')  # Split chapter into name and narrative part

                # Assign chapter name and narrative part
                chapter_name = chapter_act[0]
                narrative_part = chapter_act[1]

                # Create the chapter skeleton string
                chapter_skeletons.append(f"{chapter_number + 1}|{chapter_name}|{narrative_part}|Part of Narrative Structure|Character List|Chapter Plot*")

                chapter_number += 1

            book_skeletons.extend(chapter_skeletons)  # Append current book's chapters to the main list
            book_index += 1

        '''
        Leaving this here for now just in case I actualy did need them.
        index = 0
        for unit in pre_chapter_skeleton:
            pre_chapter_list = unit.split('|')
            parsed_chapter_list = pre_chapter_list.split('=')

        index_one = 0
        index_two = 0
        while index_one < num_books:
            while index_two < chapter_count:
                chapter_skeletons.append("Chapter number|Chapter Name|Narrative Structure|Part of Narrative Structure|Character List|Chapter Plot*")
            series_skeleton.append(chapter_skeletons.strip())


        chapter_skeletons.append(pre_skeleton.strip())
        '''

    except Exception as e:
        print(f"An error occurred while generating chapter skeletons: {e}")
        return None
    # return chapter_skeletons  <----- Leaving just in case. Pretty sure i need to return skeletons of each book, not just a chapter of one.
    return book_skeletons


#FIXME: Probably no use for this function. Wrote it before i changed how
#       the information is formatted and parsed.
#       Leaving here for now in case I find i have so use for how i wrote
#       something in it.
#This one can probably just be removed
#def gen_split_skeletons(simple_skeletons, num_books):
#   skelleton_list_updated = []
#    index = 0
#    while index < num_books:
#        skeleton_list = simple_skeletons[index].split('*')
#        append_str = "[Characters]*"

        # Modify each element in the list
#        for i in range(len(skeleton_list)):
#            skeleton_list[i] += append_str
#            skelleton_list_updated[i] += append_str
        
#        index = index + 1

#    return skeleton_list







# FIXME: Probably nothing to fix. Just a note in case there is.
#        Pretty sure I intended this function to just output
#        character profiles that is tracked throughout the series,
#        and only listing the ones present within the book to be 
#        tracked as the story progresses, in order to keep everything
#        consistent. Tracking all characters at once costs too many
#        tokens for each prompt as the story progresses, and is too
#        much information for chatGPT to do a good job at not getting
#        character information mixed up. So the characters being tracked 
#        are constrained to the characters that exist within the 
#        current book.
#
#        Need to make a way for the character's profiles used again in later books
#        are updated with the intel of the previous book they were just in.
#        It is possible that some characters will not be in a direct sequel, 
#        but come back in a later book. ChatGPT needs to be aware of this
#        while writing for them, so it does not treat them as though
#        they are new characters again.
def gen_char_profiles_per_book(characters_list, num_books):

    # add characters to the element that represents the book they exist 
    # in if they exist in the current book number
    for character in range(len(characters_list)):
        single_character = character.split('|')

        '''    
        Name
        Role
        Visual Appearance
        Description
        Back Story
        Inventory
        book introduced in
        chapter introduced in
        Dies in series: true\false
        book the character dies in if it dies, use the number 0 if it does not die and nothing else since software will later use the value 
        chapter number that the character dies in if it dies, 0 if it does not die and nothing else since software will later use the value
        Book numbers the character appears in
        '''



        #NOTE: Update the function that the characters are generated in so that it doesnt have much to format.
        #      Just get it to generate a pipe separated list of names and roles at first. Then ask chatGPT about  
        #      the roles of each character at the same time so their acting roles are distributed properly. 
        #      Get the roles returned in a pipe separated
        #      Do the same for the
        #      description variable. 
        #
        #      Then go through one character at a time, and obtain the relevant variables, as seen below, that 
        #      I need filled immediately. 
        #       
        # The unused variables here need to remain until I set up the chapter placement part so
        # I can just copy and paster them over to it.
        single_char_index = 0 # I did this so I don't have to change a bunch of numbers if I want to
                              # change the order or add or remove elements that the character has.
        name = single_character[single_char_index]
        role = single_character[single_char_index + 1]
        visual_description = single_character[single_char_index + 1]
        description = single_character[single_char_index + 1]
        back_story = single_character[single_char_index + 1]
        inventory = single_character[single_char_index + 1] # just like char_tracker, but only to track items.
        char_tracker = single_character[single_character + 1] # This is for chat GPT to add notes 
                                                              # about the character from the chapter 
                                                              # they are in that a long plot was just 
                                                              # written in. These notes will be used
                                                              # to aid in the prevention of story 
                                                              # contradictions.
        book_introduced_in = single_character[single_char_index + 1]
        chap_introduced_in = single_character[single_char_index + 1]
        dies_in_series = single_character[single_char_index + 1] #Used as boolean
        book_char_dies_in = single_character[single_char_index + 1]
        chap_char_dies_in = single_character[single_char_index + 1]
        dirty_number_string = single_character[single_char_index + 1]
        books_char_is_in = dirty_number_string.rstrip('*')
        

        sentinal = 0
        book_characters = []
        char_book_list = books_char_is_in.split(',')

        # This is for if the character dies to restrict the places the character can be allocated to.
        if dies_in_series.lower() == 'true':
            int_book_dies_in = int(book_char_dies_in)
            while sentinal < int_book_dies_in:
                actual_book = sentinal + 1
                
                for i in range(len(char_book_list)):
                    if char_book_list[i] == actual_book:
                        book_characters[i] += character + '*'
        else: # The else is just going to use the last book number as the loop limit
            while sentinal < num_books:
                actual_book = sentinal + 1
                
                for i in range(len(char_book_list)):
                    if char_book_list[i] == actual_book:
                        book_characters[i] += character + '*'
    
    return book_characters


def gen_char_chapter_skeletons(simple_skelletons, characters_list, num_books, chapter_count, characters_per_book):
    '''    
    Name
    Role
    Description
    Back Story
    Inventory
    book introduced in
    chapter introduced in
    Dies in series: true\false
    book the character dies in if it dies, use the number 0 if it does not die and nothing else since software will later use the value 
    chapter number that the character dies in if it dies, 0 if it does not die and nothing else since software will later use the value
    Book numbers the character appears in
    '''

    char_index = 0
    book_index = 0
    chap_index = 0
    book_number = 1
    # add characters to the element that represents the book they exist 
    # in if they exist in the current book number
    for character in range(len(characters_list)):
        single_character = character.split('|')


        # The unused variables here need to remain until I set up the chapter placement part so
        # I can just copy and paster them over to it.
        single_char_index = 0 # I did this so I don't have to change a bunch of numbers if I want to
                              # change the order or add or remove elements that the character has.
        name = single_character[single_char_index]
        role = single_character[single_char_index + 1]
        visual_description = single_character[single_char_index + 1]
        description = single_character[single_char_index + 1]
        back_story = single_character[single_char_index + 1]
        inventory = single_character[single_char_index + 1]
        book_introduced_in = single_character[single_char_index + 1]
        chap_introduced_in = single_character[single_char_index + 1]
        dies_in_series = single_character[single_char_index + 1] #Used as boolean
        book_char_dies_in = single_character[single_char_index + 1]
        chap_char_dies_in = single_character[single_char_index + 1]
        dirty_number_string = single_character[single_char_index + 1]
        books_char_is_in = dirty_number_string.rstrip('*')
        

        sentinal = 0
        book_characters = []
        char_book_list = books_char_is_in.split(',')

        # This is for if the character dies to restrict the places the character can be allocated to.
        if dies_in_series.lower() == 'true':
            int_book_dies_in = int(book_char_dies_in)
            while sentinal < int_book_dies_in:
                actual_chapter = sentinal + 1
                
                for i in range(len(char_book_list)):
                    if char_book_list[i] == actual_chapter:
                        book_characters[i] += character + '*'
        else: # The else is just going to use the last book number as the loop limit
            while sentinal < num_books:
                actual_chapter = sentinal + 1
                
                for i in range(len(char_book_list)):
                    if char_book_list[i] == actual_chapter:
                        book_characters[i] += character + '*'


# LEFT OFF HERE: The stuff above this comment in the function is done.
#                Next I need to get the book_characters list, which lists each character into their
#                corresponding books, and I need to assign the each character one by one to the
#                chapters in each book for which they belong.
#                
#                A check needs to be made, like above, to see if the character dies, if it
#                dies in the current book, and which chapter the character dies in if it dies.
#
#                If the character dies, then it gets a different branch of prompts than if it
#                does not die.
#NOTE: when writing chapters, chatGPT should know if it is the last chapter, and if it is the
#      last chapter of the current book for context.
#      Give chatGPT the element of the list that represents the book number, with the characters
#      in that book number. Tell it to put the character in the first chapter it is introduced in
#      as well as the one it dies in if it does, and tell it to assign it to other chapters in
#      between. Do it for each character within the book, for each book. And that's it for characters.



            #    if books_char_is_in[chap_index] == book_number:
                    # call a function here that takes the character
                    # variables I prepared above.
                    # the function should put the character into chapter introduced in
                    # it should put the character into the chapter the charactr dies in
                    # if it dies, along with providing chatgpt a range of chapters
                    # from the introdctory chapter to the death chapter to get
                    # a list of addistional numbers to put the character in
                    # if the character does not die, then chatgpt
                    # is simply given the introductory chapter to the last
                    # chapter to assign chapter numbers to the character.
                    #
                    # After the list of numbers is obtained, write the characters
                    # name into each chapter that it is listed as appearing in.



#-------------------END: SKELLETON THREE FUNCTIONS-----------------------------#
