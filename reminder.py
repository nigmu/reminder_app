import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import datetime
import webbrowser

# Import functions from the graph module
import graph

class DSAReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA and Aptitude Reminder App")

        # Main frame
        self.main_frame = ttk.Frame(root, padding="20", style='MainFrame.TFrame')
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Label for the number of DSA problems solved
        self.problems_label_dsa = ttk.Label(self.main_frame, text="Number of DSA problems solved today:", style='Label.TLabel')
        self.problems_label_dsa.grid(row=0, column=0, pady=10, padx=10)

        # Frame to hold the DSA counter components
        self.counter_frame_dsa = ttk.Frame(self.main_frame, style='CounterFrame.TFrame')
        self.counter_frame_dsa.grid(row=1, column=0, pady=10, padx=10)

        # Decrement button for DSA
        self.decrement_button_dsa = tk.Button(self.counter_frame_dsa, text="-", command=self.decrement_counter_dsa, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 16), width=10, height=1)
        self.decrement_button_dsa.grid(row=0, column=0, padx=5)

        # Variable to hold the DSA counter value
        self.counter_var_dsa = tk.IntVar(value=0)
        # Label to display the DSA counter value
        self.counter_display_dsa = ttk.Label(self.counter_frame_dsa, textvariable=self.counter_var_dsa, style='CounterDisplay.TLabel')
        self.counter_display_dsa.grid(row=0, column=1, padx=5)

        # Increment button for DSA
        self.increment_button_dsa = tk.Button(self.counter_frame_dsa, text="+", command=self.increment_counter_dsa, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 16), width=10, height=1)
        self.increment_button_dsa.grid(row=0, column=2, padx=5)

        # Label for the number of Aptitude problems solved
        self.problems_label_aptitude = ttk.Label(self.main_frame, text="Number of Aptitude problems solved today:", style='Label.TLabel')
        self.problems_label_aptitude.grid(row=2, column=0, pady=10, padx=10)

        # Frame to hold the Aptitude counter components
        self.counter_frame_aptitude = ttk.Frame(self.main_frame, style='CounterFrame.TFrame')
        self.counter_frame_aptitude.grid(row=3, column=0, pady=10, padx=10)

        # Decrement button for Aptitude
        self.decrement_button_aptitude = tk.Button(self.counter_frame_aptitude, text="-", command=self.decrement_counter_aptitude, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 16), width=10, height=1)
        self.decrement_button_aptitude.grid(row=0, column=0, padx=5)

        # Variable to hold the Aptitude counter value
        self.counter_var_aptitude = tk.IntVar(value=0)
        # Label to display the Aptitude counter value
        self.counter_display_aptitude = ttk.Label(self.counter_frame_aptitude, textvariable=self.counter_var_aptitude, style='CounterDisplay.TLabel')
        self.counter_display_aptitude.grid(row=0, column=1, padx=5)

        # Increment button for Aptitude
        self.increment_button_aptitude = tk.Button(self.counter_frame_aptitude, text="+", command=self.increment_counter_aptitude, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 16), width=10, height=1)
        self.increment_button_aptitude.grid(row=0, column=2, padx=5)

        # Proceed button
        self.proceed_button = tk.Button(self.main_frame, text="Save", command=self.ask_more_problems, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 20, "bold"), width=10, height=1)
        self.proceed_button.grid(row=4, column=0, pady=20, padx=10)

        # Show in Graph button
        self.show_graph_button = tk.Button(self.main_frame, text="Show in Graph", command=self.show_graph, bg='#3F72AF', fg='#F9F7F7', font=("Helvetica", 20, "bold"), width=15, height=1)
        self.show_graph_button.grid(row=5, column=0, pady=20, padx=10)

        # Configure styles
        self.style = ttk.Style()
        self.style.configure('MainFrame.TFrame', background="#112D4E")
        self.style.configure('CounterFrame.TFrame', background="#112D4E")
        self.style.configure('Label.TLabel', background="#112D4E", foreground="#F9F7F7", font=("Helvetica", 26, "bold"))
        self.style.configure('CounterDisplay.TLabel', background="#112D4E", foreground="#F9F7F7", font=("Helvetica", 20))

    def increment_counter_dsa(self):
        """Increment the DSA counter value."""
        self.counter_var_dsa.set(self.counter_var_dsa.get() + 1)

    def decrement_counter_dsa(self):
        """Decrement the DSA counter value, ensuring it does not go below zero."""
        if self.counter_var_dsa.get() > 0:
            self.counter_var_dsa.set(self.counter_var_dsa.get() - 1)

    def increment_counter_aptitude(self):
        """Increment the Aptitude counter value."""
        self.counter_var_aptitude.set(self.counter_var_aptitude.get() + 1)

    def decrement_counter_aptitude(self):
        """Decrement the Aptitude counter value, ensuring it does not go below zero."""
        if self.counter_var_aptitude.get() > 0:
            self.counter_var_aptitude.set(self.counter_var_aptitude.get() - 1)

    def ask_more_problems(self):
        """Ask if the user wants to solve more problems."""
        num_problems_solved_dsa = self.counter_var_dsa.get()
        num_problems_solved_aptitude = self.counter_var_aptitude.get()
        answer = messagebox.askyesno("Solve More Problems", "Do you want to solve more problems?")
        if answer:
            self.open_website("https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2")
        else:
            self.save_and_close()

    def open_website(self, url):
        """Open the specified website."""
        webbrowser.open(url)

    def save_and_close(self):
        """Save the user's response and close the application."""
        num_problems_solved_dsa = self.counter_var_dsa.get()
        num_problems_solved_aptitude = self.counter_var_aptitude.get()
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the response to the CSV file
        with open("dsa_responses.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date_time, num_problems_solved_dsa, num_problems_solved_aptitude])

        self.root.quit()  # Close the application

    def show_graph(self):
        df = graph.header()
        graph.graph(df)

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = DSAReminderApp(root)
    root.mainloop()
