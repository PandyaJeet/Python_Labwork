from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send_message(self, user, text):
        pass


class EmailNotification(Notification):
    def send_message(self, user, text):
        print(f"Sending Email to {user}: {text}")


class SMSNotification(Notification):
    def send_message(self, user, text):
        print(f"Sending SMS to {user}: {text}")


def main():
    email = EmailNotification()
    sms = SMSNotification()
    email.send_message("krupa@charusat.edu.in", "College will remain closed tomorrow.")
    sms.send_message("9876543210", "College will remain closed tomorrow.")


main()
