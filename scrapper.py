from ParserClass import Parser


parser = Parser(link='https://www.turbo.az/autos')

link_code = '//div[@class="products-container"]//div[@class="products"][3]//a//@href'
price_code = '//div[@class="products-container"]//div[@class="products"][3]//div[@class="product-price"]//text()'
car_names = '//div[@class="products-container"]//div[@class="products"][3]//div[@class="products-description"]//p[@class="products-name"]//text()'
atts_code = '//div[@class="products-container"]//div[@class="products"][3]//div[@class="products-description"]//div[@class="products-attributes"]//p[@class="products-attributes-i"]//text()'


car_names = parser.get_data(link_code)

print(car_names)
