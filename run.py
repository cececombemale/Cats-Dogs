from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import giphy_client
import time
from giphy_client.rest import ApiException
import random

api_instance = giphy_client.DefaultApi()
api_key = 'W5yCq7xTGzQ3e'



app = Flask(__name__)
numbers = {}
stats = ["we prevented 2,531 family pets from being surrendered.",
        "we returned 1,920 animals to their home.",
        "we placed 11,944 animals with New Hope adoption partners.",
        "we vaccinated and micro-chipped 1,454 clinic pets."
        "we helped 7,010 animals get adopted at Care Centers and Mobile events."]

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    api_instance = giphy_client.DefaultApi()
    api_key= 'W5yCq7xTGzQ3e'

    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if body == 'dog' or body == 'Dog' or body == 'cat' or body == 'Cat':
        number = request.values.get('From', None)
        msg = ""
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1
        if numbers[number] % 3 == 0:
            n = random.randint(0,5)
            msg += "ACC (Animal Care Centers of NYC) is an organization that helps homless and abandoned animals, including dogs and cats. In 2017, " + stats[n] + " Please help us by visiting our website and donating."
        tag = body
        api_response = api_instance.gifs_random_get(api_key, tag=tag)
        url = api_response.data.url
        msg = url + "\n" + msg
        resp.message(msg)
    else:
        resp.message("Would you like a dog gif or a cat gif? Please respond with 'dog' or 'cat'")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
