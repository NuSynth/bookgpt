# bookgpt
This program is intended to guide ChatGPT through prompts to make it write entire novels. Later updates will enable it to make series of novels.

# It will not yet write a good novel
But it does write good templates. This is useful for authors who want to spend less time on thinking of a story. ChatGPT thinks of the story for the author. The author only needs to write the chapters.

Don't check the box for custom number of chapters. It doesn't work right yet. I only left that in the GUI because I dont feel like changing more of the GUI code right now.

In order to run the program, you have to get an API key from OpenAI, and you probably need to setup a virtual environment to run this. I use a virtual environment.

Open a directory that you want the text files to be stored in, and run this in a terminal:

python3 '/path/to/bookGPTgui.py'

using the full path from the root of your system to the python file.

# AUTHOR SYSTEM
If you run the program, you will notice that users can select the story to be designed in the style of one author, while having it write in the style of another. This is to reduce the risk that it will plagiarize a particular author. It's possible that it will design a story pretty closely to a story designed by the author selected for the style of the design, but if a different author is selected for the style of the writing then I think the risk of plagiarization is pretty low. Plus, I have the story idea box, which allows users to provide an idea for the story of their own, which even further decreases the chance of the artificial intelligence performing and plagiarization. So that's what those things are about. Hopefully the works that get produced are as original as can be.

# WARNING ON TOKENS
This warning only applies to the use of this program when the checkbox "Only a template" is not checked.

You have to buy tokens from OpenAI in order to use the program, unless you're using a local model on your hardware. I'm doing what I can to reduce the number of tokens that it uses. I just spent a bunch of money testing this program. Dont blame me if you don't like how many tokens it cost to make a book, or if you didn't have enough tokens for it to finish making a book, or if you don't like the book and your tokens went to waste. I don't like how much it costs, and I'm the one who made the program. The update I gave it to make the chapters bigger made it a lot more expensive per-book. If you want it to make a cheaper book, then just replace the call for make_chapter2 to make_chapter. That makes a way cheaper book, but its way shorter. Another way to reduce the cost is to downgrade which GPT model the program calls. It uses GPT 4 right now, but it might do ok with a weaker GPT model.


# WARNING ON BOOK QUALITY
The current quality of the books it produces is low. But it produces good ideas and templates. Right not it is best to run this with the checkbox ticked for "Only a template." 






# PROJECT GOAL
The goal of this project is to have a program that can output entire novels with the push of a button. It will not be there until large language models can write more consistent material, and follow instructions more precisely.
