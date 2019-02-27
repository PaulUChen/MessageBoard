# MessageBoard 留言板

以下是用到的
Django 2.1.3
Python 3
virtualenv 15.1.0
撰寫是使用PyCharm
另外有用到的套件：
pip install django-allauth

在messageboard資料夾底下，以終端機或直接在PyCharm的Terminal輸入
python manage.py runserver
點擊 http://127.0.0.1:8000/
即可執行網站

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
