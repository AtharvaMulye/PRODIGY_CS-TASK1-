import tkinter as tk
def caesar_cipher(text, shift, decrypt=False):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text.lower():
        if char in alpha:
            idx = alpha.find(char)
            new_idx = (idx + shift) % 26 if not decrypt else (idx - shift) % 26
            new_char = alpha[new_idx]
        else:
            new_char = char
        result += new_char
    return result

def encrypt():
    plaintext = plaintext_entry.get()
    shift_key = int(shift_entry.get()) 
    encrypted_text = caesar_cipher(plaintext, shift_key)
    encrypted_text_entry.delete(0, tk.END)
    encrypted_text_entry.insert(0, encrypted_text)

def decrypt():
    encrypted_text = encrypted_text_entry.get()
    shift_key = int(shift_entry.get())
    decrypted_text = caesar_cipher(encrypted_text, shift_key, decrypt=True)
    plaintext_entry.delete(0, tk.END) 
    plaintext_entry.insert(0, decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

input_frame = tk.LabelFrame(root, text="Text")
input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

plaintext_label = tk.Label(input_frame, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)
plaintext_entry = tk.Entry(input_frame)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

encrypted_text_label = tk.Label(input_frame, text="Encrypted Text:")
encrypted_text_label.grid(row=1, column=0, padx=5, pady=5)
encrypted_text_entry = tk.Entry(input_frame)
encrypted_text_entry.grid(row=1, column=1, padx=5, pady=5)

controls_frame = tk.LabelFrame(root, text="Controls")
controls_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

shift_label = tk.Label(controls_frame, text="Shift Key:")
shift_label.grid(row=0, column=0, padx=5, pady=5)
shift_entry = tk.Entry(controls_frame)
shift_entry.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = tk.Button(controls_frame, text="Encrypt", command=encrypt, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
encrypt_button.grid(row=1, column=0, padx=5, pady=5)

decrypt_button = tk.Button(controls_frame, text="Decrypt", command=decrypt, bg="#FF5722", fg="white", font=("Arial", 10, "bold"))
decrypt_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()