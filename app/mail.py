
# TODO with girder
def send_email(subject, sender, recipients, text_body, html_body):
    msg = {}
    msg.body = text_body
    msg.html = html_body
    return msg

