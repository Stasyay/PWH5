# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

st = 'я люблю Квабван абвод жлпабв кофе'
st2 = 'абв'

res = list(filter(lambda x: st2 not in x, st.split()))

print(" ".join(res))
