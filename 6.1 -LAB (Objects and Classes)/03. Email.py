class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    information = input()
    if information == "Stop":
        break
    else:
        # information_list = information.split()
        # current_sender = information_list[0]
        # current_receiver = information_list[1]
        # current_content = information_list[2]
        current_sender, current_receiver, current_content = information.split()
        current_email = Email(current_sender, current_receiver, current_content)
        emails.append(current_email)
indices_of_the_sent_emails = [emails[int(index)].send() for index in input().split(", ")]
for email in emails:
    print(email.get_info())


# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# line = input()
# while line != "Stop":
#     tokens = line.split()
#     current_sender = tokens[0]
#     current_receiver = tokens[1]
#     current_content = tokens[2]
#     email = Email(current_sender, current_receiver, current_content)
#     emails.append(email)
#     line = input()
# send_emails = list(map(lambda x: int(x), input().split(", ")))
# for x in send_emails:
#     emails[x].send()
# for email in emails:
#     print(email.get_info())
