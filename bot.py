#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6659031789:AAFGvbid5bXThMZCgTP25WEppdKIvAp90Po'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('img/QA.png', 'rb')
	bot.send_photo(message.chat.id, sti)
    #клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Операторы SQL")
	item2 = types.KeyboardButton("Операторы Linux")
	item3 = types.KeyboardButton("Операторы Git")
	item4 = types.KeyboardButton("Структура багрепорта")
	item5 = types.KeyboardButton("Типы данных Json")
	markup.add(item1, item2, item3, item4, item5)
	bot.send_message(message.chat.id, "Привет тебе от помощника Джека , {0.first_name}!".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)
    #назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':

		if message.text == 'Операторы SQL':
			foto = open("img/sql.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, '''SELECT - Какой столбик вывести, 
    FROM - Из какой таблички вывести  
JOIN- Какую табличку добавляем
    ON- Название столбика из одной таблицы
WHERE- Какой столбик известен из текста вопроса = его значение (AND-и OR-или)
    ORDER BY- Столбец по которому сортировать
LIMIT- Число, ограничение выборки (правило хорошего тона, чтобы не повесить БД)
    UPDATE- Название таблицы
SET- Какой столбик меняем = новое значение

			Агрегатные функции
COUNT()- Количество
    MIN()- Минимальное значение
MAX()- Максимальное значение
    AVG()- Среднее значение
SUM()- Сумма
			Виды JOIN
INNER JOIN- Вернет данные у которых есть пара
     LEFT JOIN- Вернет данные у которых есть пара и данные без пары из левой таблицы
RIGHT JOIN- Выдает данные, у которых есть пара и данные без пары из правой таблицы
    FULL JOIN- Выдает данные у которых как усть пара так и без праы
CROSS JOIN- Выдает комбинацию каждой строки в 1 таблице со всеми записями во 2 таблице
    *- Выводит все ''')




		elif message.text == 'Операторы Linux':
			foto = open("img/Linux.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, '''PWD - Показать текущее местоположение (папку)
    CD - Сменить папку (change direktory)
CD .. - Вернуться на уровень выше
    LS - Просмотр содержимого папки
    MKDIR - Создать новую папку
MV - Переместить или переименовать файл
    CP - Копировать файл
TOUCH - Создать файл
    RM - Удаление файла
RMDIR - Удаление папки
    CAT - Предосмотр содержимого
GREP - Фильтр
    TAIL - Выведи последние N строк
HEAD - Выведи первые N строк
    VIM NANO - Открыть или редактировать текстовый файл
        УПРАВЛЕНИЕ в VIM:
I - Активировать режим редактора (появится внизу надпись INSERT)
	ESK - Закончить режим редактора (исчезнет внизу надпись INSERT)
ESK + :WQ + ENTER - Выйти и сохранить (при вводе этой команды она будет видна внизу терминала)
    ESK + :Q! + ENTER - Выйти без сохранений (при вводе этой команды она будет видна внизу терминала)
''')



		elif message.text == 'Операторы Git':
			foto = open("img/Git.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, '''GIT INIT - Сделать из любой папки git папку
	GIT CLONE - Скачать на компьютер репозиторий 
GIT BRANCH - Показать в какой ты сейчас ветке 
    GIT PULL - Скачать обновления с репозитория
GIT CHECKOUT -B - Переключиться на новую ветку
	GIT ADD - Добавить в текущий коммит новые файлы или папки которых раннее не было
GIT COMMIT -M - Создать коммит (сохранить текущее состояние)
	GIT PUSH - Запушить (отправить) твои изменения в репозиторий
GIT STATUS - Узнать в какой ветке ты сейчас находишься 
	GIT LOG - Показывает какие файлы ты изменил
GIT MERGE MASTER - Влить в мою ветку , ветку мастер
	GIT RESET -hard - Отменить коммит
		Как запушить изменения:
CTRL+S - Сохранить изменения в IDE (редакторе кода)
	GIT ADD . - Выполнить 
GIT COMMIT -M - "Название нового коммита"
	GIT PUSH - Выполнить
''')



		elif message.text == 'Структура багрепорта':
			foto = open("img/Bug.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, '''~Summari(Заголовок) - [bug][web][прод] - Заголовок. Что , где и при каких условиях?
        ~Description (описание) - пример, нет картинок у новостей на сайте на главной
~Шаги воспроизведения(глаголы в инфинитиве) - 1.Открыть сайт 2.Обновить страницу и т.д.
	    ~Текущий результат - Можно описать словами , желательно еще скриншотом или скринкастом
~Ожидаемый результат - Можно словами или скриншот (или ссылка на макет)
	    ~Окружение - 1.Билд(это версия приложения, сайта или бекенда,если знаем). 2.Только ios или android или на обеих платформах. 3. Браузер (какой, какая версия)
~Тестовые устройства - Например(Макбук16, андроид 10 ксиоми экр. 6 дюймов)
	    ~Ручка(чаще для баг репорта на бекенд) - Курл запроса
~Аналитика - Если бы я у вас работал то прикрепил бы ссылку на яндекс метрику с количеством пользователей, которых зааффектила проблема
	    ~Документация - Если бы я у вас работал то прикрепил бы ссылку на документацию по фиче 
~Логи(Кибана) или (Сентри) - Если бы я у вас работал то прикрепил ссылку на логи из Кибаны или Сентри
	    ~Clack или Дискорд (ссылка на тренд) - Если бы я у вас работал , то прикрепил ссылку обсуждения этого бага в слак
~Priority(приориретет) - Минор, Нормал ,Блокер 
	    ~Severity (Серьезность) - Блокер, Критикал, Нормал, Минор, Тривиал
~Followers (последователи) - Босс, Менеджер
	    ~Assignee (правоприемник) - На кого назначим
			
			)''')



		
		elif message.text == 'Типы данных Json':
			foto = open("img/JSON.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, '''"Строка"
	Число
Boolean
	null
[Массив]
	{Объект}    ''')
		else:
			bot.send_message(message.chat.id,'Я не знаю что на это ответить')



bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
