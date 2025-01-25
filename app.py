import os
import shutil
import requests
from datetime import datetime
import pytz
import schedule
import time
import zipfile

def create_github_release(repo_path, git_config):
    """
    Создает релиз в GitHub
    """
    try:
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz)
        
        archive_name = f"auto_build_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}"
        archive_path = os.path.join(repo_path, f"{archive_name}.zip")
        
        # Создание временной директории без archives
        temp_dir = os.path.join(repo_path, 'temp_build')
        os.makedirs(temp_dir, exist_ok=True)
        
        # Копирование файлов, исключая archives
        for item in os.listdir(repo_path):
            if item != 'archives' and item != 'temp_build':
                s = os.path.join(repo_path, item)
                d = os.path.join(temp_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
        
        # Архивация временной директории
        shutil.make_archive(archive_path[:-4], 'zip', temp_dir)
        
        # Удаление временной директории
        shutil.rmtree(temp_dir)
        
        release_data = {
            "tag_name": archive_name,
            "target_commitish": "main",
            "name": f"Build {archive_name}",
            "body": f"Автоматическая сборка от {current_time.strftime('%Y-%m-%d %H:%M:%S')}",
            "draft": False,
            "prerelease": False
        }
        
        url = f"https://api.github.com/repos/{git_config['username']}/{git_config['repo']}/releases"
        
        headers = {
            "Authorization": f"token {git_config['token']}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.post(url, json=release_data, headers=headers)
        
        if response.status_code == 201:
            release_info = response.json()
            upload_url = release_info['upload_url'].replace('{?name,label}', f'?name={archive_name}.zip')
            
            with open(archive_path, 'rb') as file:
                upload_response = requests.post(
                    upload_url, 
                    headers={
                        "Authorization": f"token {git_config['token']}",
                        "Content-Type": "application/zip"
                    }, 
                    data=file
                )
            
            if upload_response.status_code in [200, 201]:
                print(f"Успешно создан релиз: {archive_name}")
                
                # Удаление архива после успешной загрузки
                os.remove(archive_path)
                print(f"Архив {archive_name}.zip был удален.")
                return True
            else:
                print("Ошибка загрузки архива")
                return False
        else:
            print(f"Ошибка создания релиза: {response.text}")
            return False
    
    except Exception as e:
        print(f"Общая ошибка: {e}")
        return False

def daily_release():
    """Ежедневное создание релиза"""
    repo = {
        "path": r"C:\build", 
        "git_config": {
            "username": "xdghrj",
            "repo": "auto_build_test",
            "token": "ghp_XXXXXXXXXXXXXXXXXXXXX"
        }
    }
    
    create_github_release(repo['path'], repo['git_config'])

def main():
    schedule.every().day.at("23:00").do(daily_release)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
