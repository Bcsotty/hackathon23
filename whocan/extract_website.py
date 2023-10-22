from bs4 import BeautifulSoup
import requests


def _remove_html_tags(html: str) -> list[str]:
    blocklist = [
        'style',
        'script',
        'img',
        '[document]',
        'meta'
    ]
    soup = BeautifulSoup(html, 'html.parser')

    text = [t.strip() for t in soup.find_all(string=True) if t.parent.name not in blocklist and t.strip() != '']

    return text


def _download_html(url: str) -> str | None:
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


def extract_website_text(url: str) -> list[str] | None:
    html_content = _download_html(url)
    if html_content:
        text = _remove_html_tags(html_content)

        return text


if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    text = extract_website_text(website_url)

    if text:
        for t in text:
            print(t)
