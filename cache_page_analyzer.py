import json
import urllib.request
from html.parser import HTMLParser
from ciphers import caesar
from bs4 import BeautifulSoup


class GeocacheHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        print(self.getpos())

    def handle_endtag(self, tag):
        print("End tag :", tag)
        print(self.getpos())
        # pass

    def handle_startendtag(self, tag, attrs):
        print("Self enclosed tag :", tag)
        print(self.getpos())

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        pass


def build_report(geocache_html: str) -> str:
    parser = GeocacheHTMLParser()
    parser.feed(geocache_html)
    return 'FEEDING DONE'
    html = BeautifulSoup(raw_html, 'html.parser')

    cache_id = html.find(id='ctl00_ContentBody_CoordInfoLinkControl1_uxCoordInfoCode').get_text(strip=True)
    cache_name = html.find(id='ctl00_ContentBody_CacheName').get_text(strip=True)
    hidden_by = html.find(id='ctl00_ContentBody_mcd1').get_text().split()[3]
    date_hidden = html.find(id='ctl00_ContentBody_mcd2').get_text().split()[2]
    difficulty_and_terrain = html.find(id='ctl00_ContentBody_diffTerr').find_all('span')
    cache_difficulty = difficulty_and_terrain[0].img['alt'].split()[0]
    cache_terrain = difficulty_and_terrain[1].img['alt'].split()[0]
    cache_size = html.find(id='ctl00_ContentBody_size').p.span.img['title'].split()[1]

    attribute_images = html.find(id='ctl00_ContentBody_detailWidget').find_all('img')
    cache_attributes = []
    for image in attribute_images:
        attribute = image['alt']
        if attribute != 'blank':
            cache_attributes.append(attribute)

    try:
        background_img_url = html.body['background']
    except KeyError:
        background_img_url = 'N/A'

    try:
        related_web_page = html.find(id='ctl00_ContentBody_uxCacheUrl')['href']
    except TypeError:
        related_web_page = 'N/A'

    short_description = html.find(id='ctl00_ContentBody_ShortDescription').prettify()
    long_description = html.find(id='ctl00_ContentBody_LongDescription').prettify()

    encrypted_hint = html.find(id='div_hint').get_text(strip=True)
    decrypted_hint = caesar.decrypt(encrypted_hint, 13) if len(encrypted_hint) > 0 else 'N/A'

    return  f"\n{cache_id} - {cache_name}\n" +\
            f"---\n" +\
            f"Hidden by: \"{hidden_by}\" on {date_hidden}\n" +\
            f"Diffuculty: {cache_difficulty}, Terrain: {cache_terrain}, Size: {cache_size}\n" +\
            f"Cache hint: {decrypted_hint}\n" +\
            f"Background image URL: {background_img_url}\n" +\
            f"Related webpage URL: {related_web_page}\n" +\
            f"Attributes: {cache_attributes}\n" +\
            f"---\n" +\
            f"Short description: \n{short_description}\n" +\
            f"Long description: \n{long_description}\n"


def fetch_html(gc_id: str):
    with open(".auth.json", "r",) as auth_file:
        auth_json = json.loads(auth_file.read())
    jwt = auth_json['gc_jwt']

    ###########################################################################################
    ##### TEMPORARY WHILE TESTING TO PREVENT EXTRA HTTP CALLS #################################
    # request = urllib.request.Request(f'https://www.geocaching.com/geocache/{gc_id}', headers={'Cookie':f'jwt={jwt}'}, method='GET')
    # response = urllib.request.urlopen(request)
    # html = response.read().decode('utf-8')
    # with open(f'{gc_id.upper()}.html', "w") as file:
    #     file.write(html)
    # return html
    ###########################################################################################
    with open(f'{gc_id.upper()}.html', "r") as file:
        return file.read()
    ##### TEMPORARY WHILE TESTING TO PREVENT EXTRA HTTP CALLS #################################
    ###########################################################################################
    request = urllib.request.Request(f'https://www.geocaching.com/geocache/{gc_id}', headers={'Cookie':f'jwt={jwt}'}, method='GET')
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


if __name__ == '__main__':
    muffin = 'GC4XZ37'
    squatch = 'GC4YRP4'
    odd_even = 'GC8KD18'
    test = 'GCTEST'

    html = fetch_html(test)
    report = build_report(html)
    print(report)