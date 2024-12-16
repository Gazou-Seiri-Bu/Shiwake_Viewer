import glob
import os
import sys
import piexif
import piexif.helper
from PIL import Image, PngImagePlugin
from datetime import datetime
from pywintypes import Time

# Windowsの場合
on_windows = os.name == 'nt'
if on_windows:
    import win32file
    import win32con

# WEBP品質
WEBP_QUALITY = 80
# 画像形式
IMG_INPUT_FORMAT = 'PNG'
IMG_OUTPUT_FORMAT = 'WEBP'
# 画像拡張子
IMG_INPUT_FILENAME_EXT = 'png'
IMG_OUTPUT_FILENAME_EXT = 'webp'

# コマンドライン引数でフォルダパスを取得
if len(sys.argv) != 2:
    print("使い方: python script.py <フォルダパス>")
    sys.exit(1)

input_dir = sys.argv[1]
if not os.path.isdir(input_dir):
    print(f"指定されたパスはフォルダではありません: {input_dir}")
    sys.exit(1)

# 入力フォルダと出力フォルダ
input_dir = os.path.abspath(input_dir)
folder_name = os.path.basename(input_dir)  # フォルダ名を取得
parent_dir = os.path.dirname(input_dir)  # 親ディレクトリを取得
output_dir = os.path.join(parent_dir, folder_name + '-webp')  # 親ディレクトリに `-webp` フォルダを作成
os.makedirs(output_dir, exist_ok=True)

# 画像を配列に格納
files = glob.glob(os.path.join(input_dir, '*.' + IMG_INPUT_FILENAME_EXT))

# 対象画像の変換・保存
for file in files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    output_file_name = file_name + '.' + IMG_OUTPUT_FILENAME_EXT
    output_file_path = os.path.join(output_dir, output_file_name)

    def get_png_info(file):
        try:
            # 画像を開く
            img = Image.open(file)

            # PngImagePluginの情報を取得
            png_info = img.info

            # ファイルを閉じる
            img.close()

            return png_info

        except Exception as e:
            print(f"画像を開けませんでした。: {e}")
            return None

    # PNGファイルからpnginfoを取得
    png_info = get_png_info(file)

    # 画像を開く
    image = Image.open(file)

    # 日時情報を取得
    access_time   = os.path.getatime(file) # アクセス日時
    modify_time   = os.path.getmtime(file) # 更新日時

    if on_windows:
        creation_time = os.path.getctime(file) # 作成日時

    # WEBPに変換
    image.save(output_file_path, IMG_OUTPUT_FORMAT, quality=WEBP_QUALITY)

    # 画像を閉じる
    image.close()

    # WEBPファイルにExifデータ（PNG Info）を保存する
    if png_info is not None:
        # pnginfoの各項目を改行区切りで連結
        png_info_data = ""
        for key, value in png_info.items():
            if key == 'parameters':
                # Automatic1111形式の場合
                png_info_data += f"{value}\n"
            else:
                # NovelAI形式の場合
                png_info_data += f"{key}: {value}\n"

        png_info_data = png_info_data.rstrip()

        # Exifデータを作成
        exif_dict = {"Exif": {piexif.ExifIFD.UserComment: piexif.helper.UserComment.dump(png_info_data or '', encoding='unicode')}}

        # Exifデータをバイトに変換
        exif_bytes = piexif.dump(exif_dict)

        # Exifデータを挿入して新しい画像を保存
        piexif.insert(exif_bytes, output_file_path)

    else:
        print("PNG情報を取得できませんでした。")

    # 日付情報の設定
    # WEBPファイルのハンドルを取得（Windowsのみ）
    if on_windows:
        handle = win32file.CreateFile(
            output_file_path,
            win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            0,
            None
        )

        # WEBPファイルに元画像の作成日時、アクセス日時、更新日時を設定
        win32file.SetFileTime(handle, Time(creation_time), Time(access_time), Time(modify_time))

        # ハンドルを閉じる
        handle.Close()

    # 他のプラットフォームではアクセス日時と更新日時を設定
    os.utime(output_file_path, (access_time, modify_time))

print(f"変換が完了しました。WEBPファイルは {output_dir} に保存されました。")
