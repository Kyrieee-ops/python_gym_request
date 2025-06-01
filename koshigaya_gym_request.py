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
from selenium.common.exceptions import TimeoutException, NoSuchWindowException


def init_browser():
    options = Options() #optionsの呼び出し
    options.page_load_strategy = 'normal' #ページ全体がロードするまで待機
    # ブラウザを最大化した状態で起動するオプションを追加
    options.add_argument('--start-maximized')
    options.add_argument('--enable-webgl')  # WebGLを有効化
    options.add_argument('--ignore-gpu-blocklist')
    
    return webdriver.Chrome(options=options) # PATHが通っていればこれでOK

def user_requests(browser):
    try:
        email = os.getenv("EMAIL")  # 環境変数からメールアドレスを取得
        # 越谷市スポーツセンターのページにアクセス
        target_url = "https://www.city.koshigaya.saitama.jp/kurashi_shisei/kosodate/supotu/etc/sportscenter.html"
        browser.get(target_url)

        # current_pos = browser.execute_script("return window.pageYOffset;")
        # print(f"現在の垂直位置: {current_pos}px")

        # # ページの高さを確認
        # page_height = browser.execute_script("return document.body.scrollHeight")
        # print(f"ページ全体の高さ: {page_height}px")

        # 指定の場所までスクロール
        browser.execute_script("window.scrollTo(0, 2250)")

        # 「こちらをクリック」をクリック
        link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main_content2"]/p[2]/a'))
        )

        link.click()
        print("越谷市スポーツセンターのページにアクセスし、リンクをクリックしました")

        # 新しいタブへの切り替えを試みる
        try:
            WebDriverWait(browser, 3).until(
                lambda d: len(d.window_handles) > 1
            )
            browser.switch_to.window(browser.window_handles[1])
            print("利用者管理タブに切り替えました")
        except (TimeoutException, NoSuchWindowException):
            print("新しいタブへの切り替えは発生しませんでした。現在のタブを継続使用します")

        # どちらの場合でも実行する処理
        no_registration_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="js-main"]/div[3]/label'))
        )
        no_registration_link.click()
        print("「利用登録せずに申し込む方はこちら」のリンクをクリックしました -> 手続き申し込み画面に遷移します")

        # 新しいウィンドウ/タブに切り替え
        WebDriverWait(browser, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        browser.switch_to.window(browser.window_handles[1])
        print("手続き申し込みタブに切り替えました")

        # 「同意する」を押下
        # 同意した後の画面は新しいブラウザで表示しているわけではないのでブラウザ切り替え処理は不要
        agree_button = browser.find_element(By.ID, "ok")
        agree_button.click()

        current_pos = browser.execute_script("return window.pageYOffset;")
        print(f"現在の垂直位置: {current_pos}px")

        # ページの高さを確認
        page_height = browser.execute_script("return document.body.scrollHeight")
        print(f"ページ全体の高さ: {page_height}px")
        # スクリーンショットを保存
        browser.save_screenshot("koshigaya_sports_center.png") 

        browser.execute_script("window.scrollTo(0, 700)")

        # 手続き申し込み画面で連絡先メールアドレスを入力
        send_email = browser.find_element(By.XPATH, '//*[@id="inputMailtoForm.sendMailto"]')
        send_email.send_keys(email)
        print("連絡先メールアドレスを入力しました")
        
        send_mailto_confirm = browser.find_element(By.XPATH, '//*[@id="inputMailtoForm.sendMailtoConfirm"]')
        send_mailto_confirm.send_keys(email)
        print("確認のため、メールアドレスを再度入力しました")

        # 完了ボタンをクリックし申請リンクをメールで受信
        complete_button = browser.find_element(By.XPATH, '//*[@id="js-main"]/div[4]/div[2]/input')
        complete_button.click()
        print("申請リンクボタンをクリックしました")

        return True
    except Exception as e:
        print(f"利用申請中にエラーが発生しました: {e}")
        return False
    finally:
        pass

# メイン処理フロー
def main():
    browser = init_browser()
    # 体育館貸出抽選の画面に遷移
    user_requests(browser)  # 利用申請処理
    browser.quit()  # 必ずブラウザを閉じる


# main関数を呼び出す
if __name__ == "__main__":
    load_dotenv()  # 環境変数読み込み
    main()