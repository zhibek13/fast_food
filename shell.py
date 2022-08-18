from fast_food.models import *

user = User.objects.create(email='nikname21@gmail.com', password='defender42')
client = Client.objects.create(name='Азат Соколов', card_number='4147565798789009', user=user)
user2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')
worker = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=user2)
sh = Food.objects.create(name='Шаурма', start_price='50')
g = Food.objects.create(name='Гамбургер', start_price='50')
syr = Ingredient.objects.create(name='Сыр', extra_price='10')
chicken = Ingredient.objects.create(name='Курица', extra_price='70')
meat = Ingredient.objects.create(name='Говядина', extra_price='80')
salat = Ingredient.objects.create(name='Салат', extra_price='15')
fri = Ingredient.objects.create(name='Фри', extra_price='15')

order = Order.objects.create(food=sh, ingredient=meat, client=client, worker=worker, order_date_time='2022-08-18')
order.ingredient.set([syr, salat, fri])
order2 = Order.objects.create(food=g, ingredient=chicken, client=client, worker=worker, order_date_time='2022-08-18')
order2.ingredient.set([salat])

