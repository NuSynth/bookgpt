If you are on Windows, then the Windows 11 instructions should be read first.



You need to have keys for openAI and Google Gemini in order to use this program. Using this program costs tokens for openAI and Google Gemini. In total; I pay between 2 to 3 dollars per book. But the chapters all get written out without me doing any work, so I see it as worth it.

These instructions will soon be updated for getting an API key for Grok. Right now the program is not set up to use Grok, but it will be.


Google Gemini API key:

1. Go to Google AI Studio
Google provides API keys for Gemini through Google AI Studio.

👉 Visit: https://aistudio.google.com

You’ll need to be signed in with a Google account.




2. Create a New API Key
Once you're in AI Studio:

Click “Get API key” or open the API Keys section from the left sidebar near the bottom.

Select “Create API key” near the top right side.

Choose a project (or create a new one if prompted).

Google will generate an API key for you.

Under the section that says "Key" there should be random letters that are clickable. Click that.

A section opens up with information. Under the section that says API Key, highlight that and copy it.


3. Right click the bookGPT file labeled "promptFunctions" to open the right-click menu.

Select the option that says: Edit with Notepad.


Near the top of the file are these two sections:


# Replace 'YOUR_API_KEY' with your actual key
#For google Gemini
client_gemini = genai.Client(api_key="YOUR_API_KEY_HERE")

#For ChatGPT
client_gpt = OpenAI(
  api_key = "YOUR_API_KEY_HERE",
)



4) For this line: client_gemini = genai.Client(api_key="YOUR_API_KEY_HERE")

Highlight the text YOUR_API_KEY_HERE. Make sure the quotation marks are not highlighted, but be sure all of the text within the quotation marks are highlighted.

Right-click the highlited text to bring up the right click menu, and click paste.


You should now have the API key for Google Gemini pasted there. Make sure you set up your payment method so that google Gemini can be used.
On the left side of of the web page for Google AI Studio, there is a billing section. Setup your billing in that section. It is pay as you go. 






OpenAI API Key:

1. Go to the OpenAI Platform Dashboard
👉 https://platform.openai.com

Sign in if you aren’t already.

2. Open the API Keys Page (New Location)
Select API keys on the left side bar.

3. Click “Create new secret key” near the top right.

A thing will pop up title "Save your key" 

Your key should already be highlighted.

Right-click the highlighted text and select copy from the right-click menu.


Go back to the "promptFunctions file that should still be open in your Notepad program.



For this section:

#For ChatGPT
client_gpt = OpenAI(
  api_key = "YOUR_API_KEY_HERE",
)


Highlight the text: YOUR_API_KEY_HERE

Right click the highlighted text.

Select paste from the right-click menu.


At the top of the Notepad program, select File.

Select Save.

Exit Notepad.


4) Setting up billing:

Next to your profile icon in the OpenAI web page, select the cogwheel icon.

On the left panel, there is a section that says billing. Go to that.

You can upload a set amount of money. Whatever you want. The books are all very cheap to be made. You can upload 10 dollars and keep making them until the funds run out if you want.




