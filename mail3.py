import os
import smtplib

from dotenv import load_dotenv

website = "https://dvmn.org/profession-ref-program/khudoyan7/Mm9m5/"
friend_name = "Иван"
my_name = "Азат"
from_email = "cfcenzo@yandex.ru"
to_email = "cfcenzo@yandex.ru"
subject = "Важно!"

letter = """\
From: {from_email}
To: {to_email}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем фидбэк от преподавателя.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах.  
Задачи от тимлидов со стажем от 10 лет в программировании.  
→ Будешь учиться без стресса и бессонных ночей.  
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.  
→ Подготовишь крепкое резюме.  
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

message = letter.format(friend_name=friend_name, my_name=my_name, website=website, from_email=from_email, to_email=to_email, subject=subject)

load_dotenv()

login = os.getenv("EMAIL_LOGIN")
password = os.getenv("EMAIL_PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(login, password)
server.sendmail(from_email, to_email, message.encode("UTF-8"))

server.quit()
