# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

word1 = "разработка"
word2 = "сокет"
word3 = "декоратор"

print(type(word1), word1)
print(type(word2), word2)
print(type(word3), word3)

word1_unicode = word1.encode('unicode_escape').decode()
word2_unicode = word2.encode('unicode_escape').decode()
word3_unicode = word3.encode('unicode_escape').decode()

print(type(word1_unicode), word1_unicode)
print(type(word2_unicode), word2_unicode)
print(type(word3_unicode), word3_unicode)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

print(type(word_1), word_1, len(word_1))
print(type(word_2), word_2, len(word_2))
print(type(word_3), word_3, len(word_3))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

# Слова "класс" и "функция" невозможно записать в байтовом типе, так как они содержат символы, не принадлежащие ASCII-таблице (кодировка по умолчанию для байтовых строк).
# Слова "attribute" и "type" можно записать в байтовом типе.


# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

a = "разработка"
b = "администрирование"
c = "protocol"
d = "standard"

a_bytes = a.encode()
b_bytes = b.encode()
c_bytes = c.encode()
d_bytes = d.encode()

a_decoded = a_bytes.decode()
b_decoded = b_bytes.decode()
c_decoded = c_bytes.decode()
d_decoded = d_bytes.decode()

print(a, "-->", a_bytes, "-->", a_decoded)
print(b, "-->", b_bytes, "-->", b_decoded)
print(c, "-->", c_bytes, "-->", c_decoded)
print(d, "-->", d_bytes, "-->", d_decoded)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess

sites = ["yandex.ru", "youtube.com"]

for site in sites:
    ping_process = subprocess.Popen(['ping', '-c', '5', site], stdout=subprocess.PIPE)
    ping_output = ping_process.communicate()[0]
    print(ping_output.decode('cp866').encode('utf-8'))
