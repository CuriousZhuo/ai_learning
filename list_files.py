# === 文件批处理工具：第 1 步 + 第 2 步 + 第 3 步 ===
# 功能：把 test_files 下所有 .jpg 文件重命名为 IMG_ 前缀

import os  # 拿出"操作系统工具箱"

folder_path = "./test_files"  # 文件夹路径（字符串）

all_files = os.listdir(folder_path)  # 返回列表 ["music.mp3", "photo_001.jpg", ...]

for name in all_files:                      # name 临时代表列表里每个文件名
    if name.endswith(".jpg"):               # 字符串.endswith() → True/False

        # --- 第 3 步：拆名 → 拼新名 → 改名 ---

        # ① 拆：os.path.splitext("photo_001.jpg") → ("photo_001", ".jpg")
        name_part, ext_part = os.path.splitext(name)

        # ② 拼：f-string 用 {} 把变量值嵌入字符串
        new_name = f"IMG_{name_part}{ext_part}"
        # "photo_001" + ".jpg" → "IMG_photo_001.jpg"

        # ③ 拼完整路径（因为脚本和文件夹不在同一层）
        old_path = os.path.join(folder_path, name)       # "./test_files/photo_001.jpg"
        new_path = os.path.join(folder_path, new_name)   # "./test_files/IMG_photo_001.jpg"

        # ④ 执行改名
        os.rename(old_path, new_path)
        print(f"{name}  →  {new_name}")   # 打印改名记录

    # 不是 .jpg 的文件 → 跳过，什么也不做


# === 新概念速查 ===
#
# os.path.splitext("文件名")
#   作用：把文件名拆成（名字, 后缀）
#   例子："photo_001.jpg" → ("photo_001", ".jpg")
#         "music.mp3"     → ("music", ".mp3")
#
# f"...{变量}..."
#   作用：把变量值嵌入字符串模板
#   例子：f"IMG_{name_part}{ext_part}" → "IMG_photo_001.jpg"
#
# os.path.join("文件夹", "文件名")
#   作用：把文件夹路径和文件名拼成完整路径（自动处理 / 和 \ ）
#   例子：os.path.join("./test_files", "photo_001.jpg") → "./test_files/photo_001.jpg"
#
# os.rename(旧路径, 新路径)
#   作用：重命名文件
#   例子：os.rename("./test_files/photo_001.jpg", "./test_files/IMG_photo_001.jpg")


# === 本次执行流程图 ===
#
# os.listdir() → ["music.mp3", "notes.txt", "photo_001.jpg", "photo_002.jpg", "readme.md", "report.docx"]
#      ↓
# for name 逐个：
#   "music.mp3"       → if .jpg? → False → 跳过
#   "notes.txt"       → if .jpg? → False → 跳过
#   "photo_001.jpg"   → if .jpg? → True
#     ↓
#     ① splitext → ("photo_001", ".jpg")
#     ② f-string → "IMG_photo_001.jpg"
#     ③ join 路径 → "./test_files/photo_001.jpg" 和 "./test_files/IMG_photo_001.jpg"
#     ④ rename   → 文件改名 ✅
#     print "photo_001.jpg  →  IMG_photo_001.jpg"
#   "photo_002.jpg"   → 同上流程 ✅
#   "readme.md"       → if .jpg? → False → 跳过
#   "report.docx"     → if .jpg? → False → 跳过
