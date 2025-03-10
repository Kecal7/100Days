import smtplib

my_email = "lukas.koupil@gmail.com"
password = "aaa"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Hello"
    )
