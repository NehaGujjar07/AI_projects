import tkinter as tk
from tkinter import scrolledtext, PhotoImage
import random
import datetime
import time

# ChatBot logic
class ChatBot:
    def __init__(self):
        self.user_memory = {}  # To store user's name if provided
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        # Exit command
        if user_input in ['exit', 'quit']:
            return "Goodbye! Take care.", True
        
        # Pattern matching logic
        if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            return random.choice(["Hello!", "Hi there!", "Hey! How can I help you today?"]), False
        
        elif 'how are you' in user_input:
            return random.choice([
                "I'm just a program, but I'm feeling helpful today!",
                "I'm doing great, thanks for asking! How about you?",
                "I'm here and ready to chat with you!"
            ]), False
        
        elif 'your name' in user_input:
            return "My name is ChatBot. I'm here to chat with you and answer simple questions.", False
        
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            return f"The current time is {current_time}.", False
        
        elif 'date' in user_input:
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            return f"Today's date is {current_date}.", False
        
        elif 'weather' in user_input:
            return "I'm not connected to the internet, but I hope the weather is nice where you are!", False
        
        elif 'name is' in user_input or 'i am' in user_input:
            name = user_input.split('is')[-1] if 'is' in user_input else user_input.split('i am')[-1]
            name = name.strip().capitalize()
            self.user_memory['name'] = name
            return f"Nice to meet you, {name}!", False
        
        elif 'bye' in user_input or 'goodbye' in user_input:
            return random.choice(["Goodbye!", "See you later!", "Take care!"]), True
        
        else:
            return random.choice([
                "I'm not sure I understand that.",
                "Can you rephrase that?",
                "That's interesting, but I don't know how to respond to it.",
                "I'm still learning. Could you try asking in a different way?"
            ]), False


# ChatBot GUI using Tkinter
class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Colorful ChatBot")
        self.root.configure(bg="#E8EEF1")
        
        # Header with title
        self.header_frame = tk.Frame(root, bg="#4A90E2")
        self.header_frame.pack(fill=tk.X)
        
        self.header_label = tk.Label(self.header_frame, text="ChatBot", font=("Arial", 18, "bold"), bg="#4A90E2", fg="white")
        self.header_label.pack(pady=10)
        
        # Chat display with scrollable window
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Helvetica", 12), bg="#F4F6F7", fg="#333333")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.pack(pady=10, padx=10)
        
        # User input entry box
        self.user_input = tk.Entry(root, font=("Helvetica", 14), bg="#F1F1F1", fg="#333333", borderwidth=2)
        self.user_input.pack(pady=10, padx=10, fill=tk.X)
        self.user_input.bind('<Return>', self.send_message)  # Press Enter to send message
        
        # Button frame
        self.button_frame = tk.Frame(root, bg="#F4F6F7")
        self.button_frame.pack()
        
        # Send Button
        self.send_button = tk.Button(self.button_frame, text="Send", font=("Arial", 12, 'bold'), bg="#4CAF50", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Clear Chat Button
        self.clear_button = tk.Button(self.button_frame, text="Clear Chat", font=("Arial", 12, 'bold'), bg="#F39C12", fg="white", command=self.clear_chat)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Exit Button
        self.exit_button = tk.Button(self.button_frame, text="Exit", font=("Arial", 12, 'bold'), bg="#E74C3C", fg="white", command=root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.chatbot = ChatBot()
    
    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        
        if user_message == "":
            return  # Do not process empty messages
        
        self.display_message("You", user_message, "#D1E7DD")  # User message (green)
        self.user_input.delete(0, tk.END)  # Clear input box
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "ChatBot is typing...\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
        self.root.after(1000, lambda: self.generate_response(user_message))
    
    def generate_response(self, user_message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete('end-2l', 'end-1l')
        self.chat_display.config(state=tk.DISABLED)
        
        bot_response, should_exit = self.chatbot.get_response(user_message)
        self.display_message("ChatBot", bot_response, "#FFD6D6")  # Bot message (red)
        
        if should_exit:
            self.root.quit()
    
    def display_message(self, sender, message, bg_color):
        self.chat_display.config(state=tk.NORMAL)
        time_stamp = datetime.datetime.now().strftime('%H:%M:%S')
        
        self.chat_display.insert(tk.END, f"{sender} ({time_stamp}):\n", 'bold')
        self.chat_display.insert(tk.END, f"  {message}  \n", 'message')
        
        self.chat_display.tag_configure('bold', font=('Helvetica', 10, 'bold'))
        self.chat_display.tag_configure('message', background=bg_color, foreground="#333333", font=('Helvetica', 12), borderwidth=5)
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)  # Auto-scroll to the bottom
    
    def clear_chat(self):
        """Clears the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)
    root.mainloop()
