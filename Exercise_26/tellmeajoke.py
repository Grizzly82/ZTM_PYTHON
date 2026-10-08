# Using the tkinter library to check the Tk version
import tkinter as tk
# This script prints all jokes available from the pyjokes library.
import pyjokes

# Create the main window
root = tk.Tk()
root.title("Joke Generator")

# Display the Tk version
print("Tk version:", tk.TkVersion)
# Add a label to the window
label = tk.Label(root, text="Welcome to the Joke Generator!")
label.pack(pady=20)
root.configure(background="grey")
root.minsize(500, 500)
root.maxsize(900, 500)
root.geometry("300x300+50+50")


#print out jokes in the Tkinter window
# Create a frame to hold the jokes
jokes_frame = tk.Frame(root)
jokes_frame.pack()

#add a button the generates one joke at a time
# Function to generate a joke and display it in the jokes frame
# add textbox to display jokes
# display jokes one at a time
#add padding to the jokes frame
# add spacing between the jokes and the button

def generate_joke():
    jokes_textbox.delete(1.0, tk.END)
    joke = pyjokes.get_joke()
    #Font style for the joke text
    jokes_textbox.tag_configure("center", justify="center")
    jokes_textbox.tag_configure("bold", font=("Helvetica", 18, "bold"))
    jokes_textbox.insert(tk.END, joke + "\n", "center")
    jokes_textbox.tag_add("bold", "1.0", "end")
    jokes_textbox.see(tk.END)
    return joke

#center the text in the textbox to the center of frame
jokes_textbox = tk.Text(jokes_frame, wrap="word", height=10, width=100)
jokes_frame.configure(padx=20, pady=20,highlightbackground="black",highlightthickness=1)
jokes_textbox.pack()

button = tk.Button(root, text="Generate Joke", command=generate_joke)
button.pack(pady=20)
# Add jokes to the frame (currently commented out)

##for joke in pyjokes.get_jokes():
  ##tk.Label(jokes_frame, text=joke).pack()

#tk.Label(jokes_frame, text="That's all the jokes I have!").pack()


# Start the Tkinter main loop
root.mainloop()