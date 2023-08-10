import smtplib
import ssl
import requests
import datetime
import os


def send_email():
    host = "smtp.gmail.com"
    port = 465
    username = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    receiver = ["skeerthana4734@gmail.com", "keerthukeerthana4734@gmail.com"]
    message = (
        f"Subject: Astronomy Image of the day - {str(todayDate)}"
        + "\n"
        + "\nGood Morning! \n"
        + "\n"
        + f"Image: {title}"
        + "\n"
        + "Click the below link to know more"
        + "\n"
        + link
        + "\nHave a good day!\n\n\n"
        + "Regards,\nKeerthana"
    )
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        for id in receiver:
            server.sendmail(username, id, message)


todayDate = datetime.date.today()
link = "https://astronomy-image-of-the-day.streamlit.app/"
apiKey = os.environ.get("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"

response = requests.get(url)
data = response.json()

title = data["title"]
print(title)


if __name__ == "__main__":
    send_email()
