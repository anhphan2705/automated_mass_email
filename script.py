import rpa as r

target_email_qty = 1
gmail_username = ""
gmail_password = ""

def get_target_email(qty=target_email_qty):
    # Fake email retreival process
    target_emails = []

    for i in range(qty):
        # Open website
        r.url("https://10minutemail.net/new.html")
        r.wait()
        print("[DEBUG] Website connected")

        # read the email address
        target_emails.append(r.read("//input[@id='fe_text']"))
        print("[DEBUG] Copied email address")

    return target_emails


def email_login(username=gmail_username, password=gmail_password):
    # Connect to email
    r.url(
        "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AS5LTASKD7jTjDVqbpNsOcWqYuPOw2ye7uu_ZdaeYOyhzf2ZVDJuCDvkNVb_A2RjhQFuiM2Ga6el4Q&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-2113468384%3A1719195565901303&ddm=0"
    )
    r.wait(3)

    # Login
    print("[DEBUG] Typing username")
    r.type("//input[@type='email']", username)
    r.click('Next')
    r.wait(3)
    
    print("[DEBUG] Typing password")
    r.type("//input[@type='password']", password)
    r.click('Next')
    r.wait(7)

    print("[DEBUG] Gmail Login Successfully")

def get_screenshot(name="result.png"):
    # Screenshot of the page
    r.snap(element_identifier="page", filename_to_save=name)
    print("[DEBUG] Screenshot taken")

def send_email():
    for target_email in target_emails:
        r.click("Compose")
        r.type("//input[@aria-label='To recipients']", target_email)
        r.type("//input[@name='subjectbox']", "Test Email")
        r.type("//div[@aria-label='Message Body']", "This is a test email")
        r.dom('document.querySelector("[aria-label=\'Send ‪(Ctrl-Enter)‬\']").click()')
        r.wait(2)
        print("[DEBUG] Email sent to", target_email)
        
def check_sent_folder():
    r.url("https://mail.google.com/mail/u/0/#sent")
    r.wait(2)
    print("[DEBUG] Checked sent folder")

if __name__ == "__main__":
    r.init(turbo_mode=True, visual_automation=True)

    target_emails = get_target_email(2)
    email_login()
    send_email()
    check_sent_folder
    r.wait(3)
    get_screenshot()
    
    r.close()