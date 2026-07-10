import smtplib
import schedule
import time
import re

from getpass import getpass
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email)


def get_user_details():
    print("\n" + "=" * 60)
    print("GMAIL LOGIN")
    print("=" * 60)

    print("\nIMPORTANT")
    print("- Use your Gmail address.")
    print("- Use your Gmail App Password.")
    print("- Do NOT use your normal Gmail password.\n")

    while True:
        sender = input("Sender Gmail : ").strip()
        if valid_email(sender):
            break
        print("Invalid email address.\n")

    password = getpass("Gmail App Password : ")

    while True:
        receiver = input("Receiver Email : ").strip()
        if valid_email(receiver):
            break
        print("Invalid email address.\n")

    subject = input("Subject : ")

    print("\nEnter Email Message.")
    print("Press ENTER twice to finish.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    body = "\n".join(lines)
    return sender, password, receiver, subject, body


def send_email(sender, password, receiver, subject, body):
    try:
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        print("\nConnecting to Gmail...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender, password)
        server.send_message(message)
        server.quit()

        print("\n===================================")
        print("EMAIL SENT SUCCESSFULLY")
        print("===================================")
        print("Time :", datetime.now())
        print("From :", sender)
        print("To   :", receiver)
        print()

    except smtplib.SMTPAuthenticationError:
        print("\nLOGIN FAILED")
        print("Reason:")
        print("- Wrong Gmail address")
        print("- Wrong App Password")
        print("- Using Gmail password instead of App Password")
        print("- 2-Step Verification not enabled\n")

    except Exception as e:
        print("\nERROR")
        print(e)


def send_now():
    sender, password, receiver, subject, body = get_user_details()
    send_email(sender, password, receiver, subject, body)


def schedule_email():
    sender, password, receiver, subject, body = get_user_details()

    while True:
        schedule_time = input("\nSchedule Time (HH:MM - 24 Hour Format): ").strip()
        try:
            time.strptime(schedule_time, "%H:%M")
            break
        except ValueError:
            print("Invalid Time Format.")

    schedule.every().day.at(schedule_time).do(
        send_email, sender, password, receiver, subject, body
    )

    print("\n" + "=" * 60)
    print("EMAIL SCHEDULER STARTED")
    print("=" * 60)
    print("Sender   :", sender)
    print("Receiver :", receiver)
    print("Time     :", schedule_time)
    print("\nWaiting...")
    print("Press CTRL + C to stop.\n")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler Stopped.")


def instructions():
    print("=" * 65)
    print("EMAIL AUTOMATION TOOL")
    print("=" * 65)
    print("""
This tool allows you to:
- Send an email instantly
- Schedule an email at a specific time
- Automate repetitive email tasks
""")


def menu():
    instructions()
    while True:
        print("=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("1. Send Email Now")
        print("2. Schedule Email")
        print("3. Exit")

        choice = input("\nEnter Choice : ")
        if choice == "1":
            send_now()
        elif choice == "2":
            schedule_email()
        elif choice == "3":
            print("\nThank you for using Email Automation Tool.")
            break
        else:
            print("\nInvalid Choice.\n")


if __name__ == "__main__":
    menu()
