from bs4 import BeautifulSoup
import requests as re


def main():
    base = "https://ru.stackoverflow.com/questions"
    base_for_links = "https://ru.stackoverflow.com"
    html = re.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    questions = soup.find('div', id='questions')
    questions_summary = questions.find_all('a', class_='s-link')
    for q in questions_summary:
        print(q.text)
        print(base_for_links + q.get('href'))
        print('-'*40)


if __name__ == "__main__":
    main()
