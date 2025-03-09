import telebot
 from telebot.types import ReplyKeyboardMarkup, KeyboardButton
 from config import TOKEN
 from logic import get_class
 
 bot = telebot.TeleBot(TOKEN)
 
 @bot.message_handler(commands=['start', 'help'])
 def send_welcome(message):
     bot.send_message(message.chat.id, 
                      "Привет! Отправь мне картинку собаки, и я определю, сгенерирована она с помощью AI или сделана по настоящему, а так же могу посоветовать библиотеки для датасетов с помощью комманды library.")
 
 @bot.message_handler(content_types=['photo'])
 def get_photo(message):
     if not message.photo: 
         return bot.send_message(message.chat.id, "Это не картинка")
 
     file_info = bot.get_file(message.photo[-1].file_id)
     print('file_info:', file_info)
     file_name = file_info.file_path.split('/')[-1]
     print('file_name:', file_name)
 
     downloaded_file = bot.download_file(file_info.file_path)
     with open(file_name, 'wb') as new_file:
         new_file.write(downloaded_file)
 
     result = get_class(image_path=file_name)
     bot.send_message(message.chat.id, f'{result}')
 
 @bot.message_handler(commands=['library'])
 def library_dataset(message):
     bot.send_message(message.chat.id, '''NumPy - Упрощает работу с векторами и матрицами, содержит готовые методы для разных математических операций. 
 SciPy - Основывается на NumPy и расширяет её возможности, включает методы линейной алгебры и для работы с вероятностными распределениями, интегральным исчислением и преобразованиями Фурье. 
 Matplotlib - Низкоуровневая библиотека для создания двумерных диаграмм и графиков. 
 Scikit learn - Основана на NumPy и SciPy, в ней есть алгоритмы для машинного обучения и интеллектуального анализа данных: кластеризации, регрессии и классификации. 
 TensorFlow - Фреймворк для обучения, настройки и тренировки нейронных сетей. 
 Keras - Библиотека глубокого обучения, благодаря модульности и масштабированию позволяет легко и быстро создавать прототипы. 
 Seaborn - Библиотека более высокого уровня, чем Matplotlib, с её помощью проще создавать специфическую визуализацию: тепловые карты, временные ряды и скрипичные диаграммы. 
 Bokeh - Создаёт интерактивные и масштабируемые графики в браузерах, используя виджеты JavaScript. 
 Basemap - Используется для создания карт. 
 NetworkX - Применяется для создания и анализа графов и сетевых структур, предназначена для работы со стандартными и нестандартными форматами данных.  
 ''')
 
 
 
 bot.infinity_polling()
