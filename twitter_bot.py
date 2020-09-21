from requests_oauthlib import OAuth1Session
import random
import os


def main():

    # 環境変数取得
    API_KEY = os.environ.get('API_KEY')
    API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
    ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

    # Twitter認証
    twitter = OAuth1Session(
        API_KEY, API_SECRET_KEY, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )

    # POST URL
    API_ENDPOINT = "https://api.twitter.com/1.1/statuses"
    METHOD_URL = "update.json"
    POST_URL = API_ENDPOINT + "/" + METHOD_URL

    # ツイート用パラメータ設定
    params = {"status": createMessage()}

    # Twitter API
    res = twitter.post(POST_URL, params=params)

    # 結果判定
    if res.status_code == 200:
        print("Success.")
    else:
        print(f"Failed: {res.status_code}")
        print(POST_URL)


def createMessage():

    message = ""
    i = 0

    # ランダムな日本語10文字を設定
    while i < 10:
        message += chr(random.randint(ord('あ'), ord('ん')))
        i += 1

    return message


if __name__ == "__main__":
    main()
