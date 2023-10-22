from bs4 import BeautifulSoup
import requests

def remove_html_tags(html):
    blocklist = [
        'style',
        'script',
        'img',
    ]
    soup = BeautifulSoup(html, 'html.parser')

    text = [t.strip() for t in soup.find_all(string=True) if t.parent.name not in blocklist and t.strip() != '']

    return text

def download_html(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            html_content = str(soup)

            return html_content
        else:
            print(f"Failed to retrieve HTML. Status code: {response.status_code}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    html_content = download_html(website_url)

    if html_content:
        text = remove_html_tags(html_content)
        for t in text:
            print(t)
