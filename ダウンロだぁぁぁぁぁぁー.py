import urllib.request
import urllib.error
import os

url = input("ダウンロードしたいファイルのリンクを入力:")
yorn = input(f"{url}を本当にダウンロードしますか？（Y/N)")

if yorn.lower() == "y":
    print("ダウンロードを開始します")
    try:
        filename = os.path.basename(url)

        response = urllib.request.urlopen(url)
        data = response.read()

        with open(filename, "wb") as f:
            f.write(data)

        print("ダウンロードしたファイル名:", filename)
        print("ダウンロード完了")

    except urllib.error.HTTPError as e:
        print("HTTP エラー　そのようなファイルはなさそうです..", e.code, e.reason)

    except urllib.error.URLError as e:
        print("URL にアクセスできませんでした", e.reason)

    except Exception as e:
        print("エラーが発生しましたもう一回お試しください", e)


else:
    print("ダウンロードをキャンセルしました")
