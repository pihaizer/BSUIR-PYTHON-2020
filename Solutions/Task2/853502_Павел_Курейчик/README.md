Python: >= 3.8

Установка программы:

Прописываем в терминале 'python setup.py install', находясь в главной папке проекта.

Тестирование:

Для запуска тестов необходимо прописать 
'python -m unittest tests.test_(cached/external_sort/json_decoder/json_encoder/singleton/vector)'

Оценка покрытия кода тестами:

Для запуска всех тестов используем 'coverage run -m unittest discover' (необходимо подождать около минуты).
Для оценки покрытия кода тестами прописываем 'coverage report -m' и получаем необходимую информацию