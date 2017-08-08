# moztrap-compose
lemonlatte/docker-moztrapのdocker-compose対応
DB初期化を組見込んでるのでこのまま起動すれば動く(と思う)

* lemonlatte/docker-moztrapをpull  
  `docker pull lemonlatte/docker-moztrap`

* 本データをクローン  
  `git clone git@github.com:acmos-takano/moztrap-compose.git`

* docker-composeを調整  
  * 注：ベースとなるlemonlatte/docker-moztrapがワリと古い起動方法をしてるので合わせるために環境変数を追加してる  
  * 以下に注意
```
MYSQL_HOST: db    # 内部でリンク用の環境変数を合成するためにservicesの「db」を明記。MySQLのsevice名を変えた時には注意。
DB_PORT: 3306     # 同上。
DEFAULT_FROM_EMAIL: 'from@example.com'    # 以下メール設定。向き先のメールサーバを指定。  
EMAIL_HOST: localhost  
EMAIL_PORT: 25001  
EMAIL_HOST_USER: 'please set smtpauth-user'   # ただしこの辺未検証w  
EMAIL_HOST_PASSWORD: 'please set smtpauth-password'  
EMAIL_USE_TLS: 'False'  
MOZ_SLEEP: 10   # DB起動を待つためのスリープ。```

* docker-compose起動  
  `docker-compose up -d --build`
