**INTRO**

ParserClass will help you to scrap information from any website.

**HOW TO USE IT**

    1. Create parser object
    2. visit website that you want to grab data from and create a "route" to that information
        Example: Let's assume that your information resides inside the following structure:
                <div class="sample-class">
                    <span class="sample-text">Sample Text</span>
                </div>
        Then, your route will be div.class.sample-class/span.class.sample-text and 
        your indicator will be text() - because you want to reach out the text in span.
        so, sample_data = parser.prepare_sections('div.class.sample-class/span.class.sample-text', 'text()')
        print(sample_data) will give you what you need.
                Example 2:
                <div>
                    <span>Sample text</span>
                </div>
                would be div.span with text() indicator
                sample_data = parser.prepare_sections('div.span', 'text()') will do the job
    3. use get_data() method to grab data
    4. that is it. Just print data, save or do whatever you want to do.


**EXAMPLE 1**
    
    In this example, I will demonstrate how to get data from turbo.az - a website where all cars are sold in Azerbaijan, 
    it has an huge database of cars.
    
    from ParserClass import Parser
    parser = Parser(link='https://www.turbo.az/autos')
    # Here I want to grab information from turbo.az/autos, that is why I initialize class with this link.
    # Now, let's say that I am focused on getting all the names of cars that is added as a new car, I mean the entry is
    # fresh, not a vip or any sort of other advertised content.
    # car_names = parser.prepare_sections('div.class.products-container/div.class.products/div.class.products-description/p.class.products-name', 'text()') 
    # is what I need in this case. It is in the source code, you can check it by yourself as well.
    # I use parser.get_data() class to retrieve data.
    # car_names = parser.get_data(car_names) - this will return pyton list
    # print(car_names)
    # Here is the output:
    # ['LADA (VAZ) Niva', 'Toyota Prius', 'Hyundai i30', 'Kia Optima', 'Chevrolet Aveo', 'Kia Optima', 'Land Rover RR Sport', 'Nissan Sunny', 'Mercedes E 320', 'LADA (VAZ) 2107', 'Mercedes C 180', 'LADA (VAZ) 2107', 'Toyota Prado', 'LADA (VAZ) 21013', 'Mercedes 190', 'GAZ 33021', 'Kia Cee`d', 'LADA (VAZ) 2107', 'LADA (VAZ) 21099', 'Mitsubishi Pajero', 'Mercedes C 180', 'Mercedes CLS 55 AMG', 'Mercedes E 240', 'BMW 528']


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
    I quickly write my route like this: div.class.quote/span.class.text and indicator is text()
    quote_route = parser.prepare_sections('div.class.quote/span.class.text', 'text()')
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
