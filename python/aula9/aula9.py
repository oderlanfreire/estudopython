def write_archive(text):
    archive = open('teste.txt', 'w')
    archive.write(text)
    archive.close()


def update_archive(text):
    archive = open('teste.txt', 'a')
    archive.write(text)
    archive.close()

def read_archive(archive_name):
    archive = open(archive_name, 'r')
    text = archive.read()
    print(text)


if __name__ == '__main__':
    ##write_archive('primeira linha.\n')
    #update_archive('segunda linha.\n')
    read_archive('teste.txt')

# para modificar o arquivo se usa 'a' no lugar do 'w' caso ja exista algo escrito no arqivo
