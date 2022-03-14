# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

with(open('nginx_logs.txt', encoding='utf-8')) as f:
    # content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    spam = {}

    for line in f:
        spam.setdefault(line.split()[0], 0)
        spam[line.split()[0]] += 1
        # print(spam)

spam = sorted(spam.items(), key=lambda x: x[1], reverse=True)
print(spam[:1])
