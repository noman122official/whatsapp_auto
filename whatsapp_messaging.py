from twilio.rest import Client

def msg_send(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'ACe82f87fc51567b2a4e722d9e45e*****'
    auth_token = '76b30edf9053de41ce9d61e4ce5*****'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'':'+91[yournumber]'}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'Hello from Naman{}'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )

        print(msg_loved_ones.sid)

msg_send()


        