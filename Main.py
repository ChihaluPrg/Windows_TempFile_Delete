import os
import shutil

def is_file_in_use(file_path):
    try:
        # ファイルが使用中でないかを確認
        with open(file_path, 'r+'):
            return False
    except IOError:
        return True

def delete_temp_files(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                # サブディレクトリの場合は再帰的に削除
                delete_temp_files(item_path)
            else:
                # ファイルが使用中でない場合に削除
                if not is_file_in_use(item_path):
                    try:
                        os.remove(item_path)
                        print(f"削除しました: {item_path}")
                    except PermissionError:
                        print(f"アクセス権限エラー: {item_path} は削除できません。")
                    except FileNotFoundError:
                        print(f"ファイルが見つかりません: {item_path} は削除できません。")
                    except IsADirectoryError:
                        print(f"{item_path} はディレクトリです。")
                    except Exception as e:
                        print(f"{item_path} の削除に失敗しました: {e}")
                else:
                    print(f"使用中のため削除できません: {item_path}")
        # 空になったフォルダを削除
        try:
            os.rmdir(folder_path)
            print(f"フォルダを削除しました: {folder_path}")
        except PermissionError:
            print(f"アクセス権限エラー: {folder_path} は削除できません。")
        except FileNotFoundError:
            print(f"フォルダが見つかりません: {folder_path} は削除できません。")
        except Exception as e:
            print(f"{folder_path} の削除に失敗しました: {e}")
    else:
        print(f"{folder_path} は存在しないか、ディレクトリではありません。")

# 使用例
temp_folder_path = r'C:\Users\sakip\AppData\Local\Temp'
delete_temp_files(temp_folder_path)
