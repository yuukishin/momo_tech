import requests
from bs4 import BeautifulSoup
import os

url = "https://www.akb48.co.jp/about/members"
file_path = "C:\\Users\\user\\OneDrive\\ドキュメント\\python\\momo_tech\\images\\pokemon"

# HTML取得
response = requests.get(url)
response.raise_for_status()

# BeautifulSoupオブジェクト生成
soup = BeautifulSoup(response.text, "html.parser")

# imgタグを全て取得
img_tags = soup.find_all("img")

# imgタグのsrc属性から画像のURLを取得し、対象画像をダウンロード
for i, img_tag in enumerate(img_tags):
    img_url = img_tag.get("src")

    # URLが相対URLの場合には絶対URLに変換
    img_url = requests.compat.urljoin(url, img_url)

    # 画像データを取得
    img_response = requests.get(img_url)
    # HTTPステータスが200以外の場合は例外を発生させる
    img_response.raise_for_status()
    # ファイル名作成
    filename = os.path.join(file_path, f"akb48_member{i}.jpg")

    # 画像データをファイルに保存
    with open(filename, "wb") as f:
        f.write(img_response.content)
