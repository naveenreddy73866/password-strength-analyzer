import argparse
from zxcvbn import zxcvbn
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# ---------------- Password Analysis ---------------- #
def analyze_password(password):
    """Analyze the strength of a given password using zxcvbn."""
    result = zxcvbn(password)
    return {
        "score": result["score"],
        "feedback": result["feedback"],
        "crack_time": result["crack_times_display"]
    }

# ---------------- Wordlist Generator ---------------- #
def generate_wordlist(inputs):
    """Generate a custom wordlist based on user inputs with common patterns."""
    patterns = []

    for word in inputs:
        word = word.strip()
        patterns.extend([
            word,
            word.capitalize(),
            word + "123",
            word[::-1],
            word + "2025",
            word.replace('a', '@').replace('s', '$').replace('o', '0').replace('e', '3')
        ])

    return list(set(patterns))  # Remove duplicates

# ---------------- Export Function ---------------- #
def export_wordlist(wordlist, filename="custom_wordlist.txt"):
    """Export the generated wordlist to a .txt file."""
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + "\n")
    print(f"Wordlist exported to {filename}")

# ---------------- CLI Mode ---------------- #
def cli_mode():
    """Run the tool in CLI mode using argparse."""
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("-p", "--password", help="Password to analyze")
    parser.add_argument("-i", "--inputs", nargs='+', help="Custom inputs for wordlist generation")
    parser.add_argument("-o", "--output", default="custom_wordlist.txt", help="Output filename")

    args = parser.parse_args()

    if args.password:
        result = analyze_password(args.password)
        print("\nPassword Strength Analysis")
        print("Score:", result["score"])
        print("Feedback:", result["feedback"])
        print("Crack Times:", result["crack_time"])

    if args.inputs:
        wordlist = generate_wordlist(args.inputs)
        export_wordlist(wordlist, args.output)

# ---------------- GUI Mode ---------------- #
def gui_mode():
    """Run the tool in GUI mode using tkinter."""
    def on_analyze():
        password = pw_entry.get()
        result = analyze_password(password)
        time = result['crack_time']['offline_fast_hashing_1e10_per_second']
        analysis_result.set(f"Score: {result['score']}, Crack Time: {time}")

    def on_generate():
        inputs = [x.strip() for x in input_entry.get().split(',') if x.strip()]
        if not inputs:
            messagebox.showwarning("Input Error", "Please enter at least one input.")
            return

        wordlist = generate_wordlist(inputs)
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Wordlist As"
        )
        if filename:
            export_wordlist(wordlist, filename)
            messagebox.showinfo("Success", f"Wordlist saved to {filename}")

    # GUI Window Setup
    root = tk.Tk()
    root.title("Password Analyzer & Wordlist Generator")
    root.geometry("500x300")

    tk.Label(root, text="Enter Password:").pack(pady=5)
    pw_entry = tk.Entry(root, width=40)
    pw_entry.pack()

    tk.Button(root, text="Analyze Password", command=on_analyze).pack(pady=5)
    analysis_result = tk.StringVar()
    tk.Label(root, textvariable=analysis_result).pack(pady=5)

    tk.Label(root, text="Enter Custom Inputs (comma separated):").pack(pady=5)
    input_entry = tk.Entry(root, width=40)
    input_entry.pack()

    tk.Button(root, text="Generate Wordlist", command=on_generate).pack(pady=10)

    root.mainloop()

# ---------------- Main Execution ---------------- #
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        cli_mode()
    else:
        gui_mode()
