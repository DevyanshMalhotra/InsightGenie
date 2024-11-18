import requests
from bs4 import BeautifulSoup

def google_search(query):
    """
    Perform a Google search and return snippets filtered for relevance.
    """
    try:
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract search snippets
        snippets = [snippet.get_text() for snippet in soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")]
        return snippets[:5] if snippets else ["No relevant results found."]
    except Exception as e:
        return [f"Error during search: {e}"]

