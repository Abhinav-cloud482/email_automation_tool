# Email Automation Tool

> A Python tool to send and schedule Gmail messages securely using App Passwords, `smtplib`, and `schedule` for automated email workflows.


## Project Description

**Email Automation Tool** is a lightweight Python-based application that allows users to send and schedule Gmail messages directly from the terminal.

The project uses :

* `smtplib` for secure Gmail SMTP email delivery
* `schedule` for automated email scheduling
* Built-in validation and error handling for reliable workflows

The tool provides a simple menu-driven interface where users can :

* Send emails instantly
* Schedule emails for a specific time
* Authenticate securely using Gmail App Passwords
* Validate email addresses
* Handle login and input errors gracefully

It is designed as a simple automation utility for personal productivity, workflow automation, and Python learning projects.


# Features

- Send emails instantly through Gmail SMTP
- Schedule emails using 24-hour time format
- Secure authentication using Gmail App Passwords
- Email address validation
- Simple terminal-based menu system
- Error handling for invalid inputs and authentication failures
- Lightweight and beginner-friendly Python implementation


# Requirements

Before running the project, make sure you have :

* Python **3.7 or higher**
* A Gmail account
* Gmail **2-Step Verification enabled**
* Gmail **App Password generated**


# Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abhinav-cloud482/email-automation-tool.git
```

Move into the project folder :

```bash
cd email-automation-tool
```


### 2. Install dependencies

```bash
pip install schedule
```


# Gmail App Password Setup

This tool does **not** use your normal Gmail password.

Follow these steps :

1. Open your Google Account settings.
2. Enable **2-Step Verification**.
3. Create an **App Password** for Mail.
4. Copy the generated App Password.
5. Use that password when running the program.

Your Gmail password remains private and secure.


# Run the Application

Start the tool :

```bash
python email_automation.py
```

Follow the terminal instructions :

1. Enter your Gmail address.
2. Enter your Gmail App Password.
3. Enter receiver email.
4. Enter subject and message.
5. Choose sending option.


# Usage

## 1. Send Email Immediately

Select:

```
1. Send Email Now
```

Enter the required details and the email will be delivered instantly.


## 2. Schedule an Email

Select :

```
2. Schedule Email
```

Provide a time in :

```
HH:MM
```

Example :

```
18:30
```

The program will continue running and automatically send the email at the selected time.


## 3. Exit

Select :

```
3. Exit
```

The application closes safely.


# Example Run

```
============================================================
                 EMAIL AUTOMATION TOOL
============================================================

MAIN MENU
==================================================
1. Send Email Now
2. Schedule Email
3. Exit

Choose an option:
```


# Project Structure

```
email-automation-tool/
│
├── email_automation.py     # Main Python application
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```


# Security Notes

* Never use your normal Gmail password.
* Always use a Gmail App Password.
* Do not share your App Password publicly.
* Consider using environment variables for production projects.


# Future Improvements

Possible upgrades :

* Add GUI interface using Tkinter
* Add email templates
* Support multiple scheduled emails
* Add database storage
* Add logging system
* Add encrypted credential storage


# License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project.


# Contributing

Contributions are welcome!

For major changes :

1. Open an issue first.
2. Discuss the proposed improvement.
3. Submit a pull request.


# Author

Developed by **Abhianv Dixit**

Python Developer | Automation & Workflow Tools
