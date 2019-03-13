from Parser import Parser

parser = Parser('https://oxu.az')

header_route = 'section.@class.news-list/div.@class.news-i/a/div.@class.news-i-content/div.@class.title'
header_prepare = parser.prepare_sections(header_route, 'text()')
headers = parser.get_data(header_prepare)

for header in headers:
    print(header)
