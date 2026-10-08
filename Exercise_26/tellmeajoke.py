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
label.pack()
root.configure(background="yellow")
root.minsize(500, 500)
root.maxsize(900, 500)
root.geometry("300x300+50+50")


#print out jokes in the Tkinter window
# Create a frame to hold the jokes
jokes_frame = tk.Frame(root)
jokes_frame.pack()

#add a button the generates one joke at a time
def generate_joke():
    joke = pyjokes.get_joke()
    tk.Label(jokes_frame, text=joke).pack()

button = tk.Button(root, text="Generate Joke", command=generate_joke)
button.pack()  
# Add jokes to the frame (currently commented out)

##for joke in pyjokes.get_jokes():
  ##tk.Label(jokes_frame, text=joke).pack()

#tk.Label(jokes_frame, text="That's all the jokes I have!").pack()


# Start the Tkinter main loop
root.mainloop()