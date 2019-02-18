import tweepy
import csv
import time

#Credenciais de acesso do app do twitter
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#autenticação de acesso
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Criando o dataset onde os tweets serão salvos
file = csv.writer(open("dataset_teste.csv", "w"))
file2 =  open("dataset_teste_json","w")

row = []

#Criando o padrão deconsumo da search api para captura dos tweets.

statuses = tweepy.Cursor(api.search, q='#orlando', since='2019-02-18', until='2019-02-17', lang='en').items()

while True:
    try:
        # Lendo os tweets
        status = statuses.next()
        # capturando só alguns parametros
        row=str(status.user.screen_name),str(status.created_at),str(status.text),status.geo
        # Escrevendo no CSV
        file.writerow(row)
        # Salvando o JSON
        file2.write(str(status))
        file2.write("\n")

        exit()

    except tweepy.TweepError:
        # Devido a limitação a cada 3200 tweets é necessário esperar 15 minutos
        print("wait 15 minutes...")
        time.sleep(60*15)
        continue
    except StopIteration:
        print("Acabou!!")
        break