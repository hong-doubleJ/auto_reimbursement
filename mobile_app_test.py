from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# 登录与授权
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # 首次登录时弹出网页认证
drive = GoogleDrive(gauth)

# 上传文件
uploaded = st.file_uploader("上传发票/截图", accept_multiple_files=True)
if uploaded:
    for file in uploaded:
        gfile = drive.CreateFile({'title': file.name, 'parents': [{'id': 'Attachment'}]})
        gfile.SetContentString(file.getvalue().decode('utf-8', errors='ignore'))
        gfile.Upload()
        st.success(f"已上传到Google Drive: {file.name}")
