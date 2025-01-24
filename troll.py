import random
import time
import webbrowser

while True:                    #web sitelerini değiştrebilirsiniz
    sites = random.choice ([ "youtube.com" , "instagram.com" , "facebook.com" , "pinterest.com" , "whatsapp.com" , "boomsonar.com"])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    time.sleep(0.1)        #süreyi ayarlayabilirsiniz(çok hızlı şuan)
