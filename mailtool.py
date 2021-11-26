import smtplib
import webbrowser
import sys
import time



class mail_tool:
    userid=" "
    password=" "
    body=" "
    target=" "
    subject=" "
    target_list=[]
    def __init__(self,user_id,passwd,msg,tgt,sub):
        self.userid=user_id
        self.password=passwd
        self.body=msg
        self.target=tgt
        self.subject=sub

    def spam(self):
        print("----------------------MAIL SPAMMER----------------------------")
        count=int(input("Enter the number of mails to spam the Target: "))
        message = ("From :\t" + self.userid + "\nSubject :\t" + self.subject + "\n" + self.body)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        try:
            server.login(self.userid, self.password)
        except smtplib.SMTPAuthenticationError:
            print("\nPlease Check your Password\n")
            print("\nOr Please enable less-secure option in your Gmail Account\n")
            resp = int(input("\nEnter 1 to enable Less-Secure-Apps now or Enter 0 to ignore :\n\n"))
            if (resp == 1):
                webbrowser.open('http://myaccount.google.com/lesssecureapps', new=2)
                sys.exit()

        for i in range(0,count):
            try:
                server.sendmail(self.userid, self.target, message)
                print("\nSuccessfully sent " + str(i + 1) + " Mail to the target \n")
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nMail Spammer has been stopped by User\n")
                sys.exit()
            except:
                print("\nFailed to Send!!!\n")

        server.close()

    def multiple_mail(self):
        print("----------------------MULTI-MAIL----------------------------")

        message = ("From :\t" + self.userid + "\nSubject :\t" + self.subject + "\n" + self.body)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        try:
            server.login(self.userid, self.password)
        except smtplib.SMTPAuthenticationError:
            print("\nPlease Check your Password\n")
            print("\nOr Please enable less-secure option in your Gmail Account\n")
            resp = int(input("\nEnter 1 to enable Less-Secure-Apps now or Enter 0 to ignore :\n\n"))
            if (resp == 1):
                webbrowser.open('http://myaccount.google.com/lesssecureapps', new=2)
                sys.exit()
        for i in self.target_list:
            try:
                server.sendmail(self.userid, i, message)
                print("\nSuccessfully sent Mail to " + i + " Account !!!\n")
                time.sleep(1)
            except KeyboardInterrupt:
                print("Process has been Interrupted by User")
                sys.exit()
            except:
                print("Failed to Send!!!")

        server.close()

def main():
    print("------------------------------------MAIL TOOL -----------------------------")
    print("1. MAIL SPAMMER ")
    print("2.SEND MAIL TO MULTIPLE ID'S")

    choice=input("Enter your choice: ")
    if(choice=='1'):
        mail_id = input("Enter your Gmail id: ")
        passwrd = input("Enter your password: ")
        msg = input("Enter the message to be sent: ")
        sub = input("Enter the subject of mail: ")
        target = input("Enter the target mail Id: ")

        mail_client = mail_tool(mail_id, passwrd, msg, target, sub)
        mail_client.spam()

    if(choice=='2'):
        mail_id = input("Enter your Gmail id: ")
        passwrd = input("Enter your password: ")
        msg = input("Enter the message to be sent: ")
        sub = input("Enter the subject of mail: ")
        mail_client = mail_tool(mail_id, passwrd, msg, " ", sub)
        n = int(input("Enter the number of G-Mail accounts you want to send this mail to : "))
        for i in range(0, n):
            target = input("Enter G-Mail id no." + str(i + 1) + " :\t")
            mail_client.target_list.append(target)
        mail_client.multiple_mail()










main()