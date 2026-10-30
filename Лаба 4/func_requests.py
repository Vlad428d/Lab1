import requests
def check_site_status(url):
    try: return requests.get(url, timeout=5).status_code
    except: return 404
