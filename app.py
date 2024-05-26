import os
import time
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def delete_old_files(folder_path, seconds):
    now = time.time()
    cutoff = now - seconds

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_modified_time = os.path.getmtime(file_path)
            print(f"Checking file: {file_path}")
            print(f"Last modified time: {time.ctime(file_modified_time)}")
            print(f"Cutoff time: {time.ctime(cutoff)}")
            if file_modified_time < cutoff:
                try:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
if __name__ == "__main__":
    config_path = "config.yaml"
    config = load_config(config_path)

    # Kiểm tra nội dung file cấu hình
    print("Cấu hình đã tải:")
    print(f"Thư mục: {config.get('folder_path')}")
    print(f"Số giây: {config.get('seconds')}")

    folder_path = config.get('folder_path')
    seconds = config.get('seconds')

    delete_old_files(folder_path, seconds)
