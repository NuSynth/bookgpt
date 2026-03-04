import promptFunctions as pf
import tkinter as tk
from tkinter import ttk



def main():
    # Create the main window
    root = tk.Tk()
    root.title("Story Generator")
    
    def generate_story():
        # GUI inputs START
        # setup_skelletons section
        design_author = design_var.get()
        chapter_author = writing_var.get()
        category_variable = category_var.get()
        structure_choice = structure_var.get()

        # new
        # For custom idea
        checkbox_checked = checkbox_var.get()
        custom_text_input = custom_text_var.get()

        # For custom number of chapters
        check_numchaps = check_chaps.get()
        chapter_quantity = chapter_number.get()


        # For Crude Humor
        # check_humor = checkbox_humor

        #For only a template
        check_template = check_template_var.get()

        # A.I. model selection
        model_choice = model_selected.get()

        # This is needed for some genres to have blood and gore
        book_genre = category_var.get()

        # This is if the user wants to structure the book differently than the selected design author would have. Reduces plagiarism risk.
        structure_check = structure_checkbox_var.get()

        # This is if the user wants the story to be told from a first-person point of view
        first_person_pov = first_person.get()


        #### setup_skelletons START####
        # Generate the series name and the series plot
        if not checkbox_checked:  # Use `not` to check for False in Python
            book_name = pf.name_book(design_author, category_variable)
            book_plot = pf.book_plot(design_author, category_variable, book_name)
        else:
            book_name = pf.custom_name_book(custom_text_input, design_author, category_variable)
            book_plot = pf.custom_book_plot(custom_text_input, design_author, category_variable, book_name)

        # Custom or default number of chapters
        TRUE = 1
        FALSE = 0
        DEFAULT_TWELVE = 12
        if not check_numchaps:
            chapter_quantity = DEFAULT_TWELVE

        if not check_template:
            template = FALSE
        else:
            template = TRUE
        
        #For character generation
        characters = pf.characters_in_book(book_plot, chapter_quantity)


        # Write the templates and book
        book_template = pf.book_template(structure_check, structure_choice, book_genre, characters, design_author, category_variable, book_plot, chapter_quantity)
        pf.write_to_template(first_person_pov, book_genre, model_choice, design_author, characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, chapter_quantity, template)




    # Create a frame for the "Styles" section
    styles_frame = ttk.LabelFrame(root, text="Styles", padding=(20, 10))
    styles_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    #For book design and writing style
    authors_list = [
        "Anna Sewell",
        "Antoine de Saint-Exupéry",
        "Arthur C. Clarke",
        "Bram Stoker",
        "Charles Dickens",
        "Clive Barker",
        "Douglas Adams",
        "E.L. James",
        "Emily Brontë",
        "Erich Maria Remarque",
        "Ernest Hemingway",
        "F. Scott Fitzgerald",
        "Frank Herbert",
        "Gabriel García Márquez",
        "George Lucas",
        "George Orwell",
        "H. P. Lovecraft",
        "Harper Lee",
        "Insane Donald Trump",
        "Isaac Asimov",
        "J.K. Rowling",
        "Jessie Gussman",
        "Johanna Spyri",
        "John Carpenter",
        "Madison Love",
        "Margaret Mitchell",
        "Markus Zusak",
        "Mary Shelley",
        "Matthew J. Costello",
        "Miguel de Cervantes",
        "Oscar Wilde",
        "Paulo Coelho",
        "Phillip K. Dick",
        "Ridley Scott",
        "RL Stine",
        "Robert A. Heinlein",
        "Rod Serling",
        "William Gibson",
        "William P. Young"
    ]

    # Dropdown for "Writing"
    writing_label = ttk.Label(styles_frame, text="Writing:")
    writing_label.grid(row=0, column=0, sticky="w")
    writing_authors = authors_list
    writing_var = tk.StringVar()
    writing_dropdown = ttk.Combobox(styles_frame, textvariable=writing_var, values=writing_authors)
    writing_dropdown.grid(row=0, column=1, sticky="ew")
    writing_dropdown.set("Select an Author")

    # Dropdown for "Story Design"
    design_label = ttk.Label(styles_frame, text="Story Design:")
    design_label.grid(row=1, column=0, sticky="w")
    design_authors = authors_list
    design_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=design_var, values=design_authors)
    design_dropdown.grid(row=1, column=1, sticky="ew")
    design_dropdown.set("Select Author")
    
    # Dropdown for "Category"
    design_label = ttk.Label(styles_frame, text="Story Category:")
    design_label.grid(row=2, column=0, sticky="w")
    
    categories = [
        "Fiction", 
        "Comedy Science Fiction",
        "Science Fiction",
        "Sci-Fi horror",
        "Horror",
        "Holiday Romance",
        "Fantasy",
        "Comedy",
        "Christian SciFi",
        "Christian Fantasy"
    ]


    category_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=category_var, values=categories)
    design_dropdown.grid(row=2, column=1, sticky="ew")
    design_dropdown.set("Select a Category")

    writing_structures = [
        "Chiastic",
        "Circular Narrative",
        "Dan Harmon Story Circle",
        "Episodic",
        "Epistolary",
        "Fichtean Curve",
        "Five-Act",
        "Frame Narrative",
        "Freytag's Pyramid",
        "Hero's Journey",
        "In Medias Res",
        "Kishōtenketsu",
        "Linear Narrative",
        "Monomyth",
        "Nonlinear Narrative",
        "Parallel Narrative",
        "Quest",
        "Rags to Riches",
        "Save the Cat Beat Sheet",
        "Seven-Point Story",
        "Snowflake Method",
        "Story Within a Story",
        "Three-Act",
        "Tragedy",
        "Try-Fail Cycle"
    ]

    # Checkbox for writing structure
    structure_checkbox_var = tk.BooleanVar()
    structure_checkbox = ttk.Checkbutton(styles_frame, text="Custom Structure", variable=structure_checkbox_var)
    structure_checkbox.grid(row=3, column=0, columnspan=2, sticky="w")

    # Dropdown options for custom structure
    structure_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=structure_var, values=writing_structures)
    design_dropdown.grid(row=3, column=1, sticky="ew")
    design_dropdown.set("Select a Structure")

    # Checkbox for custom idea
    checkbox_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(styles_frame, text="Custom Idea", variable=checkbox_var)
    checkbox.grid(row=4, column=0, columnspan=2, sticky="w")

    # Entry for custom text input
    custom_text_label = ttk.Label(styles_frame, text="Story Idea:")
    custom_text_label.grid(row=5, column=0, sticky="w")
    custom_text_var = tk.StringVar()
    custom_text_entry = ttk.Entry(styles_frame, textvariable=custom_text_var)
    custom_text_entry.grid(row=5, column=1, sticky="ew")


    # Checkbox for narration point of view
    first_person = tk.BooleanVar()
    checkbox = ttk.Checkbutton(styles_frame, text="First-person POV", variable=first_person)
    checkbox.grid(row=6, column=0, columnspan=2, sticky="w")

    # Checkbox for custom number of chapters
    spacer = tk.Frame(styles_frame, height=20) # This is to separate it from other options a little
    spacer.grid(row=7, column=0)
    check_chaps = tk.BooleanVar()
    checkbox_chapters = ttk.Checkbutton(styles_frame, text="Number of Chapters", variable=check_chaps)
    checkbox_chapters.grid(row=7, column=0, columnspan=2, sticky="w")

    chapter_number = tk.IntVar(value=1)
    chapter_spin = tk.Spinbox(styles_frame, from_=1, to=100, textvariable=chapter_number, width=5)
    chapter_spin.grid(row=8, column=1, sticky="w")

    # Checkbox for crude humor and vulgor language
    # checkbox_humor = tk.BooleanVar()
    # checkbox = ttk.Checkbutton(styles_frame, text="Crude Humor", variable=checkbox_humor)
    # checkbox.grid(row=7, column=0, columnspan=2, sticky="w")

    # Only output the template of the book so a human can write it.
    check_template_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(styles_frame, text="Only a template", variable=check_template_var)
    checkbox.grid(row=9, column=0, columnspan=2, sticky="w")

    # Radio button for A.I. selection
    model_selected = tk.IntVar(value=1)

    radio1 = tk.Radiobutton(styles_frame, text="ChatGPT", variable=model_selected, value=1)
    radio2 = tk.Radiobutton(styles_frame, text="Gemini", variable=model_selected, value=2)

    spacer = tk.Frame(styles_frame, height=20) # This is to separate it from other options a little
    spacer.grid(row=10, column=0)

    radio_label = ttk.Label(styles_frame, text="A.I. model to write story")
    radio_label.grid(row=11, column=0, sticky="w")
    radio1.grid(row=12, column=0, columnspan=4, sticky="w")
    radio2.grid(row=13, column=0, columnspan=4, sticky="w")

    # Create a frame for the "Start" button and "Generate Story" label
    start_frame = ttk.Frame(root, padding=(20, 10))
    start_frame.grid(row=4, column=0, padx=20, pady=10, sticky="e")

    # Start button
    start_button = ttk.Button(start_frame, text="Start", command=generate_story)
    start_button.grid(row=0, column=1)

    # Generate Story label
    generate_label = ttk.Label(start_frame, text="Generate Story:")
    generate_label.grid(row=0, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()
