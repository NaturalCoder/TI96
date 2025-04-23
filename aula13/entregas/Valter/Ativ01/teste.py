from datetime import datetime


x = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

y = datetime.now()


print(y.strftime('Hoje é %A, %d de %B de %Y'))