from app import app
from flask import render_template
#flask.render_template(template_name_or_list, **context)


@app.route('/')
def index():
	name = 'Ivan'
	return render_template('index.html', n=name)
	#Функция ищет шаблоны в папке Templates, которая должна быть расположена впапке текушего файла
