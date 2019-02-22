from flask import Flask
from config import Configuration
from posts.blueprint import posts
#Импортируем класс Flask из модуля flask установленного
app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix="/blog")
#Создание переменной арр конструктором класса Flask
#__name__ - имя текущего файла, передаваемое в конструктор
#flask, отталкиваясь от имени файла и пути к нему ищет отальные, необходимые для работы элементы
#

