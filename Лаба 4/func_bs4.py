from bs4 import BeautifulSoup
def extract_page_title(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
    return soup.title.string if soup.title else "Немає заголовка"
