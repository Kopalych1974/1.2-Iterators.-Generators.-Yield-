'''
Задача:
Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии. 
Записывает в файл пару: страна – ссылка.
'''



import json
import wikipediaapi


class LinkOfPpage:

    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.wiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl

        return country, country_link



if __name__ == '__main__':
    output_file = open('links_to_country_pages.txt', 'w', encoding='utf-8')
    print ("Идет поиск страницы из Википедии по каждой стране из файла countries.json.")
    for country, item in LinkOfPpage('countries.json', 0):
        output_file.write(str(country) + '\t —> \t' + ' Link of page' + '\t —> \t' + str(item) + '\n')
        print('.', end='', flush=True)

    output_file.close()
