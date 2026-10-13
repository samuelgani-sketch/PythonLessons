st = "In a distant, but not so unrealistic, future \
where mankind has abandoned earth because it has \
become covered with trash from products sold by \
the powerful multi-national Buy N Large corporation, \
WALLE, a garbage collecting robot has been left to \
clean up the mess. Mesmerized with trinkets of Earth's \
history and show tunes, WALLE is alone on Earth except \
for a sprightly pet cockroach. One day, EVE, a sleek \
(and dangerous) reconnaissance robot, is sent to Earth to \
find proof that life is once again sustainable."

# 1. Длина строки
print(len(st))

# 2. Весь текст в нижнем регистре
print(st.lower())

# 3. Замена WALLE на WALL-E
st = st.replace("WALLE", "WALL-E")
print(st)

# 4. Сколько раз встречается слово Earth
print(st.count("Earth"))