🔐 Password Strength Checker

A modern, smart desktop application to evaluate the strength of passwords using regex-based logic and real-time visual feedback. Developed as part of a Cybersecurity & Ethical Hacking Internship, this project demonstrates secure input validation, intuitive user interface design, and offline-ready deployment with .exe packaging.


---

📘 Overview

Weak passwords are one of the most common vulnerabilities exploited in cyberattacks. This tool is designed to analyze the strength of user-entered passwords using a score-based system. It provides categorized feedback (Weak, Medium, Strong) and helpful suggestions to improve password security. Built with Python and Tkinter, it also includes a modern interface, dark/light themes, and utility options like copy and clear.


---

🚀 Features

✔️ Regex-based strength evaluation (length, digits, case, symbols)

✔️ Desktop GUI with modern layout

✔️ Toggle eye icon for password visibility

✔️ Real-time feedback and suggestions

✔️ Copy password to clipboard with one click

✔️ Clear input and reset results

✔️ Dual theme support – Light & Dark

✔️ .exe-ready for offline execution



---

🧠 Password Strength Logic

The tool uses a scoring algorithm based on:

Length of password

Presence of uppercase letters

Presence of lowercase letters

Inclusion of digits

Use of special characters


🔍 Output:

Weak → Red badge

Medium → Orange badge

Strong → Green badge



---

🛠️ Technologies Used

Purpose	Tools / Libraries Used

Programming	Python 3.12
Regex Evaluation	re
GUI Development	Tkinter
Icon Rendering	Pillow (PIL)
Clipboard Support	Pyperclip
App Packaging	PyInstaller



---

📁 Folder Structure

Password_Strength_Checker/
├── password_checker.py         # Main script
├── eye_open.png                # Show password icon
├── eye_closed.png              # Hide password icon
├── password_icon.ico           # Application icon for exe
├── README.md                   # Project documentation


---

📄 Project Documentation

📘 This project was completed under a Cybersecurity & Ethical Hacking Internship and includes full source code, GUI assets, and packaging instructions. You can find the full PDF report here:

👉 Download PDF Report(https://drive.google.com/file/d/16gTJ5rV8MfyISi1Gtkbwp2z83cekTN-y/view?usp=sharing)


---

🖥️ How to Use

1. Open the application via Python or run the .exe


2. Enter a password in the input field


3. View its strength classification


4. Apply suggestions to strengthen it


5. Use copy/clear/theme toggle as needed




---

📦 Create Executable

To convert the script into an offline .exe (link):(https://drive.google.com/file/d/1rHRtP02XzL-JG_UHJAwTGP6nUfCX7Qo9/view?usp=sharing)

pyinstaller --onefile --windowed --icon=password_icon.ico password_checker.py

Make sure eye_open.png, eye_closed.png, and .ico are in the same folder.


---

👨‍💻 Author

D. Sai Srinivas Reddy
B.Tech – Computer Science and Engineering
Vignan’s LARA Institute of Technology and Science


---

📬 Contact

📧 Email: saisrinivasreddy456@gmail.com

🔗 LinkedIn: linkedin.com/in/sai-srinivas-reddy

💻 GitHub: github.com/Reddy-02



---

🔒 Internship Statement

This project was developed as part of a Cybersecurity & Ethical Hacking Internship to demonstrate secure software development and password validation using regular expressions in a GUI environment.
