# 🔐 Caesar Cipher Encryption Tool

I built this modern **Caesar Cipher Encryption Tool** with **Python and Tkinter**. You can use it to transform text with the classical Caesar Cipher technique and switch easily between encryption and decryption.

---

## 📌 Project Overview

The **Caesar Cipher Encryption Tool** is a desktop cryptography application. It demonstrates one of the simplest and best-known substitution cipher techniques.

The application allows users to:

* Enter text to encrypt or decrypt
* Select a custom shift value
* Encrypt messages using the Caesar Cipher
* Decrypt previously encrypted messages
* Preserve spaces, numbers, and special characters
* Copy results easily
* Clear input and output
* Use a clean and modern graphical interface

I developed this project as part of a **Python/Cybersecurity internship project**. It helped me understand the fundamentals of classical cryptography and encryption techniques.

---

## ✨ Features

### 🔒 Encryption

You can convert plaintext into encrypted text with a shift value that you select.

### 🔓 Decryption

You can convert encrypted text back into readable plaintext with the reverse shift.

### 🔢 Custom Shift Value

You can choose your own shift value instead of using a fixed value.

### 🖥️ Modern GUI

I built the desktop interface with **Tkinter** so you can use the tool easily.

### 🔤 Character Preservation

The application handles:

* Uppercase letters
* Lowercase letters
* Spaces
* Numbers
* Special characters

The tool keeps non-alphabetic characters unchanged.

### 📋 Copy Result

You can easily copy the encrypted or decrypted result.

### 🧹 Clear Function

You can clear the input, output, and selected values with one action.

### ⚠️ Input Validation

The application validates your input and shows appropriate messages when required information is missing or invalid.

---

## 🧠 How Caesar Cipher Works

The Caesar Cipher is a **substitution cipher**. It shifts each plaintext letter by a fixed number of positions in the alphabet.

For example, with a shift value of **3**:

```text
A → D
B → E
C → F
D → G
```

Therefore:

```text
HELLO
```

becomes:

```text
KHOOR
```

### Encryption Formula

For a letter represented by its alphabet position:

```text
E(x) = (x + k) mod 26
```

Where:

* `x` = position of the original character
* `k` = shift value
* `26` = number of letters in the English alphabet

### Decryption Formula

```text
D(x) = (x - k) mod 26
```

Decryption reverses the shift used during encryption.

---

## 🛠️ Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Core programming language |
| Tkinter            | Graphical User Interface  |
| String Operations  | Text processing           |
| Modular Arithmetic | Cipher calculations       |

---

## 📂 Project Structure

```text
Caesar-Cipher-Encryption-Tool/
│
├── caesar.py
├── README.md
└── screenshots/
    ├── home.png
    ├── encryption.png
    └── decryption.png
```

> The exact file structure may vary depending on the final version of the project.

---

## 🚀 Getting Started

### Prerequisites

You need Python installed on your computer before you run the project.

Check your Python installation:

```bash
python --version
```

or:

```bash
py --version
```

Most standard Python installations on Windows include Tkinter.

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Caesar-Cipher-Encryption-Tool.git
```

### 2. Open the project folder

```bash
cd Caesar-Cipher-Encryption-Tool
```

### 3. Run the application

```bash
python caesar.py
```

On Windows, you can also use:

```bash
py caesar.py
```

---

## 💻 How to Use

### Step 1 — Enter Text

Enter the message you want to encrypt or decrypt.

Example:

```text
HELLO WORLD
```

### Step 2 — Enter Shift Value

Enter the number of positions by which the letters should be shifted.

Example:

```text
3
```

### Step 3 — Choose an Operation

Select either:

* **Encrypt**
* **Decrypt**

### Step 4 — View the Result

The application processes your text and displays the result in the output section.

For example:

```text
Input:
HELLO WORLD

Shift:
3

Encrypted:
KHOOR ZRUOG
```

---

## 🖼️ Screenshots

### Main Interface

Add your application screenshot here:

```text
screenshots/home.png
```

### Encryption

Add an encryption screenshot here:

```text
screenshots/encryption.png
```

### Decryption

Add a decryption screenshot here:

```text
screenshots/decryption.png
```

You can display the screenshots on GitHub using:

```markdown
![Main Interface](screenshots/home.png)
```

---

## 🔐 Security Note

The Caesar Cipher is a **classical educational cipher** and should **not be used for protecting real passwords, confidential information, or sensitive data**.

Because there are only a limited number of possible shifts, Caesar Cipher encryption can be easily broken using brute-force techniques.

This project is intended for:

* Learning cryptography fundamentals
* Understanding substitution ciphers
* Practicing Python programming
* Learning GUI development with Tkinter
* Demonstrating basic encryption concepts

---

## 🎯 Learning Objectives

I practiced the following concepts while building this project:

* Python programming
* Functions and conditional statements
* String manipulation
* Loops
* Modular arithmetic
* Character encoding concepts
* Basic cryptography
* GUI development with Tkinter
* Input validation
* Event-driven programming
* Project organization

---

## 🔮 Future Improvements

I could extend the project with these features in the future:

* Add multiple cipher algorithms
* Add ROT13 encryption
* Add Vigenère Cipher
* Add automatic brute-force Caesar Cipher analysis
* Add file encryption/decryption
* Add dark/light theme switching
* Add encryption history
* Add export/save functionality
* Improve accessibility
* Add unit tests
* Package the application as a standalone executable

---

## 📚 Project Purpose

This project shows how I can implement a classical encryption algorithm as a functional desktop application.

It combines **cryptography concepts, Python programming, and GUI development** in one beginner-friendly project.

---

## 👩‍💻 Author

**Nagma Sorathiya**

Diploma in Computer Engineering

### Skills Demonstrated

* Python
* Tkinter
* HTML/CSS/JavaScript
* Django
* SQL
* Git & GitHub

---

## ⭐ Support

If you find this project useful for learning, you can **star ⭐ the repository**.

---

## 📄 License

I created this project for educational and learning purposes.
