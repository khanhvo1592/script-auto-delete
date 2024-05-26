import os
import time
import yaml
import logging

# Thiết lập logging
logging.basicConfig(
    filename='delete_files.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info("Loaded configuration successfully.")
        return config
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        raise


def delete_old_files(folder_path, seconds):
    now = time.time()
    cutoff = now - seconds
    deleted_files = []

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_modified_time = os.path.getmtime(file_path)
            logging.info(f"Checking file: {file_path} (Last modified: {time.ctime(file_modified_time)})")
            if file_modified_time < cutoff:
                try:
                    os.remove(file_path)
                    logging.info(f"Deleted {file_path}")
                    deleted_files.append(file_path)
                except Exception as e:
                    logging.error(f"Failed to delete {file_path}: {e}")

    if deleted_files:
        logging.info(f"Total files deleted: {len(deleted_files)}")
        logging.info("Deleted files:\n" + "\n".join(deleted_files))
    else:
        logging.info("No files were deleted.")


if __name__ == "__main__":
    config_path = "config.yaml"
    try:
        config = load_config(config_path)
        logging.info("Configuration loaded.")
        logging.info(f"Folder path: {config.get('folder_path')}")
        logging.info(f"Seconds: {config.get('seconds')}")

        folder_path = config.get('folder_path')
        seconds = config.get('seconds')

        delete_old_files(folder_path, seconds)
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
