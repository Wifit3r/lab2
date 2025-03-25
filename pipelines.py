import os
import requests
import scrapy
import sqlite3
from itemadapter import ItemAdapter


class Lab2Pipeline:
    def process_item(self, item, spider):
        return item


class ImagePipeline:
    def process_item(self, item, spider):
        if 'img_url' in item:
            img_url = item['img_url']
            img_name = img_url.split('/')[-1]
            response = requests.get(img_url)
            if response.status_code == 200:
                os.makedirs('images', exist_ok=True)
                img_path = os.path.join('images', img_name)
                with open(img_path, 'wb') as f:
                    f.write(response.content)
            else:
                spider.logger.error(f"Не вдалося завантажити фото: {img_url}")
        return item
    
import sqlite3

import sqlite3
import requests

class DBPipeline:
    def open_connect(self, spider):
        try:
            self.conn = sqlite3.connect('news.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS news 
                (title TEXT, url TEXT, date TEXT, img_url TEXT, img_name TEXT, image BLOB)'''
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error opening database connection: {e}")

    def close_connect(self, spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        try:
            img_data = None
            if item['img_url']:
                response = requests.get(item['img_url'])
                if response.status_code == 200:
                    img_data = response.content
            
            self.cursor.execute(
                '''INSERT INTO news (title, url, date, img_url, img_name, image) 
                VALUES (?, ?, ?, ?, ?, ?)''', 
                (item['title'], item['url'], item['date'], item['img_url'], item.get('img_name', None), img_data)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting data into database: {e}")
        return item