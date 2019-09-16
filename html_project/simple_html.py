from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet</p>
<p>Another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Anne</li>
    <li>Jen</li>
    <li>Charlie</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_item = [li.string for li in list_items]
    print(list_item)


def find_subtitle():
    para = simple_soup.find('p', {'class':'subtitle'})
    print(para.string)


def find_other_para():
    para = simple_soup.findAll('p')
    other_para = [p for p in para if 'subtitle' not in p.attrs.get('class', [])]
    print(other_para[0].string)


find_title()
find_list_items()
find_subtitle()
find_other_para()