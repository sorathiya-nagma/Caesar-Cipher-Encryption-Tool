import tkinter as tk
from tkinter import messagebox


# ============================================================
# CAESAR CIPHER ALGORITHM
# ============================================================

def caesar_cipher(text, shift):
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    Encryption:
        shift = positive number

    Decryption:
        shift = negative number
    """

    result = ""

    for char in text:

        # Uppercase letters
        if char.isupper():

            new_char = chr(
                (ord(char) - ord("A") + shift) % 26
                + ord("A")
            )

            result += new_char

        # Lowercase letters
        elif char.islower():

            new_char = chr(
                (ord(char) - ord("a") + shift) % 26
                + ord("a")
            )

            result += new_char

        # Keep spaces, numbers and symbols unchanged
        else:
            result += char

    return result


# ============================================================
# MAIN APPLICATION
# ============================================================

class CaesarCipherApp:

    def __init__(self, root):

        self.root = root

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.root.title(
            "Caesar Cipher | Encryption & Decryption Tool"
        )

        self.root.geometry(
            "1150x780"
        )

        self.root.minsize(
            900,
            600
        )

        self.root.configure(
            bg="#F8EDEE"
        )

        # ----------------------------------------------------
        # COLORS
        # ----------------------------------------------------

        self.BG = "#F8EDEE"
        self.WHITE = "#FFFFFF"

        self.DARK = "#5A1025"
        self.TEXT = "#3B0A18"
        self.MUTED = "#7A4A59"

        self.BLUE = "#7A1F3D"
        self.BLUE_DARK = "#5A1025"
        self.BLUE_LIGHT = "#F8E7EB"

        self.GREEN = "#8B2948"
        self.GREEN_DARK = "#6B1733"
        self.GREEN_LIGHT = "#F7E8EC"

        self.BORDER = "#E5C5CC"
        self.INPUT_BG = "#FCF5F6"
        # ----------------------------------------------------
        # VARIABLES
        # ----------------------------------------------------

        self.shift_var = tk.StringVar(
            value="3"
        )

        self.encrypt_count = tk.StringVar(
            value="0 characters"
        )

        self.decrypt_count = tk.StringVar(
            value="0 characters"
        )

        self.status_var = tk.StringVar(
            value="Ready — enter text to begin."
        )

        # ----------------------------------------------------
        # BUILD INTERFACE
        # ----------------------------------------------------

        self.create_header()

        self.create_scrollable_area()

        self.create_footer()
            # ========================================================
    # FOOTER
    # ========================================================

    def create_footer(self):

        footer = tk.Frame(
            self.root,
            bg=self.WHITE,
            height=42,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        footer.pack(
            fill="x",
            side="bottom"
        )

        footer.pack_propagate(False)

        tk.Label(
            footer,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="left",
            padx=30,
            pady=10
        )

        tk.Label(
            footer,
            text="Caesar Cipher • Educational Encryption Tool",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="right",
            padx=30,
            pady=10
        )

        # ----------------------------------------------------
        # MOUSE WHEEL
        # ----------------------------------------------------

        self.root.bind_all(
            "<MouseWheel>",
            self.on_mousewheel
        )

        # Linux mouse wheel support
        self.root.bind_all(
            "<Button-4>",
            self.on_mousewheel_linux
        )

        self.root.bind_all(
            "<Button-5>",
            self.on_mousewheel_linux
        )

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.DARK,
            height=105
        )

        header.pack(
            fill="x",
            side="top"
        )

        header.pack_propagate(False)

        # Main header content
        header_content = tk.Frame(
            header,
            bg=self.DARK
        )

        header_content.pack(
            fill="both",
            expand=True,
            padx=40
        )

        # Logo
        tk.Label(
            header_content,
            text="🔐",
            font=("Segoe UI Emoji", 30),
            bg=self.DARK,
            fg="white"
        ).pack(
            side="left",
            padx=(0, 15)
        )

        # Title area
        title_area = tk.Frame(
            header_content,
            bg=self.DARK
        )

        title_area.pack(
            side="left",
            pady=20
        )

        tk.Label(
            title_area,
            text="Caesar Cipher",
            font=("Segoe UI", 25, "bold"),
            bg=self.DARK,
            fg="white"
        ).pack(
            anchor="w"
        )

        tk.Label(
            title_area,
            text="Encryption & Decryption Tool",
            font=("Segoe UI", 10),
            bg=self.DARK,
            fg="#CBD5E1"
        ).pack(
            anchor="w"
        )

        # Status
        status_area = tk.Frame(
            header_content,
            bg=self.DARK
        )

        status_area.pack(
            side="right"
        )

        tk.Label(
            status_area,
            text="●",
            font=("Segoe UI", 14),
            bg=self.DARK,
            fg="#22C55E"
        ).pack(
            side="left"
        )

        tk.Label(
            status_area,
            text=" Ready",
            font=("Segoe UI", 10),
            bg=self.DARK,
            fg="#CBD5E1"
        ).pack(
            side="left"
        )

    # ========================================================
    # SCROLLABLE AREA
    # ========================================================

    def create_scrollable_area(self):

        # Outer frame
        container = tk.Frame(
            self.root,
            bg=self.BG
        )

        container.pack(
            fill="both",
            expand=True
        )

        # Canvas
        self.canvas = tk.Canvas(
            container,
            bg=self.BG,
            highlightthickness=0,
            bd=0
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Scrollbar
        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        # Scrollable frame
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg=self.BG
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )

        # Update scroll region
        self.scrollable_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        # Make frame width equal to canvas width
        self.canvas.bind(
            "<Configure>",
            self.resize_scrollable_frame
        )

        # Build content
        self.create_main_content()

    # ========================================================
    # SCROLL HELPERS
    # ========================================================

    def update_scroll_region(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def resize_scrollable_frame(self, event):

        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )

    def on_mousewheel(self, event):

        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    def on_mousewheel_linux(self, event):

        if event.num == 4:

            self.canvas.yview_scroll(
                -1,
                "units"
            )

        elif event.num == 5:

            self.canvas.yview_scroll(
                1,
                "units"
            )

    # ========================================================
    # MAIN CONTENT
    # ========================================================

    def create_main_content(self):

        main = tk.Frame(
            self.scrollable_frame,
            bg=self.BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        # ----------------------------------------------------
        # INTRODUCTION
        # ----------------------------------------------------

        tk.Label(
            main,
            text="Encrypt and decrypt your messages",
            font=("Segoe UI", 18, "bold"),
            bg=self.BG,
            fg=self.DARK
        ).pack(
            anchor="w"
        )

        tk.Label(
            main,
            text=(
                "Use the Caesar Cipher to shift letters by a selected key. "
                "Enter plaintext for encryption or ciphertext for decryption."
            ),
            font=("Segoe UI", 10),
            bg=self.BG,
            fg=self.MUTED
        ).pack(
            anchor="w",
            pady=(5, 25)
        )

        # ----------------------------------------------------
        # INPUT SECTION
        # ----------------------------------------------------

        input_area = tk.Frame(
            main,
            bg=self.BG
        )

        input_area.pack(
            fill="x"
        )

        input_area.grid_columnconfigure(
            0,
            weight=1
        )

        input_area.grid_columnconfigure(
            1,
            weight=1
        )

        self.create_encrypt_card(
            input_area
        )

        self.create_decrypt_card(
            input_area
        )

        # ----------------------------------------------------
        # KEY SETTINGS
        # ----------------------------------------------------

        self.create_settings(
            main
        )

        # ----------------------------------------------------
        # OUTPUT SECTION
        # ----------------------------------------------------

        self.create_output_section(
            main
        )

        # ----------------------------------------------------
        # HOW IT WORKS
        # ----------------------------------------------------

        self.create_info_section(
            main
        )

        # ----------------------------------------------------
        # CLEAR BUTTON
        # ----------------------------------------------------

        clear_frame = tk.Frame(
            main,
            bg=self.BG
        )

        clear_frame.pack(
            fill="x",
            pady=(20, 5)
        )

        tk.Button(
            clear_frame,
            text="↻  Clear All",
            command=self.clear_all,
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.TEXT,
            activebackground="#E2E8F0",
            activeforeground=self.TEXT,
            relief="flat",
            highlightbackground=self.BORDER,
            highlightthickness=1,
            padx=25,
            pady=9,
            cursor="hand2"
        ).pack(
            side="right"
        )

    # ========================================================
    # ENCRYPT CARD
    # ========================================================

    def create_encrypt_card(self, parent):

        card = tk.Frame(
            parent,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # Header
        header = tk.Frame(
            card,
            bg=self.WHITE
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(18, 5)
        )

        tk.Label(
            header,
            text="🔒  TEXT TO ENCRYPT",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left"
        )

        tk.Label(
            header,
            textvariable=self.encrypt_count,
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="right"
        )

        # Description
        tk.Label(
            card,
            text="Enter normal/plain text here.",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            anchor="w",
            padx=20
        )

        # Input
        self.encrypt_input = tk.Text(
            card,
            height=9,
            wrap="word",
            font=("Consolas", 11),
            bg=self.INPUT_BG,
            fg=self.TEXT,
            insertbackground=self.BLUE,
            relief="flat",
            padx=15,
            pady=14
        )

        self.encrypt_input.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.encrypt_input.bind(
            "<KeyRelease>",
            self.update_encrypt_count
        )

        # Encrypt button
        tk.Button(
            card,
            text="🔒  Encrypt Text",
            command=self.encrypt_text,
            font=("Segoe UI", 10, "bold"),
            bg=self.BLUE,
            fg="white",
            activebackground=self.BLUE_DARK,
            activeforeground="white",
            relief="flat",
            padx=22,
            pady=9,
            cursor="hand2"
        ).pack(
            anchor="e",
            padx=20,
            pady=(0, 20)
        )

    # ========================================================
    # DECRYPT CARD
    # ========================================================

    def create_decrypt_card(self, parent):

        card = tk.Frame(
            parent,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        # Header
        header = tk.Frame(
            card,
            bg=self.WHITE
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(18, 5)
        )

        tk.Label(
            header,
            text="🔓  TEXT TO DECRYPT",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left"
        )

        tk.Label(
            header,
            textvariable=self.decrypt_count,
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="right"
        )

        # Description
        tk.Label(
            card,
            text="Enter encrypted/ciphertext here.",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            anchor="w",
            padx=20
        )

        # Input
        self.decrypt_input = tk.Text(
            card,
            height=9,
            wrap="word",
            font=("Consolas", 11),
            bg=self.INPUT_BG,
            fg=self.TEXT,
            insertbackground=self.GREEN,
            relief="flat",
            padx=15,
            pady=14
        )

        self.decrypt_input.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.decrypt_input.bind(
            "<KeyRelease>",
            self.update_decrypt_count
        )

        # Decrypt button
        tk.Button(
            card,
            text="🔓  Decrypt Text",
            command=self.decrypt_text,
            font=("Segoe UI", 10, "bold"),
            bg=self.GREEN,
            fg="white",
            activebackground=self.GREEN_DARK,
            activeforeground="white",
            relief="flat",
            padx=22,
            pady=9,
            cursor="hand2"
        ).pack(
            anchor="e",
            padx=20,
            pady=(0, 20)
        )

    # ========================================================
    # SETTINGS
    # ========================================================

    def create_settings(self, parent):

        card = tk.Frame(
            parent,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=22
        )

        # Left section
        left = tk.Frame(
            card,
            bg=self.WHITE
        )

        left.pack(
            side="left",
            padx=22,
            pady=17
        )

        tk.Label(
            left,
            text="SHIFT / KEY",
            font=("Segoe UI", 11, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            anchor="w"
        )

        tk.Label(
            left,
            text="Number of positions each letter moves",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            anchor="w"
        )

        # Key entry
        key_frame = tk.Frame(
            card,
            bg=self.WHITE
        )

        key_frame.pack(
            side="left",
            padx=10
        )

        self.shift_entry = tk.Entry(
            key_frame,
            textvariable=self.shift_var,
            font=("Segoe UI", 14, "bold"),
            justify="center",
            width=7,
            bg=self.INPUT_BG,
            fg=self.DARK,
            relief="flat"
        )

        self.shift_entry.pack(
            ipady=7
        )

        # Quick keys
        quick_frame = tk.Frame(
            card,
            bg=self.WHITE
        )

        quick_frame.pack(
            side="left",
            padx=15
        )

        tk.Label(
            quick_frame,
            text="Quick:",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="left",
            padx=(0, 8)
        )

        for value in [1, 3, 5, 13]:

            tk.Button(
                quick_frame,
                text=str(value),
                command=lambda v=value: self.set_shift(v),
                font=("Segoe UI", 9, "bold"),
                bg="#F1F5F9",
                fg=self.TEXT,
                activebackground=self.BLUE,
                activeforeground="white",
                relief="flat",
                width=4,
                cursor="hand2"
            ).pack(
                side="left",
                padx=3
            )

        # Example
        tk.Label(
            card,
            text="Example: Key 3 → A becomes D",
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED
        ).pack(
            side="right",
            padx=25
        )

    # ========================================================
    # OUTPUT SECTION
    # ========================================================

    def create_output_section(self, parent):

        tk.Label(
            parent,
            text="Results",
            font=("Segoe UI", 16, "bold"),
            bg=self.BG,
            fg=self.DARK
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        outputs = tk.Frame(
            parent,
            bg=self.BG
        )

        outputs.pack(
            fill="x"
        )

        outputs.grid_columnconfigure(
            0,
            weight=1
        )

        outputs.grid_columnconfigure(
            1,
            weight=1
        )

        # ----------------------------------------------------
        # ENCRYPTED OUTPUT
        # ----------------------------------------------------

        encrypted_card = tk.Frame(
            outputs,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        encrypted_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        header = tk.Frame(
            encrypted_card,
            bg=self.WHITE
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(16, 8)
        )

        tk.Label(
            header,
            text="🔒  ENCRYPTED OUTPUT",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left"
        )

        tk.Button(
            header,
            text="Copy",
            command=self.copy_encrypted,
            font=("Segoe UI", 9),
            bg="#F1F5F9",
            fg=self.TEXT,
            activebackground="#E2E8F0",
            relief="flat",
            padx=12,
            cursor="hand2"
        ).pack(
            side="right"
        )

        self.encrypted_output = tk.Text(
            encrypted_card,
            height=7,
            wrap="word",
            font=("Consolas", 11),
            bg=self.BLUE_LIGHT,
            fg="#F9BBBB",
            relief="flat",
            padx=15,
            pady=14
        )

        self.encrypted_output.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        # ----------------------------------------------------
        # DECRYPTED OUTPUT
        # ----------------------------------------------------

        decrypted_card = tk.Frame(
            outputs,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        decrypted_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        header = tk.Frame(
            decrypted_card,
            bg=self.WHITE
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(16, 8)
        )

        tk.Label(
            header,
            text="🔓  DECRYPTED OUTPUT",
            font=("Segoe UI", 10, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            side="left"
        )

        tk.Button(
            header,
            text="Copy",
            command=self.copy_decrypted,
            font=("Segoe UI", 9),
            bg="#F1F5F9",
            fg=self.TEXT,
            activebackground="#E2E8F0",
            relief="flat",
            padx=12,
            cursor="hand2"
        ).pack(
            side="right"
        )

        self.decrypted_output = tk.Text(
            decrypted_card,
            height=7,
            wrap="word",
            font=("Consolas", 11),
            bg=self.GREEN_LIGHT,
            fg="#065F46",
            relief="flat",
            padx=15,
            pady=14
        )

        self.decrypted_output.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # ========================================================
    # INFORMATION SECTION
    # ========================================================

    def create_info_section(self, parent):

        info = tk.Frame(
            parent,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        info.pack(
            fill="x",
            pady=(25, 0)
        )

        tk.Label(
            info,
            text="💡 How Caesar Cipher Works",
            font=("Segoe UI", 12, "bold"),
            bg=self.WHITE,
            fg=self.DARK
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 7)
        )

        explanation = (
            "Caesar Cipher is a simple substitution encryption technique. "
            "Each letter is shifted forward or backward by a fixed number "
            "of positions in the alphabet. For example, with a key of 3, "
            "A becomes D, B becomes E, and Z wraps around to C. "
            "Decryption reverses the same process by shifting the letters "
            "backward by the selected key."
        )

        tk.Label(
            info,
            text=explanation,
            font=("Segoe UI", 9),
            bg=self.WHITE,
            fg=self.MUTED,
            justify="left",
            wraplength=1000
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 17)
        )

    # ========================================================
    # ENCRYPT
    # ========================================================

    def encrypt_text(self):

        text = self.encrypt_input.get(
            "1.0",
            tk.END
        ).strip()

        if not text:

            messagebox.showwarning(
                "Input Required",
                "Please enter text in the 'Text to Encrypt' box."
            )

            return

        shift = self.get_shift()

        if shift is None:
            return

        encrypted = caesar_cipher(
            text,
            shift
        )

        self.encrypted_output.delete(
            "1.0",
            tk.END
        )

        self.encrypted_output.insert(
            tk.END,
            encrypted
        )

        self.status_var.set(
            f"✓ Encryption completed using key {shift}."
        )

    # ========================================================
    # DECRYPT
    # ========================================================

    def decrypt_text(self):

        text = self.decrypt_input.get(
            "1.0",
            tk.END
        ).strip()

        if not text:

            messagebox.showwarning(
                "Input Required",
                "Please enter encrypted text in the 'Text to Decrypt' box."
            )

            return

        shift = self.get_shift()

        if shift is None:
            return

        decrypted = caesar_cipher(
            text,
            -shift
        )

        self.decrypted_output.delete(
            "1.0",
            tk.END
        )

        self.decrypted_output.insert(
            tk.END,
            decrypted
        )

        self.status_var.set(
            f"✓ Decryption completed using key {shift}."
        )

    # ========================================================
    # GET SHIFT
    # ========================================================

    def get_shift(self):

        try:

            shift = int(
                self.shift_var.get().strip()
            )

            return shift

        except ValueError:

            messagebox.showerror(
                "Invalid Key",
                "Please enter a valid number for the shift key."
            )

            return None

    # ========================================================
    # COPY ENCRYPTED
    # ========================================================

    def copy_encrypted(self):

        text = self.encrypted_output.get(
            "1.0",
            tk.END
        ).strip()

        if not text:

            messagebox.showwarning(
                "Nothing to Copy",
                "There is no encrypted output yet."
            )

            return

        self.root.clipboard_clear()

        self.root.clipboard_append(
            text
        )

        self.status_var.set(
            "✓ Encrypted output copied to clipboard."
        )

    # ========================================================
    # COPY DECRYPTED
    # ========================================================

    def copy_decrypted(self):

        text = self.decrypted_output.get(
            "1.0",
            tk.END
        ).strip()

        if not text:

            messagebox.showwarning(
                "Nothing to Copy",
                "There is no decrypted output yet."
            )

            return

        self.root.clipboard_clear()

        self.root.clipboard_append(
            text
        )

        self.status_var.set(
            "✓ Decrypted output copied to clipboard."
        )

    # ========================================================
    # CHARACTER COUNTERS
    # ========================================================

    def update_encrypt_count(self, event=None):

        text = self.encrypt_input.get(
            "1.0",
            tk.END
        ).rstrip("\n")

        count = len(text)

        self.encrypt_count.set(
            f"{count} character{'s' if count != 1 else ''}"
        )

    def update_decrypt_count(self, event=None):

        text = self.decrypt_input.get(
            "1.0",
            tk.END
        ).rstrip("\n")

        count = len(text)

        self.decrypt_count.set(
            f"{count} character{'s' if count != 1 else ''}"
        )

    # ========================================================
    # QUICK SHIFT
    # ========================================================

    def set_shift(self, value):

        self.shift_var.set(
            str(value)
        )

        self.status_var.set(
            f"Shift key changed to {value}."
        )

    # ========================================================
    # CLEAR ALL
    # ========================================================

    def clear_all(self):

        self.encrypt_input.delete(
            "1.0",
            tk.END
        )

        self.decrypt_input.delete(
            "1.0",
            tk.END
        )

        self.encrypted_output.delete(
            "1.0",
            tk.END
        )

        self.decrypted_output.delete(
            "1.0",
            tk.END
        )

        self.shift_var.set(
            "3"
        )

        self.encrypt_count.set(
            "0 characters"
        )

        self.decrypt_count.set(
            "0 characters"
        )

        self.status_var.set(
            "Ready — all fields cleared."
        )

        # Return to top
        self.canvas.yview_moveto(
            0
        )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CaesarCipherApp(
        root
    )

    root.mainloop()