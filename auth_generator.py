import gspread

# 強制觸發本地瀏覽器授權，並將結果萃取為 authorized_user.json
gc = gspread.oauth(
    credentials_filename='credentials.json',
    authorized_user_filename='authorized_user.json'
)
print("✅ 物理授權成功！專案目錄已生成 authorized_user.json，此為雲端靜默專用金鑰。")
