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


**EXAMPLE**
    
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