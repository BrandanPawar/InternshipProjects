import tkinter as tk
from tkinter import scrolledtext
from agent import ask_llm
from mcp_control import execute_command

class MediaAssistantApp:
    def __init__(self, root):
        self.root = root
        root.title("LLM Media Assistant")

        # Input Label
        self.label = tk.Label(root, text="Enter news + command:")
        self.label.pack(pady=5)

        # Input Text Box
        self.input_text = tk.Entry(root, width=80)
        self.input_text.pack(pady=5)
        self.input_text.bind("<Return>", self.process_input)

        # Run Button
        self.run_button = tk.Button(root, text="Run", command=self.process_input)
        self.run_button.pack(pady=5)

        # Output Display (scrollable)
        self.output_box = scrolledtext.ScrolledText(root, width=90, height=20, wrap=tk.WORD)
        self.output_box.pack(padx=10, pady=10)
        self.output_box.config(state=tk.DISABLED)

    def process_input(self, event=None):
        user_input = self.input_text.get().strip()
        if user_input.lower() in ['exit', 'quit']:
            self.root.quit()
            return

        if not user_input:
            return

        self.append_output(f">>> You: {user_input}\n")
        self.input_text.delete(0, tk.END)

        self.append_output("⏳ Thinking...\n")

        # Call LLM
        result = ask_llm(user_input)
        self.append_output(f"🧠 LLM Output: {result}\n")

        # MCP Control Output (capture prints)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        execute_command(result)

        sys.stdout = old_stdout
        mcp_output = mystdout.getvalue()
        self.append_output(mcp_output + "\n" + "-"*40 + "\n")

    def append_output(self, text):
        self.output_box.config(state=tk.NORMAL)
        self.output_box.insert(tk.END, text)
        self.output_box.see(tk.END)
        self.output_box.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = MediaAssistantApp(root)
    root.mainloop()