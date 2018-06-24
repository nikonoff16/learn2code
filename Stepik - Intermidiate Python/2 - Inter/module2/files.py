
# r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, содержимое файла стирается
# a (append) - открыть для записи, запись ведется в конец

with open('dataset_24465_4.txt') as orig, open('test2.txt', 'a') as kopy:
    buffer = []
    for line in orig:
        line = line.rstrip()
        buffer.append(line)
    buffer.reverse()
    contents = '\n'.join(buffer)
    kopy.write(contents)
