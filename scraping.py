from bs4 import BeautifulSoup
import requests


class Billboard:
    def __init__(self, date):
        self.date = date
        self.url = "https://www.billboard.com/charts/hot-100/" + date + "/"
        self.soup = self._get_url()
        self.billboard = self.scrape_billboard()

    def _get_url(self):
        response = requests.get(self.url).text
        return BeautifulSoup(response, 'html.parser')

    def scrape_billboard(self):
        billboard = []
        first = self.find_first_song()
        billboard.append(first)

        charts = self.soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
                                                      "lrv-u-flex-direction-column lrv-u-justify-content-center "
                                                      "lrv-u-border-b-1 u-border-b-0@mobile-max "
                                                      "lrv-u-border-color-grey-light lrv-u-padding-l-050 "
                                                      "lrv-u-padding-l-1@mobile-max")
        for chart in charts:
            song = chart.find(name="h3").get_text().strip()
            artist = chart.find(name='span').getText().strip()
            billboard.append([song,artist])
        return billboard

    def find_first_song(self):
        first = self.soup.find(class_="u-flex@mobile-max")
        song = first.find(name="a").getText().strip()
        artist = first.find(name="p").getText().strip()

        return [song, artist]

    def print_billboard(self):
        for i in self.billboard:
            print(f"Song: {i[0]}, Artist: {i[1]}")
