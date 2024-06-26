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
        
        #### Set up skelletons START####
        # Generate the series name and the series plot
        series_name = pf.name_series(cat_var.get(), num_books_var.get())
        series_plot = pf.gen_series_plot(design_var.get(), cat_var.get()) 

        # Get the size of the book
        book_size = bsize_var.get()  # This gets the current selected value from the dropdown
        chapter_count = pf.get_chapter_count(book_size)


        # Get number of book plots
        num_books = num_books_var.get()  # Number of books in the series
        num_subplots = sPlots_var.get()  # Number of subplots per book


        # Generate characters for each book 
        all_characters = pf.gen_characters(series_plot, num_books, chapter_count) # This contains all the character profiles in one string
        characters_list = pf.gen_characters_list(all_characters) # This has all the character profiles split into a list so the gpt model can analyze each individually to better assign them to chapters.
        #characters = pf.gen_characters_list(series_plot, main_plots, sub_plots, [num_subplots] * num_books, characters_list)       


        # Generate book_plots
        #FIXME: Present the character sheet for the main plots to be consistent with character sheet
        book_names = pf.gen_book_names(design_var.get(), cat_var, series_name, series_plot, book_names, num_books)
        brief_plots = pf.gen_small_main_plots(design_var.get(), cat_var, series_name, series_plot, book_names, num_books)
        main_plots = pf.gen_main_plots(design_var.get(), cat_var.get(), series_name, series_plot, book_names, num_books, brief_plots)
        sub_plots = pf.gen_sub_plots(design_var.get(), cat_var.get(), series_name, series_plot,book_names, num_books, main_plots, num_subplots)
  

        # Generate Chapter Titles
        chapter_titles = pf.gen_chapter_titles(series_plot, main_plots, book_names, sub_plots, chapter_count)
        

        # Get story design author's narrative structure
        author = design_var.get()
        narrative_structure_name = pf.query_narrative_structure(author)
        template_var = narrative_structure_name
        

        # Generate the chapter skeleton of the books
        simple_skelletons = pf.gen_chapter_skeletons(series_plot, main_plots, sub_plots, book_names, chapter_titles, template_var, num_books)
        
        # Skeletons_array_list likely not needed since output
        # of gen_split_skeletons is obsolete from re-writing 
        # gen_chapter_skeletons
        #skeletons_array_list = pf.gen_split_skeletons(simple_skelletons, num_books) # Empty Characters section is added to each element here
        
        characters_per_book = pf.gen_char_profiles_per_book(characters_list, num_books) #The empty characters section is filled here
        
        # Only the character names are written to the appropriate chapters for each book's skeleton
        characters_in_chapters = pf.gen_char_chapter_skeletons(simple_skelletons, characters_list, num_books, chapter_count, characters_per_book) #The empty characters section is filled here

        
        
        #### Set up skelletons END####

        # Write Chapters START
        
        # keep the character information in the
        # characters_per_book list. 

        # They do not need to be written in to a characters section
        # of a book chapter skelleton object iteslf because parsing
        # it gets over complicated.

        # It is over complicated because I am running out of symbols 
        # I can use to split the segments of the elements up into a new list.

        # Instead, make a new list that represents each book.
        # Like the book chapter skelletons, each element of 
        # this list contains segments that represent each chapter,



        # Write Chapters END




    # Create a frame for the "Styles" section
    styles_frame = ttk.LabelFrame(root, text="Styles", padding=(20, 10))
    styles_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Dropdown for "Writing"
    writing_label = ttk.Label(styles_frame, text="Writing:")
    writing_label.grid(row=0, column=0, sticky="w")
    
    writing_authors = ["Author A", "Author B", "Author C"]
    writing_var = tk.StringVar()
    writing_dropdown = ttk.Combobox(styles_frame, textvariable=writing_var, values=writing_authors)
    writing_dropdown.grid(row=0, column=1, sticky="ew")
    writing_dropdown.set("Select an Author")

    # Dropdown for "Story Design"
    design_label = ttk.Label(styles_frame, text="Story Design:")
    design_label.grid(row=1, column=0, sticky="w")
    
    design_authors = ["Author X", "Author Y", "Author Z"]
    design_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=design_var, values=design_authors)
    design_dropdown.grid(row=1, column=1, sticky="ew")
    design_dropdown.set("Select Author")
    
    # Dropdown for "Category"
    design_label = ttk.Label(styles_frame, text="Story Category:")
    design_label.grid(row=2, column=0, sticky="w")
    
    categories = ["Fiction", "Science Fiction", "Fantasy", "Comedy", "Christian SciFi", "Christian Fantasy"]
    cat_var = tk.StringVar()
    design_dropdown = ttk.Combobox(styles_frame, textvariable=cat_var, values=categories)
    design_dropdown.grid(row=2, column=1, sticky="ew")
    design_dropdown.set("Select a Category")

    # Create a frame for the "Series" section
    series_frame = ttk.LabelFrame(root, text="Series", padding=(20, 10))
    series_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    # Checkbox for "Series"
    series_var = tk.BooleanVar()
    series_check = ttk.Checkbutton(series_frame, text="Series", variable=series_var)
    series_check.grid(row=0, column=0, sticky="w")

    # Spinbox for "Number of books"
    num_books_label = ttk.Label(series_frame, text="Number of books:")
    num_books_label.grid(row=1, column=0, sticky="w")
    
    num_books_var = tk.IntVar(value=1)
    num_books_spin = tk.Spinbox(series_frame, from_=1, to=100, textvariable=num_books_var, width=5)
    num_books_spin.grid(row=1, column=1, sticky="w")
    
    # Create a frame for the "Book Size" section
    bsize_frame = ttk.LabelFrame(root, text="Book Size", padding=(20, 10))
    bsize_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
    
    # Dropdown for "Book Size"
    bsize_label = ttk.Label(bsize_frame, text="Book Size:")
    bsize_label.grid(row=0, column=0, sticky="w")
    
    bsize_authors = ["Small", "Medium", "Large", "REALLY LARGE", "WTF"]
    bsize_var = tk.StringVar()
    bsize_dropdown = ttk.Combobox(bsize_frame, textvariable=bsize_var, values=bsize_authors)
    bsize_dropdown.grid(row=0, column=1, sticky="ew")
    bsize_dropdown.set("Select a size")

    # Create a frame for the "Sub-Plots Per-Book" section
    sPlots_frame = ttk.LabelFrame(root, text="Sub-Plots Per-Book", padding=(20, 10))
    sPlots_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
    
    # Spinbox for "sub plots"
    sPlots_label = ttk.Label(sPlots_frame, text="Sub-Plots:")
    sPlots_label.grid(row=0, column=0, sticky="w")
    
    sPlots_var = tk.IntVar(value=1)
    sPlots_spin = tk.Spinbox(sPlots_frame, from_=1, to=100, textvariable=sPlots_var, width=5)
    sPlots_spin.grid(row=0, column=1, sticky="w")

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

