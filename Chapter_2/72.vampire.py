name = 'Carol'  # переменна name, где храниться имя
age = 3000      # возраст
if name == 'Alice':  # Если переменная name = Alice, то выполни инструкцию
    print('Hi, Alice')  # Блок инструкций if, выполниться если условие прописанное в if будет истинно
elif age < 12:  # Блок инструкции 2, выполниться если переменная age < 12 и предыдущие условие ложно
    print('Yor are not Alice, kiddo.')  # Блок инструкций elif.
elif age > 2000:  # Блок инструкции 3
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:  # Блок инструкции 4
    print('You are not Alice, grannie.')
