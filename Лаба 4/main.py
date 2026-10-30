from func_math import calculate_circle_area
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
    print(f"4. json: JSON ->\n{convert_dict_to_json({'status': 'ok', 'code': 200})}")
    print(f"5. random: Елемент -> {get_random_element(['яблуко', 'банан', 'груша'])}")
    print("\n--- ВИКЛИК СТОРОННІХ БІБЛІОТЕК ---")
    print(f"6. requests: Код google.com -> {check_site_status('https://www.google.com')}")
    print(f"7. numpy: Середнє значення -> {calculate_vector_mean([10, 20, 30])}")
    print(f"8. pandas: Датафрейм ->\n{create_simple_dataframe()}")
    print(f"9. matplotlib: {save_simple_plot()}")
    print(f"10. pydantic: Валідація -> {validate_user_data(1, 'Максим')}")
    print(f"11. loguru: {log_demo_message('Тест')}")
    print(f"12. tqdm: {run_progress_bar()}")
    print(f"13. colorama: {get_colored_text('Зелений текст!')}")
    print(f"14. pillow: {create_blank_image()}")
    print(f"15. bs4: Заголовок -> {extract_page_title('<html><title>Моя Лаба</title></html>')}")

if __name__ == '__main__':
    main()
