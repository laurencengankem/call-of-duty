import itertools 
lista = ['Photo by Nicole Favaron in QC Termemilano. Image may contain: night and shoes', 'Photo by Nicole Favaron in Forte dei Marmi. Image may contain: one or more people, people standing and outdoor', 'Photo by Nicole Favaron in Forte dei Marmi. Image may contain: one or more people, ocean, sky, outdoor, water and nature', 'Photo by Nicole Favaron in Pozze Di Malbacco. Image may contain: one or more people, outdoor, water and nature', 'Photo by Nicole Favaron in Forte dei Marmi. Image may contain: one or more people, sunglasses, sky, cloud, outdoor and closeup', 'Photo by Nicole Favaron in Tonfano, Toscana, Italy. Image may contain: ocean, sky, outdoor and water', 'Photo by Nicole Favaron on May 02, 2019. Image may contain: sky, cloud and outdoor', 'Photo shared by Nicole Favaron on April 29, 2019 tagging @chiarabalduzzi_. Image may contain: 1 person, outdoor and closeup', None, 'Photo by Nicole Favaron on January 07, 2019.', 'Photo by Nicole Favaron in Salice Terme, Liguria, Italy with @chiarabalduzzi_, @sarapizzz, @_nick_freguia_, and @magrebita. Image may contain: 7 people', 'Photo by Nicole Favaron in Forte dei Marmi. Image may contain: 1 person']
words = []

for item in lista:
    if(item is not None):
        if("Image may contain:" in item):
            description = (item.split("Image may contain:",1)[1])
            stopwords = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "and", "or", "one", "more"]
            description = description.replace(",", "")
            token = description.split()

            for stopword in stopwords:
                if stopword in token:
                    token.remove(stopword)

            for word in token:
                words.append(word)
    
print(words)