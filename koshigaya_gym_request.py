# 越谷SCページにアクセスし、申請先リンクをクリック
'''
1. 下記リンクにアクセス
https://www.city.koshigaya.saitama.jp/kurashi_shisei/kosodate/supotu/etc/sportscenter.html

2. 「こちらをクリック」をクリック処理
3. 以下画面に新しいブラウザを開いて遷移するのでブラウザ切り替え処理を入れる
https://apply.e-tumo.jp/city-koshigaya-saitama-u/profile/userLogin_initDisplay?nextURL=CqTLFdO4voa96Y73xXv0Xt7dRrdLP0zYtUINsUzZVMsQBNjlCWSX%2B5endxxIyB5jug%2FX7n9%2BCBHD%0D%0Aw2FP2V8XoE%2Bm4Zo4btwgPg7R1EzFuN9JBiJ3227xzofyAk1hBwTEu%2F2pnQTLAb0%3D%0D%0A
4. 「利用登録せずに申し込む方はこちら」のリンクをクリック
5. 「同意する」を押下
6. 連絡先メールアドレスを入力
7. これで自分のメールアドレス宛てに申請リンクが届く
8. 申請リンクを開く
9. 申請者情報を入力

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# main関数を呼び出す
if __name__ == "__main__":
    load_dotenv()  # 環境変数読み込み
    main()