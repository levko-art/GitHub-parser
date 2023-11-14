import random

import requests


class GitHubCrawler:
    def __init__(self, keywords, proxies, search_type):
        self.keywords = keywords
        self.proxies = proxies
        self.search_type = search_type

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def search_github(self):
        results = []

        for keyword in self.keywords:
            url = f'https://github.com/search?q={keyword}&type={self.search_type}'
            proxy = self.get_random_proxy()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            try:
                response = requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers, timeout=10)
                response.raise_for_status()

                json_data = response.json()

                search_results = json_data['payload']['results']

                for result in search_results:
                    repo_url = f'https://github.com/{result["repo"]["repository"]["owner_login"]}/{result["repo"]["repository"]["name"]}'
                    results.append({'url': repo_url})
            except requests.RequestException as e:
                print(f"Error: {e}")

        return results


if __name__ == '__main__':
    crawler = GitHubCrawler(
        keywords=['css'],
        proxies=['8.209.114.72:3129'],
        search_type='Repositories'
    )
    results = crawler.search_github()
    print(results)
