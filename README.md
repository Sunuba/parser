**INTRO**

- Parser will help you to scrap information from any website.
- Supports proxy


**CHANGES**
- To improve search **div.class.classname** changed to _**div.@class."classname"**_. This enables to search by text inside
any tag
- Class name changed to **Parser** from _**ParserClass**_
- Always wrap classname with double quotes. Example div.@class."classname"

**HOW TO USE IT**

    1. Create parser object
        from Parser import Parser
        
        parser = Parser('your-web-address')
        
        #if you want to use proxy, then
        parser = parser('your-web-address', use_proxy=True)
        
        Note: When you use proxy, class will grab list of all proxies 
        from https://free-proxy-list.net and randomly select one of them
        and use it.
    2. visit website that you want to grab data from and create a "route" to that information
        Example: Let's assume that your information resides inside the following structure:
                <div class="sample-class">
                    <span class="sample-text">Sample Text</span>
                </div>
        Then, your route will be div.@class."sample-class"/span.@class."sample-text" and 
        your indicator will be text() - because you want to reach out the text in span.
        so, sample_data = parser.prepare_sections('div.@class."sample-class"/span.@class."sample-text"', 'text()')
        print(sample_data) will give you what you need.
                Example 2:
                <div>
                    <span>Sample text</span>
                </div>
                would be div.@span with text() indicator
                sample_data = parser.prepare_sections('div.@span', 'text()') will do the job
    3. use get_data() method to grab data
    4. that is it. Just print data, save or do whatever you want to do.


**EXAMPLE 1**
    
    In this example, I will demonstrate how to get data from turbo.az - a website where all cars are sold in Azerbaijan, 
    it has an huge database of cars.
    
    from Parser import Parser
    parser = Parser(link='https://www.turbo.az/autos')
    # Here I want to grab information from turbo.az/autos, that is why I initialize class with this link.
    # Now, let's say that I am focused on getting all the names of cars that is added as a new car, I mean the entry is
    # fresh, not a vip or any sort of other advertised content.
    car_names = parser.prepare_sections('div.@class."products-container"/div.@class."products"//div.@class."products-description"/p.@class."products-name"', 'text()')
    # is what I need in this case. It is in the source code, you can check it by yourself as well.
    # I use parser.get_data() class to retrieve data.
    car_names = parser.get_data(car_names) #- this will return pyton list
    print(car_names)
    # Here is the output:
    # ['Mini Countryman', 'Hyundai Santa Fe', 'GAZ Next A65R32-40', 'Land Rover RR Evoque', 'BMW M3', 'Mercedes S 350', 'Chevrolet Cruze', 'Hyundai Sonata', 'Mercedes C 230', 'Kia Cerato', 'Kia Optima', 'Mercedes E 240', 'LADA (VAZ) 2104', 'Hyundai Elantra', 'GMC Yukon', 'LADA (VAZ) 2107', 'Mercedes C 220', 'BMW 318', 'LADA (VAZ) 2107', 'Toyota Prado', 'Daewoo Gentra', 'Mercedes C 200', 'Mercedes C 220', 'Mitsubishi L 200', 'Volkswagen Jetta', 'LADA (VAZ) 2107', 'Toyota Camry', 'Mercedes E 280', 'Hyundai Tucson', 'Hyundai ix35', 'LADA (VAZ) 2108', 'BMW 520', 'Mercedes E 240', 'Mercedes GL 500', 'BMW 523', 'Hyundai Accent']


**EXAMPLE 2**

    In this example I will demonstrate how to get data from http://quotes.toscrape.com/tag/inspirational/
    when I see source code, I quickly realise that the data I want to get is in the following code block
    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
        <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>
        <span>by <small class="author" itemprop="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
        </span>
        <div class="tags">
            Tags:
            <meta class="keywords" itemprop="keywords" content="inspirational,life,live,miracle,miracles" /    > 
            <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>            
            <a class="tag" href="/tag/life/page/1/">life</a>
            <a class="tag" href="/tag/live/page/1/">live</a>
            <a class="tag" href="/tag/miracle/page/1/">miracle</a>
            <a class="tag" href="/tag/miracles/page/1/">miracles</a>
        </div>
    </div>    
    
    It is inside a div (class="quote"), inside a span (class="text") and I need to access text inside the last tag.
    I quickly write my route like this: div.@class.quote/span.@class.text and indicator is text()
    quote_route = parser.prepare_sections('div.@class.quote/span.@class.text', 'text()')
    quotes = parser.get_data(quote_route)
    print(quotes)
    And the result:
        ['“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", "“I have not failed. I've just found 10,000 ways that won't work.”", "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", '“To the well-organized mind, death is but the next great adventure.”', '“It is never too late to be what you might have been.”', '“You can never get a cup of tea large enough or a book long enough to suit me.”', '“Only in the darkness can you see the stars.”', '“When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.”']
    
    for quote in quotes:
        print(quote)
 
    And the result:
    “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
    “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
    “I have not failed. I've just found 10,000 ways that won't work.”
    “This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”
    “The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”
    “To the well-organized mind, death is but the next great adventure.”
    “It is never too late to be what you might have been.”
    “You can never get a cup of tea large enough or a book long enough to suit me.”
    “Only in the darkness can you see the stars.”
    “When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.”


## Azərbaycan Dilində

1. Bu nümunədə oxu.az saytından xəbər başlıqlarını əldə etməyi göstərəcəm. İlk öncə saytın koduna baxıb, bizə lazım olan
məlumatı çıxarmalıyıq. Oxu.az-ın koduna baxdıqda aydın olur ki, bizə lazım olan məlumatlar aşağıda göstərilən kodlarda
yerləşir: 

        <section class="news-list">
                    <div class="news-i">
                        <a class="news-i-inner" href="/society/303149">
                            <div class="news-i-img-container">
                                <div class="news-i-img" style="background-image: url(https://assets.oxu.az/uploads/W1siZiIsIjIwMTkvMDMvMTIvMjEvNTAvNDkvODE5NDRjZDQtYTQxNi00MDE1LWE0MjItNzM4Y2E1MGQwYTU0LzUzNzIwMDY4XzIzMzU4NDU1NjMxMjcyMzZfOTAzNDM2MDg0MjY2OTI2MDgwMF9uLmpwZyJdLFsicCIsImVuY29kZSIsImpwZyIsIi1xdWFsaXR5IDgwIl0sWyJwIiwidGh1bWIiLCI2MjB4NDY1XHUwMDNlIl1d?sha=a1b653c35dbe463e)"></div>
                            </div>
                            <div class="news-i-content">
                                <div class="when">
                                    <div class="when-date">
                                        <div class="date-day">12&nbsp</div>
                                        <div class="date-month">Mar</div>
                                        <div class="date-year">2019</div>
                                    </div>
                                    <div class="when-time">21:56</div>
                                </div>
                                <div class="title">Şamaxıda bayram tonqalları qalanıb</div>
                                <div class="description"></div>
                            </div>
                        </a>
                    ...
        ...

Biz "Şamaxıda bayram tonqalları qalanıb" yazılan hissəni götürmək istəyirik. Eynilə də saytda olan bütün başlıqları.
Bu zaman yuxarıdan başlayaraq marşurutu çəkirik:

    section.@class."news-list"/div.@class."news-i"/a/div.@class."news-i-content"/div.@class."title"

yuxarıdakı marşuruta baxdıqda aydın olur ki, birinci elementin adı, sonra tag göstəricisi, sonra isə tag göstəricisinin
dəyəri ifadə edilib. Yəni section elementinin news-list klas tag-ı.
Digərləri də eyni qaydadadır. Daha sonra ən sonuncu elementin içərisindəki mətni götürəcəyimiz
üçün göstəricimiz də 'text()' olmalıdır. Daha detallı məlumat üçün
lxml haqqında oxuyun.

Beləliklə obyektimizi yaradıb məlumat əldə edə bilərik

    from Parser import Parser
    
    parser = Parser('https://oxu.az')
    
    # proksi ilə istifadə etmək üçün
    parser = Parser('https://oxu.az', use_proxy=True)
    marshurut = 'section.@class."news-list"/div.@class."news-i"/a/div.@class."news-i-content"/div.@class."title"'
    xeber_marshurutu = parser.prepare_sections(marshurut, 'text()')    
    xeber_basliqlari = parser.get_data(xeber_marshurutu)
    
    for basliq in xeber_basliqlari:
        print(basliq)


Bu zaman aşağıdakı nəticəni əldə edəcəksiniz:

    Azərbaycanda keçirilən “Hackathon”nun qalibi 4 min manat qazanacaq
    Şamaxıda bayram tonqalları qalanıb
    Lənkəranda 45 yaşlı kişi çayda boğuldu
    Türkiyə səmada olan “Boeing 737 Max 8” təyyarələrini geri çağırıb
    Sabah Abşeron və Sumqayıtın bir hissəsində qaz olmayacaq 
    Meyitlərdən orqanların götürülməsi işini hansı qurum həyata keçirilməlidir?
    Zülfiyyə Hüseynova Bakıdakı Qran-Pridə güləşəcək
    Astarada iribuynuzlu heyvanlarda xəstəlik aşkar edilib - FOTO
    Deputat: Ağa qara deməkdən usanın
    Ən çirkli havası olan ölkələr açıqlandı
    XİN: Paşinyanın “Qarabağ erməniliyi” fikri söz oyununa son qoydu
    Azərbaycanlı kapitan Bosfor boğazını bağlamaqla hədələyir - VİDEO
    Naxçıvanda binaların dam örtükləri təmir ediləcək
    Binaların lift təsərrüfatı yaxşılaşdırılacaq - SƏRƏNCAM
    Prezident iki şairə vəzifə verdi
    Şahmat Olimpiya Oyunlarına bir qədər də yaxınlaşdı
    İlham Əliyev Roma Papasına məktub göndərdi
    Mərkəzi Bank Fransa bankı ilə müqavilə bağladı
    Bakı Aeroportunda yeni texnologiyalar tətbiq ediləcək
    Mehriban Əliyeva Nikola Sarkozi ilə görüşdü - YENİLƏNİB + FOTO
    Bakıya uçan təyyarəyə külli miqdarda pul keçirmək istədi, saxlanıldı
    Yollardakı xətlər yenilənir - VİDEO
    Daha bir təyyarə qəzası: bu dəfə Çində - Ölənlər var

**NÜMUNƏ**

Bu nümunə tap.az saytında olan reklam başlıqlarını götürür.
    from Parser import Parser
    
    
    parser = Parser('https://tap.az/all')
    
    product_name_route = 'div.@class."endless-products"/div.@class."products-i"/a.@class."products-link"/div.@class."products-name"'
    product_names = parser.prepare_sections(product_name_route, 'text()')
    product_name = parser.get_data(product_names)
    print(product_name)
    
    for name in product_name:
        print(name)
    
    Nəticə:
    ['Böyüdücü məcun "Cennol"', 'Power bank "Xiaomi"', '"BMW F22" hava yastığı', 'Apple iPhone 5S', '4-otaqlı yeni tikili, 8 mkr., 179 m²', 'Dondurucu', 'Pianinolar', 'Həyət evi kirayə verilir, Qusar r.', 'Həyət evi kirayə verilir, Qusar r.', 'Soyuducu ', 'Uşaq avtomobili', '"Tissot" qol saatı', 'Su çəni', 'Mercedes 190, 1990 il', 'Haski', 'Obyekt icarəyə verilir, Gənclik m.', '3-otaqlı mənzil, Gənclik m., 58 m²', 'Konfet qabı', 'Mətbəx masası', '3-otaqlı yeni tikili, Həzi Aslanov m., 106 m²', 'CD-maqnitola', 'Apple MacBook Pro 15-inch, Mid 2012', 'Honda CR-V, 2005 год', 'Çörək qabı', '"Hyundai Elantra" diski', 'Apple iPhone 7 Red', '3-otaqlı yeni tikili, Həzi Aslanov m., 109 m²', 'Samsung Galaxy A6', 'Həyət evi kirayə verilir, Qusar r.', 'Kinroad, 2015 il', 'Lazer epilyasiya cihazları', 'Nasos', 'Ofis mebeli', 'Həyət evi, Zabrat 1 qəs.', 'Leagoo Kiicaa', '"Naviforce" qol saatı', 'Nissan Teana, 2008 il', '"Mercedes" diskləri - R18', '"Samsung" paltaryuyan', '"BMW F31" hava yastığı', '2-otaqlı yeni tikili, N. Nərmanov m., 106 m²', 'Həyət evi kirayə verilir, Qusar r.', '3-otaqlı mənzil, Sumqayıt ş., 72 m²', 'Mühərrik', '"Audemars Piguet" qol saatı', '"Volkswagen" qapı əlcəkləri', 'Həyət evi, Binəqədi qəs.', 'Avtomobil oturacaq üzlüyü']
    Böyüdücü məcun "Cennol"
    Power bank "Xiaomi"
    "BMW F22" hava yastığı
    Apple iPhone 5S
    4-otaqlı yeni tikili, 8 mkr., 179 m²
    Dondurucu
    Pianinolar
    Həyət evi kirayə verilir, Qusar r.
    Həyət evi kirayə verilir, Qusar r.
    Soyuducu 
    Uşaq avtomobili
    "Tissot" qol saatı
    Su çəni
    Mercedes 190, 1990 il
    Haski
    Obyekt icarəyə verilir, Gənclik m.
    3-otaqlı mənzil, Gənclik m., 58 m²
    Konfet qabı
    Mətbəx masası
    3-otaqlı yeni tikili, Həzi Aslanov m., 106 m²
    CD-maqnitola
    Apple MacBook Pro 15-inch, Mid 2012
    Honda CR-V, 2005 год
    Çörək qabı
    "Hyundai Elantra" diski
    Apple iPhone 7 Red
    3-otaqlı yeni tikili, Həzi Aslanov m., 109 m²
    Samsung Galaxy A6
    Həyət evi kirayə verilir, Qusar r.
    Kinroad, 2015 il
    Lazer epilyasiya cihazları
    Nasos
    Ofis mebeli
    Həyət evi, Zabrat 1 qəs.
    Leagoo Kiicaa
    "Naviforce" qol saatı
    Nissan Teana, 2008 il
    "Mercedes" diskləri - R18
    "Samsung" paltaryuyan
    "BMW F31" hava yastığı
    2-otaqlı yeni tikili, N. Nərmanov m., 106 m²
    Həyət evi kirayə verilir, Qusar r.
    3-otaqlı mənzil, Sumqayıt ş., 72 m²
    Mühərrik
    "Audemars Piguet" qol saatı
    "Volkswagen" qapı əlcəkləri
    Həyət evi, Binəqədi qəs.
    Avtomobil oturacaq üzlüyü


    