import os
import struct

# Определяем ключ для шифрования
key = b'mysecretkey'

# Определяем имя исходного файла и файла-оболочки
source_file = 'my_program.exe'
wrapper_file = 'wrapper.exe'

# Читаем содержимое исходного файла в бинарном режиме
with open(source_file, 'rb') as f:
    source_data = f.read()

# Шифруем содержимое исходного файла с помощью ключа
encrypted_data = bytearray()
for i in range(len(source_data)):
    key_c = key[i % len(key)]
    encrypted_c = (source_data[i] + key_c) % 256
    encrypted_data.append(encrypted_c)

# Читаем содержимое файла-оболочки в бинарном режиме
with open(wrapper_file, 'rb') as f:
    wrapper_data = f.read()

# Находим позицию, куда нужно вставить зашифрованные данные исходного файла
pos = wrapper_data.find(b'\x00\x00\x00\x00')

# Заменяем 4 байта в файле-оболочке на длину зашифрованных данных исходного файла
data_len = struct.pack('I', len(encrypted_data))
wrapper_data = wrapper_data[:pos] + data_len + wrapper_data[pos+4:]

# Добавляем зашифрованные данные исходного файла в файл-оболочку
wrapper_data = wrapper_data + encrypted_data

# Шифруем содержимое файла-оболочки с помощью ключа
encrypted_wrapper_data = bytearray()
for i in range(len(wrapper_data)):
    key_c = key[i % len(key)]
    encrypted_c = (wrapper_data[i] + key_c) % 256
    encrypted_wrapper_data.append(encrypted_c)

# Записываем зашифрованные данные в новый файл
encrypted_file_name = os.path.join(os.path.dirname(os.path.abspath(file)), 'encrypted_wrapper.exe')
with open(encrypted_file_name, 'wb') as f:
    f.write(encrypted_wrapper_data)

# Ждем, пока пользователь не запустит зашифрованный файл-оболочку
while True:
    response = input('Press enter to decrypt and run the file: ')
    if response == '':
        break

# Читаем содержимое зашифрованного файла-оболочки в бинарном режиме
with open(encrypted_file_name, 'rb') as f:
    encrypted_wrapper_data = f.read()

# Расшифровываем содержимое файла-оболочки с помощью ключа
wrapper_data = bytearray()
for i in range(len(encrypted_wrapper_data)):
    key_c = key[i % len(key)]
    decrypted_c = (encrypted_wrapper_data[i] - key_c)