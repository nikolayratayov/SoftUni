class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return print(f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}')



emails = []
while True:
    a = input()
    if a == 'Stop':
        break
    a = a.split(' ')
    sender = a[0]
    receiver = a[1]
    content = a[2]
    email = Email(sender, receiver, content)
    emails.append(email)

a = input().split(', ')
b = []
for i in a:
    b.append(int(i))
for i in b:
    emails[i].send()

for i in emails:
    i.get_info()