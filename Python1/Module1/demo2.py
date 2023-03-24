name = 'Иван'
age = 32
job_title = 'Бухгалтер'

#'Уважаемый, ... ... Поздравляем Вас с ...'

message2 = 'Уважаемый, %s %s. Поздравляем вас с %s.' % (name, job_title, age)
message3 = "Уважаемый, {0} {1}. Поздравляем вас с {2}.".format(name, job_title, age)
message4 = f"Уважаемый, {name.upper()} {job_title}. Поздравляем вас с {age}."
print(message2)
print(message3)
print(message4)