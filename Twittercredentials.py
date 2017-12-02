import tweepy

consumer_key = "bOhGN34wsBPeXRVKGgBYpoIVe";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "YuIrg5oKVgayFl8ihRx6bnoNr7LdutrN0Ff4Gbqj350zSMLSXQ";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "930606736398016512-kojlvsUVX07MP4NgMgoR1OFS8Cj6ilf";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "XU07tG6PRp3GNnchsVmhn2nsHPRdeLW9YJ0HJsh5GgZhl";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



