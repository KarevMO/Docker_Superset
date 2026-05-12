import secrets
import string

random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(50))

print(random_string)

Пароли от Суперсета:
SUPERSET_SECRET_KEY: 'BBNBaTyYSDNw9zXh25aycMq7pOL52QnLLBRT4nhMgIumVd5WDg'
Администратор
Логин:admin
Пароль:Bacin
Другие пользователи
Логин:team
Пароль:1234


Пароли от БД
POSTGRES_USER: admin
POSTGRES_PASSWORD: 1212