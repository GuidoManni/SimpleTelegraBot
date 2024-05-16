from typing import Final
import requests
from PIL import Image
import io

class STB:
    def __init__(self, token: str, user_id: int, job_id: int = 0):
        self.token = token
        self.talk_only_with = user_id
        self.job_id = job_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.talk_only_with}&text={message}"
        requests.get(url).json()  # this sends the message

    def _prepare_image_for_sending(self, img):
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        return img_bytes

    def send_image(self, image_path: str):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto?chat_id={self.talk_only_with}"
        img = Image.open(image_path)
        img_bytes = self._prepare_image_for_sending(img)
        files = {'photo': img_bytes}
        requests.post(url, files=files)

    def _prepare_file_for_sending(self, file_path: str):
        with open(file_path, 'r') as file:
            err_content = file.read()
            txt_file = io.BytesIO(err_content.encode('utf-8'))
            file_name = file_path.split('/')[-1].replace('.err', '.txt')
            return txt_file, file_name

    def send_file(self, file_path: str):
        url = f"https://api.telegram.org/bot{self.token}/sendDocument?chat_id={self.talk_only_with}"
        txt_file, file_name = self._prepare_file_for_sending(file_path)
        files = {'document': (file_name, txt_file)}
        requests.post(url, files=files)
