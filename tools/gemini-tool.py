# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-generativeai",
#     "rich",
# ]
# ///

"""
USAGE:
    uv run gemini_tool.py "Explain quantum physics"
    
    OR (Interactive Mode):
    uv run gemini_tool.py
"""

import os
import sys
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

# Initialize Rich Console for beautiful output
console = Console()

def get_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        console.print("[bold red]Error:[/bold red] GEMINI_API_KEY not found in environment variables.")
        console.print("Run: [yellow]export GEMINI_API_KEY='your_key_here'[/yellow]")
        sys.exit(1)
    return key

def main():
    genai.configure(api_key=get_key())
    
    # Use the Flash model for speed
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 1. Argument Mode: "uv run gemini_tool.py 'Hello'"
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        with console.status("[bold green]Gemini is thinking...", spinner="dots"):
            response = model.generate_content(prompt)
        
        console.print(Markdown(response.text))
        return

    # 2. Interactive Mode: "uv run gemini_tool.py"
    console.print("[bold blue]Gemini CLI[/bold blue] (Type 'exit' to quit)")
    chat = model.start_chat(history=[])
    
    while True:
        user_input = console.input("[bold green]You > [/bold green]")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        with console.status("[bold green]Thinking...", spinner="dots"):
            response = chat.send_message(user_input)
            
        console.print(Markdown(response.text))
        console.print("-" * 50)

if __name__ == "__main__":
    main()
