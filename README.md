# MessageBoard 留言板
----------------------------------------------------------------------------------------------------------------
＊以下是使用的語言和工具：

Django 2.1.3

Python 3

virtualenv 15.1.0

PyCharm

＊另外有用到的套件：

pip install django-allauth


在messageboard資料夾底下，以終端機或直接在PyCharm的Terminal輸入

python manage.py runserver

點擊 http://127.0.0.1:8000/

即可執行網站

----------------------------------------------------------------------------------------------------------------
檔案介紹：

＃messageboard 是專案資料夾：

urls.py 是放置網站連結的地方

users & board 是我這個專案的兩個app ：

Users 是負責做登入登出以及註冊的；board是做留言板的新增編輯以及呈現

＊Users 的部分：（這邊我是利用Djago的UserModel以及一些套件去做延伸)

models 建立 user table ； forms 建立表單；views 製作註冊功能

＊Board的部分：

models 一樣是建立留言板的資料表；forms 除了建立表單外也寫了驗證規則；

views的部分寫了 首頁的顯示規則（換頁、讀取資料）、新增留言的功能、編輯留言的功能


＊Template 資料夾

這是Django存放html的地方，主要是首頁home、註冊頁signup、新增post、編輯edit，裡頭也包含了一些跟views相呼應的規則來傳送以及存取資料庫的資料



----------------------------------------------------------------------------------------------------------------
功能：

＊完成了登入登出功能，並以email 作為帳號

  設定了兩個使用者
  
  email / password
  
  chen80312@gmail.com / 123456
  
  chen70312@gmail.com / x123456789

＊完成註冊功能 

＊完成留言板功能，一頁顯示五筆資料，可按下一頁。
  
  留言內容按照時間排序
  
  留言內容分成兩個顏色區塊，淡橘色為自己發布的留言，可進行編輯；淡藍色為別人發布的留言，不得編輯。

＊完成新增留言功能

  登入後才會出現新增留言按鈕，留言欄位有驗證機制，未填寫或字數不足會停留在同一頁。完成驗證才會送往資料庫並重導回首頁。
  
  
 ----------------------------------------------------------------------------------------------------------------
