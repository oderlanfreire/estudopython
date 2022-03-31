from datetime import date, datetime, time


def trabalhando_data():
    data_hoje = date.today()
    data_hoje_str = data_hoje.strftime('%A %B %Y')
    print(type(data_hoje))
    print(data_hoje_str)
    print(type(data_hoje_str))


def trabalhando_tempo():
    horario = time(hour=15, minute=30, second=44)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def date_time():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))


if __name__ == '__main__':
    # trabalhando_data()
    # trabalhando_tempo()
    date_time()
