import os

files = {
    "func_math.py": 'import math\ndef calculate_circle_area(radius):\n    return math.pi * math.pow(radius, 2)\n',
    "func_datetime.py": 'import datetime\ndef get_current_timestamp():\n    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")\n',
    "func_os.py": 'import os\ndef list_current_directory():\n    return os.listdir(".")\n',
    "func_json.py": 'import json\ndef convert_dict_to_json(data_dict):\n    return json.dumps(data_dict, indent=4)\n',
    "func_random.py": 'import random\ndef get_random_element(elements_list):\n    return random.choice(elements_list)\n',
    "func_requests.py": 'import requests\ndef check_site_status(url):\n    try: return requests.get(url, timeout=5).status_code\n    except: return 404\n',
    "func_numpy.py": 'import numpy as np\ndef calculate_vector_mean(lst):\n    return float(np.mean(np.array(lst)))\n',
    "func_pandas.py": 'import pandas as pd\ndef create_simple_dataframe():\n    return pd.DataFrame({"Ім\'я": ["Олег", "Анна"], "Бал": [95, 88]}).to_string()\n',
    "func_matplotlib.py": 'import matplotlib.pyplot as plt\ndef save_simple_plot(filename="plot.png"):\n    plt.plot([1, 2, 3], [4, 5, 6])\n    plt.title("Тестовий графік")\n    plt.savefig(filename)\n    plt.close()\n    return f"Графік збережено у {filename}"\n',
    "func_pydantic.py": 'from pydantic import BaseModel\nclass User(BaseModel):\n    id: int\n    name: str\ndef validate_user_data(user_id, name):\n    return User(id=user_id, name=name).model_dump()\n',
    "func_loguru.py": 'from loguru import logger\ndef log_demo_message(msg):\n    logger.info(f"Лог: {msg}")\n    return "Записано в лог"\n',
    "func_tqdm.py": 'import time\nfrom tqdm import tqdm\ndef run_progress_bar():\n    for _ in tqdm(range(5), desc="Обробка"): time.sleep(0.05)\n    return "Успішно"\n',
    "func_colorama.py": 'from colorama import Fore, Style, init\ndef get_colored_text(text):\n    init(autoreset=True)\n    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"\n',
    "func_pillow.py": 'from PIL import Image\ndef create_blank_image(filename="blank.png"):\n    Image.new("RGB", (100, 100), color="red").save(filename)\n    return f"Зображення створено: {filename}"\n',
    "func_bs4.py": 'from bs4 import BeautifulSoup\ndef extract_page_title(html_string):\n    soup = BeautifulSoup(html_string, "html.parser")\n    return soup.title.string if soup.title else "Немає заголовка"\n',
    "requirements.txt": "beautifulsoup4==4.12.3\ncolorama==0.4.6\nloguru==0.7.2\nmatplotlib==3.8.2\nnumpy==1.26.2\npandas==2.1.4\nPillow==10.1.0\npydantic==2.5.2\nrequests==2.31.0\ntqdm==4.66.1\n",
    "main.py": """from func_math import calculate_circle_area
from func_datetime import get_current_timestamp
from func_os import list_current_directory
from func_json import convert_dict_to_json
from func_random import get_random_element
from func_requests import check_site_status
from func_numpy import calculate_vector_mean
from func_pandas import create_simple_dataframe
from func_matplotlib import save_simple_plot
from func_pydantic import validate_user_data
from func_loguru import log_demo_message
from func_tqdm import run_progress_bar
from func_colorama import get_colored_text
from func_pillow import create_blank_image
from func_bs4 import extract_page_title

def main():
    print("--- ВИКЛИК ВБУДОВАНИХ БІБЛІОТЕК ---")
    print(f"1. math: Площа кола r=5 -> {calculate_circle_area(5):.2f}")
    print(f"2. datetime: Поточний час -> {get_current_timestamp()}")
    print(f"3. os: Файли в директорії -> {list_current_directory()[:3]}")
    print(f"4. json: JSON ->\\n{convert_dict_to_json({'status': 'ok', 'code': 200})}")
    print(f"5. random: Елемент -> {get_random_element(['яблуко', 'банан', 'груша'])}")
    print("\\n--- ВИКЛИК СТОРОННІХ БІБЛІОТЕК ---")
    print(f"6. requests: Код google.com -> {check_site_status('https://www.google.com')}")
    print(f"7. numpy: Середнє значення -> {calculate_vector_mean([10, 20, 30])}")
    print(f"8. pandas: Датафрейм ->\\n{create_simple_dataframe()}")
    print(f"9. matplotlib: {save_simple_plot()}")
    print(f"10. pydantic: Валідація -> {validate_user_data(1, 'Максим')}")
    print(f"11. loguru: {log_demo_message('Тест')}")
    print(f"12. tqdm: {run_progress_bar()}")
    print(f"13. colorama: {get_colored_text('Зелений текст!')}")
    print(f"14. pillow: {create_blank_image()}")
    print(f"15. bs4: Заголовок -> {extract_page_title('<html><title>Моя Лаба</title></html>')}")

if __name__ == '__main__':
    main()
"""
}

for name, content in files.items():
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)
print("Усі 16 файлів успішно створено!")
