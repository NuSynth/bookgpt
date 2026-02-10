# This not is for chatGPT while I get help from it to complete this software. 
# Stop putting if blocks in the function generate_story() because the program
# is only for me, I do not know python, these if blocks are cluttering the code
# because python is not as easy for me to read as C. Since it is only me using
# the program, and I will know to be sure that I will have all of the relevent date
# before any function called from within generate_story() will be available. If
# I have any problems like that, then I will add the if parts later once the rest 
# of the program is finished.

import promptFunctions as pf
import tkinter as tk
from tkinter import ttk



def main():
    # Create the main window
    root = tk.Tk()
    root.title("Story Generator")
    
    def generate_story():
        # The reason I don't have skelleton setup section and write_chapters section in their own separate sub-functions
        # is because the skelleton setup section simply fills variables and lists that are needed in order to actually write the books.
        # It would be a lot of parts to give to a write_chapters function. It's easier to just do it all here.
        # In the design documents, I can stil treat these as two separate functions, as they pretty much are modular.


        # GUI inputs START
        # setup_skelletons section
        design_author = design_var.get()
        chapter_author = writing_var.get()
        category_variable = category_var.get()

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

        #### setup_skelletons START####
        # Generate the series name and the series plot
        if not checkbox_checked:  # Use `not` to check for False in Python
            book_name = pf.name_book(design_author, category_variable)
            book_plot = pf.book_plot(design_author, category_variable, book_name)
        else:
            book_name = pf.custom_name_book(custom_text_input, design_author, category_variable)
            book_plot = pf.custom_book_plot(custom_text_input, design_author, category_variable, book_name)


        #For character generation
        characters = pf.characters_in_book(book_plot)

        default_twelve = 12
        if not check_template:
            if not check_numchaps:
                book_template = pf.book_template(characters, design_author, category_variable, book_plot, default_twelve)
                pf.write_to_book(characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, default_twelve, check_numchaps)
            else:
                custom_template = pf.book_template(characters, design_author, category_variable, book_plot, chapter_quantity)
                pf.write_to_book(characters, custom_text_input, book_plot, book_name, category_variable, custom_template, chapter_author, chapter_quantity, check_numchaps)

                #pf.write_to_book(custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, chapter_quantity, check_numchaps):
        else:
            if not check_numchaps:
                book_template = pf.book_template(characters, design_author, category_variable, book_plot, default_twelve)
                pf.write_to_template(design_author, characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, default_twelve, check_numchaps)
            else:
                custom_template = pf.book_template(characters, design_author, category_variable, book_plot, chapter_quantity)
                pf.write_to_template(design_author, characters, custom_text_input, book_plot, book_name, category_variable, book_template, chapter_author, chapter_quantity, check_numchaps)




    # Create a frame for the "Styles" section
    styles_frame = ttk.LabelFrame(root, text="Styles", padding=(20, 10))
    styles_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Dropdown for "Writing"
    writing_label = ttk.Label(styles_frame, text="Writing:")
    writing_label.grid(row=0, column=0, sticky="w")
    writing_authors = ["Ernest Hemingway", "Douglas Adams", "Clive Barker", "Riddley Scott","John Carpenter", "Insane Donald Trump", "Miguel de Cervantes", "Phillip k Dick", "Madison Love", "Jessie Gussman", "Rl stine", "Charles Dickens", "Antoine de Saint-Exupéry", "J.K. Rowling", "Gabriel García Márquez", "Harper Lee", "Margaret Mitchell", "Paulo Coelho", "Anna Sewell", "E.L. James", "F. Scott Fitzgerald", "Johanna Spyri", "Markus Zusak", "William P. Young", "George Orwell", "Erich Maria Remarque", "Emily Brontë", "Oscar Wilde", "Bram Stoker", "Mary Shelley"]
    writing_var = tk.StringVar()
    writing_dropdown = ttk.Combobox(styles_frame, textvariable=writing_var, values=writing_authors)
    writing_dropdown.grid(row=0, column=1, sticky="ew")
    writing_dropdown.set("Select an Author")

    # Dropdown for "Story Design"
    design_label = ttk.Label(styles_frame, text="Story Design:")
    design_label.grid(row=1, column=0, sticky="w")
    
    design_authors = ["Ernest Hemingway", "Douglas Adams", "Clive Barker", "Ridley Scott", "John Carpenter", "Insane Donald Trump", "Miguel de Cervantes", "Phillip k Dick", "Madison Love", "Jessie Gussman", "H. P. Lovecraft", "Rl stine", "Charles Dickens", "Antoine de Saint-Exupéry", "J.K. Rowling", "Gabriel García Márquez", "Harper Lee", "Margaret Mitchell", "Paulo Coelho", "Anna Sewell", "E.L. James", "F. Scott Fitzgerald", "Johanna Spyri", "Markus Zusak", "William P. Young", "George Orwell", "Erich Maria Remarque", "Emily Brontë", "Oscar Wilde", "Bram Stoker", "Mary Shelley"]
    design_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=design_var, values=design_authors)
    design_dropdown.grid(row=1, column=1, sticky="ew")
    design_dropdown.set("Select Author")
    
    # Dropdown for "Category"
    design_label = ttk.Label(styles_frame, text="Story Category:")
    design_label.grid(row=2, column=0, sticky="w")
    
    categories = ["Fiction", "Comedy Science Fiction", "Science Fiction","Sci-Fi horror","Horror", "Holiday Romance", "Fantasy", "Comedy", "Christian SciFi", "Christian Fantasy"]
    category_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=category_var, values=categories)
    design_dropdown.grid(row=2, column=1, sticky="ew")
    design_dropdown.set("Select a Category")

    # New start
    # Checkbox for additional option
    checkbox_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(styles_frame, text="Custom Idea", variable=checkbox_var)
    checkbox.grid(row=3, column=0, columnspan=2, sticky="w")

    # Entry for custom text input
    custom_text_label = ttk.Label(styles_frame, text="Story Idea:")
    custom_text_label.grid(row=4, column=0, sticky="w")
    custom_text_var = tk.StringVar()
    custom_text_entry = ttk.Entry(styles_frame, textvariable=custom_text_var)
    custom_text_entry.grid(row=4, column=1, sticky="ew")

    # Checkbox for custom number of chapters - This part needs more work in the backend code in order to function properly. Dont use it.
    check_chaps = tk.BooleanVar()
    checkbox_chapters = ttk.Checkbutton(styles_frame, text="Number of Chapters", variable=check_chaps)
    checkbox_chapters.grid(row=5, column=0, columnspan=2, sticky="w")

    chapter_number = tk.IntVar(value=1)
    chapter_spin = tk.Spinbox(styles_frame, from_=1, to=100, textvariable=chapter_number, width=5)
    chapter_spin.grid(row=6, column=1, sticky="w")

    # Checkbox for crude humor and vulgor language
    # checkbox_humor = tk.BooleanVar()
    # checkbox = ttk.Checkbutton(styles_frame, text="Crude Humor", variable=checkbox_humor)
    # checkbox.grid(row=7, column=0, columnspan=2, sticky="w")

    # Only output the template of the book so a human can write it.
    check_template_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(styles_frame, text="Only a template", variable=check_template_var)
    checkbox.grid(row=7, column=0, columnspan=2, sticky="w")

    # New End

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

