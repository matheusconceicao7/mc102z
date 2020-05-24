lista = input().split()
palavras = []
numeros = []
hashtags = []
emoticons = []


def verifica_palavra(x):
    if x.isalpha():
        return True
    else:
        return False


def verifica_numero(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def verifica_hashtag(x):
    if x[0] == "#":
        if x[1:].isalpha():
            return True
        else:
            return False
    else:
        return False


for item in lista:
    if verifica_palavra(item):
        palavras.append(item)
    elif verifica_numero(item):
        numeros.append(item)
    elif verifica_hashtag(item):
        hashtags.append(item)
    else:
        emoticons.append(item)

result_palavras = "Palavra(s): {0}".format(" ".join(palavras)).rstrip()
result_numeros = "Numero(s): {0}".format(" ".join(numeros)).rstrip()
result_hashtags = "Hashtag(s): {0}".format(" ".join(hashtags)).rstrip()
result_emoticons = "Emoticon(s): {0}".format(" ".join(emoticons)).rstrip()

print(result_palavras)
print(result_numeros)
print(result_hashtags)
print(result_emoticons)
