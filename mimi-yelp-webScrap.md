## Yelp is an American public company headquartered in San Francisco, California. The company develops, hosts, and markets the Yelp.com website and the Yelp mobile app, which publish crowd-sourced reviews about businesses. We'll scrape this website and perform some EDA.


```python
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
```

### Log in Yelp and make some a request for 'barber' in 'San Franciso, CA'


```python
payload = {'email': 'x', 'password': 'x'}
url = 'https://www.yelp.com/login'

login = requests.post(url, data=payload)
scrap_1 = requests.get('https://www.yelp.com/search?find_desc=barber&find_loc=San+Francisco%2C+CA&ns=1')

print(login)
print(scrap_1)
```

    <Response [200]>
    <Response [200]>



```python
parsed = BeautifulSoup(scrap_1.text, 'html.parser')
```

### Get all result pages displayed in the 1st page


```python
allPages = parsed.find_all('a', attrs={'class': "lemon--a__373c0__IEZFH link__373c0__1G70M pagination-link-component__373c0__9aHoC link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE"})
```


```python
allPages = ['https://www.yelp.com'+i['href'] for i in allPages]
allPages
```




    ['https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=30',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=60',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=90',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=120',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=150',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=180',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=210',
     'https://www.yelp.com/search?find_desc=barber&find_loc=San%20Francisco%2C%20CA&start=240']



### There are 8 links leading to the next 8 pages in total of 28 pages. We'll go to each link and make a DataFrame of all businesses and their info.

#### 4 helper functions for 4 important info


```python
def getBiz(link):
    a = requests.get(link)
    aParsed = BeautifulSoup(a.text, 'html.parser')
    allBiz = aParsed.find_all('h4')
    result = [i.a['name'] for i in allBiz][1:]
    
    return result
```


```python
def getBizLink(link):
    a = requests.get(link)
    aParsed = BeautifulSoup(a.text, 'html.parser')
    allBiz = aParsed.find_all('h4')
    result = ['https://www.yelp.com'+i.a['href'] for i in allBiz][1:]
    
    return result
```


```python
def getTotRev(link):
    a = requests.get(link)
    aParsed = BeautifulSoup(a.text, 'html.parser')
    result = int(str(aParsed.find_all('p', attrs={'class': "lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-size--large__373c0__3t60B"})[0]).split('>')[1].split('<')[0].split(' ')[0])
    
    return result
```


```python
def getAvgRev(link):
    a = requests.get(link)
    aParsed = BeautifulSoup(a.text, 'html.parser')
    rev = aParsed.find_all('div', attrs={'role': 'img'})
    result = float([i['aria-label'] for i in rev][0].split(' ')[0])
    
    return result
```


```python
bizHolder = getBiz('https://www.yelp.com/search?find_desc=barber&find_loc=San+Francisco%2C+CA&ns=1')
```


```python
linkHolder = getBizLink('https://www.yelp.com/search?find_desc=barber&find_loc=San+Francisco%2C+CA&ns=1')
```


```python
bizHolder += [item for sub in [getBiz(i) for i in allPages] for item in sub]
bizHolder
```




    ['Rick’s Barbershop',
     'JP Kempt Barber',
     'Emilio’s Barber Shop',
     'Locals Barbershop',
     'Sunset Barber Service',
     'Gentlemen’s Barber Lounge',
     'San Francisco Barber Shop',
     'Debonair Barber & Shave Parlor',
     'Old Mission Barbershop',
     'Geary Salon',
     'Mike’s Barbershop',
     'Fine Line Barbershop',
     'Daddy’s Barbershop',
     'Cutthroat Barbershop',
     'Gents Barber Club',
     'The Barbershop',
     'Public Barber Salon',
     'Haight Street Barbershop',
     'Public Barber Salon',
     'Sanctuary Barber Studio',
     'Dogpatch Barber and Shave South',
     'Barber & Gent',
     'Church Barber & Apothecary',
     'Blades Co Barber Shop - Temp. CLOSED',
     'Attention To Detail Barber Gallery',
     'Peoples Barber & Shop',
     'Moe’s Barber and Beauty',
     'Black & Gold Barber Lounge',
     '1512 Barber Shop',
     'Of Barbers & Bears',
     'The Refinery Grooming Club',
     'Barber Walter’s Mobile Service',
     '30SVN',
     'Dick’s International',
     'Peoples Barber & Shop',
     'Ingleside Barber Shop',
     'Francesco Black',
     'Gentle Cuts',
     'Paulish Barbershop',
     'Razo’s Barber Shop',
     'People’s Barber & Shop',
     'Cut To Contrast Barbershop',
     'Healing Cuts',
     'Cooper Alley & Barber Lane',
     'Metropolitan Barber Shop',
     'Anthony’s Barber Shop',
     'Fresh Blades Barbershop',
     'Topshelf Grooming',
     'Louies Barbershop',
     'Style-O-Rama Barber Shop',
     'Great Cuts On Geary',
     'Heff’s Barbershop',
     'Mone the Barber inside Westside Cuts & Style',
     'SF Barber',
     'Gif’d Crowns',
     'Dogpatch Barber and Shave North',
     'Eureka Barber Shop',
     'Nils Griffin Barbering',
     'Viks the Barbershop',
     'The Buzz',
     'Golden Door Barbershop',
     'Kyle’s BarberShop',
     'The Cutlery Barber Shop',
     'ADY Barber and Beauty Shop',
     'Friendly Cuts',
     'Just Cuts Hair Care',
     'The House Of Handsome Barbershop',
     'Cable Car Clothiers',
     'The District Barbers - Soma District',
     'Right Style Salon',
     'Ahmet’s Barber & Hair Styling',
     'Virgil’s Hair Cutting Studio',
     'Brogan and Son',
     'Westside Cuts & Style',
     'Catalano’s Barber Shop',
     'Gold and Gifted- DC',
     'Mystic Haircutting',
     'Code Salon',
     'Q Cuts',
     'Kinship Salon & Barber',
     'Lee Hong Hair Styling',
     'Zip Zap Hair',
     'Beau SF',
     'Barberella Hair Lounge',
     'Harry’s Hair Cuts',
     'Details Barbershop and Grooming Lounge',
     'Melissa Hair Studio',
     'The Barber Lounge at Bryan Roberts',
     'Dekko',
     'Ace of Fades',
     'Trym',
     'Premiere Barbershop',
     'Alex’s Barber Shop',
     'Great Image Salon',
     'Shorty Maniace At J P Kempt',
     'Brothers Barber Shop',
     'The Requisite Barber',
     'San Francisco Institute of Esthetics and Cosmetology',
     'The District Barbers - Design District',
     'Tam’s Haircuts and Shaves',
     'Laura’s Beauty & Barber Shop',
     'Annie’s Barbershop',
     'Studio Cutz',
     'Nice Cuts',
     'Clipper Guru Mobile Barber',
     'Cloak & Dagger Salon',
     'Ruby’s Cut',
     'Enzi Hair',
     'May’s Barbershop',
     'Cuts By Jack',
     'MACHETE',
     'Happy Hair Studios',
     'David Renshaw Traditional Barber',
     'Raul Anthony Pro',
     'Lyfestyle Supply Line',
     'Sck Salon',
     'Snip Snip',
     'Grey Salon',
     'Hair Shaper',
     'Mane Attraction',
     'Jonathan Baker, Stylist',
     'Styles Go',
     'B&F Barbershop',
     'Chicago’s Barbershop',
     'Dick Troy Hair Salon',
     'Nice Cuts',
     'Arcade Barbershop',
     'Supreme Clientele Barber Lounge',
     'Monterey Hair Salon',
     'CutRight Barber Shop',
     'Vicktor Stevenson Salon',
     'Simply Cuts',
     'Tony Balistreri',
     'The Tailormade Barbershop',
     'Financial District Haircut By Leo',
     'Giannini’s Barber Shop',
     'Special Haircut',
     'Nimbus Haircuts',
     'Hair Deux',
     'Zhen Mei Hair Salon',
     'Beeinsoa Barber & Beauty Shop',
     'Jane Kennedy',
     'Up Hair',
     'Gemini Hair Stylist',
     'Star East Hair Salon',
     'Barberology',
     'The Castro Barber lounge',
     'Christina’s Barber Studio',
     'Precision Hair Design',
     'Every 6 Weeks',
     'Arthur Sebastian',
     'Long Overdue',
     'Shine Hair Styles',
     'S & E Style Cut',
     'Amy’s Barber Shop',
     'The Executive Barber Shop',
     'Kim’s Precision Haircuts',
     'David James',
     'Jordan, Your Barber',
     'The Shop',
     'Flo’s Hair Styling',
     'Talarico’s Barber Shop',
     'Philgood Cuts',
     'Salon J',
     'Barber service by Kevin Panla',
     'Gemini Barber Shop',
     'Su’s Hair Salon',
     'Futaba Hair Salon',
     'Pepe Studio',
     'Maneframe',
     'Charlie’s Hair Design',
     'My Do Hair Design',
     'Bruno Hair Design',
     'Heartzilla Salon',
     'Hair Sensation',
     'Fresh Cuts',
     'Geomantic Salon SF',
     'The Park Salon',
     '3 Mil Wil Hair Salon',
     'Jackson Place Salon',
     'Population Salon Nopa',
     'Neon Shade Hair Fashion',
     'Hair Force 1',
     'Tony Does Your Hair',
     'Silver Cut Hair Salon',
     'Abner’s Barber Shop',
     'Blanca’s Art Of Hair',
     'New Looks Salon',
     'Patrick Evan Hair Salon',
     'Lisa For Hair',
     'Studio Salon',
     'Ming Yuet Stylist',
     'More Than A Cut',
     'Russ’ Barber Shop',
     'Tye’s Barber Shop',
     'Bateau Hair Salon',
     'Shavery Barbershop',
     'Nene’s Beauty & Barber Supply',
     '101 Barbershop Cut & Shave',
     'EMANstyle',
     'Tamina',
     'Mark-Jason Solofa Men’s Grooming',
     'J & J Hair Salon',
     'Shear Inspiration',
     'DZ&Y Barbershop',
     'Lombard Beauty Salon',
     'The Barberhood',
     'YSA Barbershop',
     'Perfect Cut Hair Salon',
     'San Bruno Beauty Studio',
     'San Bruno Beauty Studio',
     'Cinta Aveda Institute',
     'Saviours Salon',
     'Bebo The Barber',
     'Johnny’s Barber Shop',
     'Anna For Hair',
     'Mary’s Beauty Salon and Barber Shop',
     'Caledonia Street Barbers',
     'The Pretty Pretty Collective',
     'Spunk Salon',
     'The Woodbridge',
     'Yan Yan Beauty Salon',
     'Amazon Barber',
     'Hair On Hyde',
     'Stanley Weissberg at Up Hair Salon',
     'Salon 828',
     'City Fades Barbershop',
     'Hair of the Gods by Geno Valle',
     'Echos Hair Design',
     'Platinum’s Barber Shop',
     'Taylor / Monroe',
     'Levels Barber & Shop',
     'Barber Affiliates Barber Studio',
     'Beauty Style Exchange',
     'Fashion Cuts & Perms',
     'Images For Hair',
     'Twenty 89 Hair Design',
     'R&B Barbershop',
     'Broadway Barber Shop',
     'Mister Hyde',
     'Revival Barber + Beauty',
     'Expert Cut',
     'Supercuts',
     'Honeycomb Salon',
     'United Grooming',
     'Harry’s Hair Studio',
     'Frank Logan Barbershop',
     'Ling’s Salon',
     'Ann’s For Hair',
     'Maddix Bruyn Traditional Barber',
     'TokyoSF',
     'The Hair Place & More',
     'Shear Image Salon',
     'Hong Kong Art Salon',
     'Salon Baobao',
     'Nepenji Japan Center Beauty Clinic',
     'Bijoux Salon',
     'Hair Razors',
     'Susan Beauty Salon',
     'Sario’s Hair Design',
     'Kayo Hair Salon',
     'Lisa’s Hair Design',
     'Mz Beauty & Hair salon',
     'Art Hair Salon',
     'Cowboys & Angels',
     'Fresh Cuts Barbershop',
     'New Marbet’s Hair Cuts',
     'John Wick Barber Shop',
     'Mary’s Beauty Salon & Barber Shop',
     'Suru Barbershop']




```python
linkHolder += [item for sub in [getBizLink(i) for i in allPages] for item in sub]
linkHolder
```




    ['https://www.yelp.com/biz/ricks-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/jp-kempt-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/emilios-barber-shop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/locals-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/sunset-barber-service-san-francisco?osq=barber',
     'https://www.yelp.com/biz/gentlemens-barber-lounge-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/san-francisco-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/debonair-barber-and-shave-parlor-san-francisco?osq=barber',
     'https://www.yelp.com/biz/old-mission-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/geary-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/mikes-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/fine-line-barbershop-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/daddy-s-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/cutthroat-barbershop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/gents-barber-club-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-barbershop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/public-barber-salon-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/haight-street-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/public-barber-salon-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/sanctuary-barber-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/dogpatch-barber-and-shave-south-san-francisco?osq=barber',
     'https://www.yelp.com/biz/barber-and-gent-san-francisco-5?osq=barber',
     'https://www.yelp.com/biz/church-barber-and-apothecary-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/blades-co-barber-shop-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/attention-to-detail-barber-gallery-san-francisco?osq=barber',
     'https://www.yelp.com/biz/peoples-barber-and-shop-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/moes-barber-and-beauty-san-francisco?osq=barber',
     'https://www.yelp.com/biz/black-and-gold-barber-lounge-daly-city?osq=barber',
     'https://www.yelp.com/biz/1512-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/of-barbers-and-bears-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-refinery-grooming-club-san-francisco?osq=barber',
     'https://www.yelp.com/biz/barber-walters-mobile-service-san-francisco?osq=barber',
     'https://www.yelp.com/biz/30svn-san-francisco?osq=barber',
     'https://www.yelp.com/biz/dicks-international-san-francisco?osq=barber',
     'https://www.yelp.com/biz/peoples-barber-and-shop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/ingleside-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/francesco-black-san-francisco-7?osq=barber',
     'https://www.yelp.com/biz/gentle-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/paulish-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/razos-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/peoples-barber-and-shop-san-francisco-5?osq=barber',
     'https://www.yelp.com/biz/cut-to-contrast-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/healing-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/cooper-alley-and-barber-lane-san-francisco?osq=barber',
     'https://www.yelp.com/biz/metropolitan-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/anthonys-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/fresh-blades-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/topshelf-grooming-san-francisco?osq=barber',
     'https://www.yelp.com/biz/louies-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/style-o-rama-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/great-cuts-on-geary-san-francisco?osq=barber',
     'https://www.yelp.com/biz/heffs-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/mone-the-barber-inside-westside-cuts-and-style-san-francisco?osq=barber',
     'https://www.yelp.com/biz/sf-barber-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/gif-d-crowns-san-francisco?osq=barber',
     'https://www.yelp.com/biz/dogpatch-barber-and-shave-north-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/eureka-barber-shop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/nils-griffin-barbering-san-francisco?osq=barber',
     'https://www.yelp.com/biz/viks-the-barbershop-daly-city-2?osq=barber',
     'https://www.yelp.com/biz/the-buzz-san-francisco?osq=barber',
     'https://www.yelp.com/biz/golden-door-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/kyles-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-cutlery-barber-shop-daly-city-2?osq=barber',
     'https://www.yelp.com/biz/ady-barber-and-beauty-shop-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/friendly-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/just-cuts-hair-care-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-house-of-handsome-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/cable-car-clothiers-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-district-barbers-soma-district-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/right-style-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/ahmets-barber-and-hair-styling-san-francisco?osq=barber',
     'https://www.yelp.com/biz/virgils-hair-cutting-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/brogan-and-son-san-francisco?osq=barber',
     'https://www.yelp.com/biz/westside-cuts-and-style-san-francisco?osq=barber',
     'https://www.yelp.com/biz/catalanos-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/gold-and-gifted-dc-daly-city?osq=barber',
     'https://www.yelp.com/biz/mystic-haircutting-san-francisco?osq=barber',
     'https://www.yelp.com/biz/code-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/q-cuts-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/kinship-salon-and-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/lee-hong-hair-styling-san-francisco?osq=barber',
     'https://www.yelp.com/biz/zip-zap-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/beau-sf-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/barberella-hair-lounge-san-francisco?osq=barber',
     'https://www.yelp.com/biz/harrys-hair-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/details-barbershop-and-grooming-lounge-san-francisco?osq=barber',
     'https://www.yelp.com/biz/melissa-hair-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-barber-lounge-at-bryan-roberts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/dekko-san-francisco?osq=barber',
     'https://www.yelp.com/biz/ace-of-fades-san-francisco?osq=barber',
     'https://www.yelp.com/biz/trym-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/premiere-barbershop-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/alexs-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/great-image-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/shorty-maniace-at-j-p-kempt-san-francisco?osq=barber',
     'https://www.yelp.com/biz/brothers-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-requisite-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/san-francisco-institute-of-esthetics-and-cosmetology-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-district-barbers-design-district-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/tams-haircuts-and-shaves-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/lauras-beauty-and-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/annies-barbershop-san-bruno?osq=barber',
     'https://www.yelp.com/biz/studio-cutz-daly-city?osq=barber',
     'https://www.yelp.com/biz/nice-cuts-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/clipper-guru-mobile-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/cloak-and-dagger-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/rubys-cut-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/enzi-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/mays-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/cuts-by-jack-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/machete-san-francisco?osq=barber',
     'https://www.yelp.com/biz/happy-hair-studios-san-francisco?osq=barber',
     'https://www.yelp.com/biz/david-renshaw-traditional-barber-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/raul-anthony-pro-san-francisco?osq=barber',
     'https://www.yelp.com/biz/lyfestyle-supply-line-san-francisco-9?osq=barber',
     'https://www.yelp.com/biz/sck-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/snip-snip-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/grey-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/hair-shaper-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/mane-attraction-san-francisco?osq=barber',
     'https://www.yelp.com/biz/jonathan-baker-stylist-san-francisco?osq=barber',
     'https://www.yelp.com/biz/styles-go-san-francisco-16?osq=barber',
     'https://www.yelp.com/biz/b-and-f-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/chicagos-barbershop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/dick-troy-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/nice-cuts-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/arcade-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/supreme-clientele-barber-lounge-colma?osq=barber',
     'https://www.yelp.com/biz/monterey-hair-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/cutright-barber-shop-san-bruno?osq=barber',
     'https://www.yelp.com/biz/vicktor-stevenson-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/simply-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/tony-balistreri-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/the-tailormade-barbershop-daly-city?osq=barber',
     'https://www.yelp.com/biz/financial-district-haircut-by-leo-san-francisco?osq=barber',
     'https://www.yelp.com/biz/gianninis-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/special-haircut-san-francisco?osq=barber',
     'https://www.yelp.com/biz/nimbus-haircuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-deux-san-francisco?osq=barber',
     'https://www.yelp.com/biz/zhen-mei-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/beeinsoa-barber-and-beauty-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/jane-kennedy-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/up-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/gemini-hair-stylist-san-francisco?osq=barber',
     'https://www.yelp.com/biz/star-east-hair-salon-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/barberology-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-castro-barber-lounge-san-francisco?osq=barber',
     'https://www.yelp.com/biz/christinas-barber-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/precision-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/every-6-weeks-san-francisco?osq=barber',
     'https://www.yelp.com/biz/arthur-sebastian-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/long-overdue-san-francisco?osq=barber',
     'https://www.yelp.com/biz/shine-hair-styles-san-francisco?osq=barber',
     'https://www.yelp.com/biz/s-and-e-style-cut-san-francisco?osq=barber',
     'https://www.yelp.com/biz/amys-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-executive-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/kims-precision-haircuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/david-james-san-francisco?osq=barber',
     'https://www.yelp.com/biz/jordan-your-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/flos-hair-styling-san-francisco?osq=barber',
     'https://www.yelp.com/biz/talaricos-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/philgood-cuts-south-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/salon-j-san-francisco?osq=barber',
     'https://www.yelp.com/biz/barber-service-by-kevin-panla-south-san-francisco-9?osq=barber',
     'https://www.yelp.com/biz/gemini-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/sus-hair-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/futaba-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/pepe-studio-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/maneframe-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/charlies-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/my-do-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/bruno-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/heartzilla-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-sensation-san-francisco?osq=barber',
     'https://www.yelp.com/biz/fresh-cuts-daly-city?osq=barber',
     'https://www.yelp.com/biz/geomantic-salon-sf-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-park-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/3-mil-wil-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/jackson-place-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/population-salon-nopa-san-francisco?osq=barber',
     'https://www.yelp.com/biz/neon-shade-hair-fashion-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-force-1-daly-city-3?osq=barber',
     'https://www.yelp.com/biz/tony-does-your-hair-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/silver-cut-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/abners-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/blancas-art-of-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/new-looks-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/patrick-evan-hair-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/lisa-for-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/studio-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/ming-yuet-stylist-san-francisco?osq=barber',
     'https://www.yelp.com/biz/more-than-a-cut-san-francisco?osq=barber',
     'https://www.yelp.com/biz/russ-barber-shop-mill-valley?osq=barber',
     'https://www.yelp.com/biz/tyes-barber-shop-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/bateau-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/shavery-barbershop-mill-valley?osq=barber',
     'https://www.yelp.com/biz/nenes-beauty-and-barber-supply-san-francisco?osq=barber',
     'https://www.yelp.com/biz/101-barbershop-cut-and-shave-daly-city-8?osq=barber',
     'https://www.yelp.com/biz/emanstyle-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/tamina-san-francisco?osq=barber',
     'https://www.yelp.com/biz/mark-jason-solofa-mens-grooming-berkeley?osq=barber',
     'https://www.yelp.com/biz/j-and-j-hair-salon-san-francisco-4?osq=barber',
     'https://www.yelp.com/biz/shear-inspiration-san-francisco?osq=barber',
     'https://www.yelp.com/biz/dz-and-y-barbershop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/lombard-beauty-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/the-barberhood-san-francisco-6?osq=barber',
     'https://www.yelp.com/biz/ysa-barbershop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/perfect-cut-hair-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/san-bruno-beauty-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/generation-cuts-daly-city?osq=barber',
     'https://www.yelp.com/biz/cinta-aveda-institute-san-francisco?osq=barber',
     'https://www.yelp.com/biz/saviours-salon-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/bebo-the-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/anna-for-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/johnnys-barber-shop-pacifica?osq=barber',
     'https://www.yelp.com/biz/marys-beauty-salon-and-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-pretty-pretty-collective-san-francisco?osq=barber',
     'https://www.yelp.com/biz/spunk-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-woodbridge-san-francisco?osq=barber',
     'https://www.yelp.com/biz/caledonia-street-barbers-sausalito?osq=barber',
     'https://www.yelp.com/biz/yan-yan-beauty-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/amazon-barber-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-on-hyde-san-francisco?osq=barber',
     'https://www.yelp.com/biz/stanley-weissberg-at-up-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/salon-828-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-of-the-gods-by-geno-valle-san-francisco?osq=barber',
     'https://www.yelp.com/biz/city-fades-barbershop-daly-city?osq=barber',
     'https://www.yelp.com/biz/echos-hair-design-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/taylor-monroe-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/platinums-barber-shop-san-francisco-5?osq=barber',
     'https://www.yelp.com/biz/barber-affiliates-barber-studio-el-cerrito?osq=barber',
     'https://www.yelp.com/biz/levels-barber-and-shop-oakland?osq=barber',
     'https://www.yelp.com/biz/beauty-style-exchange-san-francisco?osq=barber',
     'https://www.yelp.com/biz/fashion-cuts-and-perms-san-francisco?osq=barber',
     'https://www.yelp.com/biz/images-for-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/twenty-89-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/broadway-barber-shop-millbrae-4?osq=barber',
     'https://www.yelp.com/biz/r-and-b-barbershop-south-san-francisco?osq=barber',
     'https://www.yelp.com/biz/mister-hyde-san-francisco-3?osq=barber',
     'https://www.yelp.com/biz/revival-barber-beauty-berkeley?osq=barber',
     'https://www.yelp.com/biz/expert-cut-san-francisco?osq=barber',
     'https://www.yelp.com/biz/supercuts-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/honeycomb-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/united-grooming-oakland-2?osq=barber',
     'https://www.yelp.com/biz/harrys-hair-studio-san-francisco?osq=barber',
     'https://www.yelp.com/biz/frank-logan-barbershop-alameda?osq=barber',
     'https://www.yelp.com/biz/lings-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/anns-for-hair-san-francisco?osq=barber',
     'https://www.yelp.com/biz/maddix-bruyn-traditional-barber-berkeley-5?osq=barber',
     'https://www.yelp.com/biz/tokyosf-san-francisco?osq=barber',
     'https://www.yelp.com/biz/the-hair-place-and-more-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/shear-image-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hong-kong-art-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/salon-baobao-san-francisco?osq=barber',
     'https://www.yelp.com/biz/nepenji-japan-center-beauty-clinic-san-francisco?osq=barber',
     'https://www.yelp.com/biz/bijoux-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/hair-razors-pacifica?osq=barber',
     'https://www.yelp.com/biz/susan-beauty-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/sarios-hair-design-san-francisco?osq=barber',
     'https://www.yelp.com/biz/kayo-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/lisas-hair-design-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/mz-beauty-and-hair-salon-san-francisco?osq=barber',
     'https://www.yelp.com/biz/art-hair-salon-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/cowboys-and-angels-san-francisco?osq=barber',
     'https://www.yelp.com/biz/fresh-cuts-barbershop-millbrae?osq=barber',
     'https://www.yelp.com/biz/new-marbets-hair-cuts-san-francisco?osq=barber',
     'https://www.yelp.com/biz/john-wick-barber-shop-san-francisco?osq=barber',
     'https://www.yelp.com/biz/marys-beauty-salon-and-barber-shop-san-francisco-2?osq=barber',
     'https://www.yelp.com/biz/suru-barbershop-oakland?osq=barber']




```python
totRevHolder = []

for i in linkHolder:
    try:
        totRevHolder.append(getTotRev(i))
    except:
        totRevHolder.append(np.nan)
```

Unable to find total reviews for:
- https://www.yelp.com/biz/mays-barbershop-san-francisco?osq=barber
- https://www.yelp.com/biz/cuts-by-jack-san-francisco-4?osq=barber
- https://www.yelp.com/biz/happy-hair-studios-san-francisco?osq=barber
- https://www.yelp.com/biz/the-castro-barber-lounge-san-francisco?osq=barber
- https://www.yelp.com/biz/jordan-your-barber-san-francisco?osq=barber
- https://www.yelp.com/biz/john-wick-barber-shop-san-francisco?osq=barber


```python
totRevHolder
```




    [170,
     240,
     253,
     118,
     125,
     179,
     139,
     113,
     55,
     184,
     51,
     64,
     220,
     15,
     151,
     161,
     947,
     10,
     428,
     14,
     81,
     50,
     45,
     183,
     61,
     953,
     50,
     137,
     111,
     14,
     105,
     20,
     18,
     116,
     245,
     74,
     50,
     129,
     18,
     49,
     86,
     87,
     10,
     47,
     144,
     12,
     71,
     31,
     90,
     34,
     44,
     87,
     34,
     21,
     3,
     58,
     51,
     28,
     63,
     45,
     46,
     56,
     69,
     68,
     137,
     127,
     71,
     98,
     120,
     30,
     78,
     67,
     234,
     67,
     8,
     63,
     146,
     943,
     20,
     148,
     94,
     445,
     26,
     118,
     32,
     106,
     11,
     3,
     203,
     43,
     6,
     1,
     30,
     28,
     12,
     58,
     9,
     487,
     5,
     19,
     131,
     55,
     5,
     171,
     2,
     57,
     37,
     36,
     nan,
     nan,
     28,
     nan,
     1,
     27,
     12,
     11,
     13,
     51,
     160,
     165,
     1,
     7,
     4,
     93,
     6,
     70,
     80,
     58,
     57,
     87,
     15,
     100,
     15,
     111,
     56,
     35,
     26,
     13,
     9,
     86,
     1,
     2,
     51,
     4,
     204,
     8,
     nan,
     14,
     99,
     180,
     263,
     19,
     122,
     54,
     6,
     66,
     56,
     163,
     nan,
     6,
     5,
     13,
     72,
     5,
     61,
     8,
     16,
     3,
     56,
     58,
     5,
     21,
     67,
     32,
     63,
     15,
     39,
     101,
     4,
     25,
     383,
     75,
     25,
     18,
     11,
     46,
     46,
     44,
     848,
     39,
     71,
     133,
     2,
     8,
     5,
     79,
     58,
     2,
     4,
     61,
     4,
     120,
     6,
     6,
     57,
     106,
     14,
     12,
     321,
     26,
     10,
     1021,
     65,
     2,
     13,
     52,
     19,
     250,
     125,
     185,
     39,
     21,
     26,
     150,
     8,
     11,
     234,
     24,
     19,
     1082,
     9,
     2,
     15,
     52,
     13,
     15,
     106,
     2,
     49,
     90,
     76,
     19,
     155,
     191,
     25,
     56,
     11,
     11,
     95,
     52,
     38,
     9,
     176,
     31,
     410,
     407,
     52,
     37,
     7,
     58,
     147,
     153,
     2,
     23,
     618,
     19,
     8,
     nan,
     20,
     10]




```python
avgRevHolder = []

for i in linkHolder:
    try:
        avgRevHolder.append(getAvgRev(i))
    except:
        print(i)
        avgRevHolder.append(np.nan)
```

Unable to find total reviews for:
- https://www.yelp.com/biz/gold-and-gifted-dc-daly-city?osq=barber
- https://www.yelp.com/biz/the-castro-barber-lounge-san-francisco?osq=barber
- https://www.yelp.com/biz/john-wick-barber-shop-san-francisco?osq=barber


```python
avgRevHolder
```




    [4.5,
     4.5,
     4.0,
     5.0,
     4.5,
     4.5,
     4.5,
     4.5,
     5.0,
     4.5,
     4.5,
     4.5,
     4.0,
     5.0,
     4.5,
     4.5,
     4.5,
     5.0,
     5.0,
     5.0,
     4.5,
     4.0,
     5.0,
     4.5,
     4.5,
     4.0,
     4.0,
     5.0,
     5.0,
     4.5,
     4.5,
     5.0,
     5.0,
     4.0,
     4.0,
     5.0,
     5.0,
     4.5,
     4.5,
     4.5,
     4.0,
     4.5,
     5.0,
     5.0,
     4.5,
     5.0,
     4.5,
     5.0,
     4.0,
     4.5,
     4.5,
     4.5,
     4.5,
     5.0,
     5.0,
     4.5,
     4.0,
     5.0,
     5.0,
     4.5,
     4.5,
     5.0,
     4.5,
     4.5,
     4.5,
     4.5,
     4.5,
     4.5,
     4.0,
     5.0,
     4.0,
     4.5,
     4.5,
     4.0,
     4.5,
     nan,
     4.5,
     4.5,
     4.5,
     4.5,
     4.5,
     4.5,
     5.0,
     4.5,
     4.0,
     4.5,
     4.5,
     5.0,
     4.5,
     4.5,
     5.0,
     5.0,
     4.0,
     4.5,
     5.0,
     3.0,
     5.0,
     4.0,
     4.0,
     4.5,
     4.5,
     5.0,
     4.0,
     4.0,
     5.0,
     5.0,
     4.5,
     5.0,
     4.0,
     5.0,
     5.0,
     4.5,
     5.0,
     5.0,
     5.0,
     5.0,
     5.0,
     5.0,
     4.0,
     4.5,
     5.0,
     4.5,
     4.5,
     4.0,
     5.0,
     3.5,
     4.0,
     5.0,
     5.0,
     4.5,
     5.0,
     4.0,
     5.0,
     4.5,
     5.0,
     4.5,
     4.5,
     4.5,
     5.0,
     4.0,
     5.0,
     5.0,
     5.0,
     5.0,
     4.5,
     4.5,
     nan,
     5.0,
     4.5,
     4.5,
     4.5,
     5.0,
     4.0,
     4.0,
     4.5,
     4.5,
     4.0,
     5.0,
     4.5,
     5.0,
     5.0,
     3.5,
     4.0,
     4.0,
     5.0,
     4.5,
     4.0,
     5.0,
     4.5,
     4.5,
     5.0,
     4.5,
     4.5,
     5.0,
     4.5,
     4.0,
     5.0,
     5.0,
     5.0,
     5.0,
     4.0,
     4.5,
     4.5,
     5.0,
     4.5,
     3.5,
     4.0,
     5.0,
     5.0,
     4.5,
     5.0,
     4.5,
     5.0,
     4.5,
     4.0,
     4.5,
     4.5,
     5.0,
     4.5,
     5.0,
     5.0,
     5.0,
     3.5,
     5.0,
     3.5,
     4.5,
     4.0,
     4.0,
     4.0,
     4.5,
     4.5,
     4.0,
     5.0,
     5.0,
     4.0,
     4.5,
     5.0,
     4.5,
     4.5,
     4.5,
     4.5,
     4.5,
     3.5,
     4.5,
     5.0,
     5.0,
     4.5,
     4.0,
     5.0,
     4.5,
     3.5,
     5.0,
     4.5,
     4.0,
     4.5,
     4.5,
     4.5,
     5.0,
     4.5,
     5.0,
     5.0,
     5.0,
     3.0,
     4.5,
     5.0,
     4.0,
     5.0,
     4.5,
     4.5,
     5.0,
     5.0,
     4.5,
     4.5,
     4.5,
     4.5,
     4.0,
     4.5,
     4.5,
     5.0,
     4.5,
     4.5,
     4.0,
     5.0,
     4.5,
     4.5,
     4.0,
     4.5,
     nan,
     4.0,
     4.5]



### Generate a complete output that contains all info


```python
output = pd.DataFrame([bizHolder, linkHolder, totRevHolder, avgRevHolder]).T
output.columns = ['name', 'link', 'total rev', 'avg rev']
output
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>link</th>
      <th>total rev</th>
      <th>avg rev</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rick’s Barbershop</td>
      <td>https://www.yelp.com/biz/ricks-barbershop-san-...</td>
      <td>170</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>JP Kempt Barber</td>
      <td>https://www.yelp.com/biz/jp-kempt-barber-san-f...</td>
      <td>240</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Emilio’s Barber Shop</td>
      <td>https://www.yelp.com/biz/emilios-barber-shop-s...</td>
      <td>253</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Locals Barbershop</td>
      <td>https://www.yelp.com/biz/locals-barbershop-san...</td>
      <td>118</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sunset Barber Service</td>
      <td>https://www.yelp.com/biz/sunset-barber-service...</td>
      <td>125</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>265</th>
      <td>Fresh Cuts Barbershop</td>
      <td>https://www.yelp.com/biz/fresh-cuts-barbershop...</td>
      <td>19</td>
      <td>4</td>
    </tr>
    <tr>
      <th>266</th>
      <td>New Marbet’s Hair Cuts</td>
      <td>https://www.yelp.com/biz/new-marbets-hair-cuts...</td>
      <td>8</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>267</th>
      <td>John Wick Barber Shop</td>
      <td>https://www.yelp.com/biz/john-wick-barber-shop...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>268</th>
      <td>Mary’s Beauty Salon &amp; Barber Shop</td>
      <td>https://www.yelp.com/biz/marys-beauty-salon-an...</td>
      <td>20</td>
      <td>4</td>
    </tr>
    <tr>
      <th>269</th>
      <td>Suru Barbershop</td>
      <td>https://www.yelp.com/biz/suru-barbershop-oakla...</td>
      <td>10</td>
      <td>4.5</td>
    </tr>
  </tbody>
</table>
<p>270 rows × 4 columns</p>
</div>




```python
output_toDraw = output.drop_duplicates().dropna()
```

### Overview of total reviews by average review in range lowest-highest


```python
import plotly.express as px

fig = px.bar(output_toDraw, x='name', y='total rev', color='avg rev')

fig.update_layout(title_text='Top 270 Barber Shops in California, CA Total Review and Average Review',
                  yaxis=dict(title='count'),
                  xaxis=dict(title='avg rev'))

fig.show()
```


<div>


            <div id="58c264f3-8db9-45df-b2c2-64caa5aca724" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("58c264f3-8db9-45df-b2c2-64caa5aca724")) {
                    Plotly.newPlot(
                        '58c264f3-8db9-45df-b2c2-64caa5aca724',
                        [{"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=4.5<br>name=%{x}<br>total rev=%{y}", "legendgroup": "4.5", "marker": {"color": "#636efa"}, "name": "4.5", "offsetgroup": "4.5", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Rick\u2019s Barbershop", "JP Kempt Barber", "Sunset Barber Service", "Gentlemen\u2019s Barber Lounge", "San Francisco Barber Shop", "Debonair Barber & Shave Parlor", "Geary Salon", "Mike\u2019s Barbershop", "Fine Line Barbershop", "Gents Barber Club", "The Barbershop", "Public Barber Salon", "Dogpatch Barber and Shave South", "Blades Co Barber Shop - Temp. CLOSED", "Attention To Detail Barber Gallery", "Of Barbers & Bears", "The Refinery Grooming Club", "Gentle Cuts", "Paulish Barbershop", "Razo\u2019s Barber Shop", "Cut To Contrast Barbershop", "Metropolitan Barber Shop", "Fresh Blades Barbershop", "Style-O-Rama Barber Shop", "Great Cuts On Geary", "Heff\u2019s Barbershop", "Mone the Barber inside Westside Cuts & Style", "Dogpatch Barber and Shave North", "The Buzz", "Golden Door Barbershop", "The Cutlery Barber Shop", "ADY Barber and Beauty Shop", "Friendly Cuts", "Just Cuts Hair Care", "The House Of Handsome Barbershop", "Cable Car Clothiers", "Virgil\u2019s Hair Cutting Studio", "Brogan and Son", "Catalano\u2019s Barber Shop", "Mystic Haircutting", "Code Salon", "Q Cuts", "Kinship Salon & Barber", "Lee Hong Hair Styling", "Zip Zap Hair", "Barberella Hair Lounge", "Details Barbershop and Grooming Lounge", "Melissa Hair Studio", "Dekko", "Ace of Fades", "Great Image Salon", "Tam\u2019s Haircuts and Shaves", "Laura\u2019s Beauty & Barber Shop", "Ruby\u2019s Cut", "Mane Attraction", "Styles Go", "B&F Barbershop", "CutRight Barber Shop", "The Tailormade Barbershop", "Giannini\u2019s Barber Shop", "Special Haircut", "Nimbus Haircuts", "Star East Hair Salon", "Barberology", "Precision Hair Design", "Every 6 Weeks", "Arthur Sebastian", "Amy\u2019s Barber Shop", "The Executive Barber Shop", "Gemini Barber Shop", "Pepe Studio", "Maneframe", "My Do Hair Design", "Bruno Hair Design", "Hair Sensation", "Neon Shade Hair Fashion", "Hair Force 1", "Silver Cut Hair Salon", "Lisa For Hair", "Ming Yuet Stylist", "Russ\u2019 Barber Shop", "Bateau Hair Salon", "Shavery Barbershop", "101 Barbershop Cut & Shave", "Lombard Beauty Salon", "San Bruno Beauty Studio", "San Bruno Beauty Studio", "Anna For Hair", "Caledonia Street Barbers", "The Pretty Pretty Collective", "Spunk Salon", "The Woodbridge", "Yan Yan Beauty Salon", "Hair On Hyde", "City Fades Barbershop", "Platinum\u2019s Barber Shop", "Barber Affiliates Barber Studio", "Fashion Cuts & Perms", "Images For Hair", "Twenty 89 Hair Design", "Broadway Barber Shop", "Honeycomb Salon", "Ling\u2019s Salon", "Ann\u2019s For Hair", "The Hair Place & More", "Shear Image Salon", "Hong Kong Art Salon", "Salon Baobao", "Bijoux Salon", "Hair Razors", "Sario\u2019s Hair Design", "Kayo Hair Salon", "Art Hair Salon", "Cowboys & Angels", "New Marbet\u2019s Hair Cuts", "Suru Barbershop"], "xaxis": "x", "y": [170, 240, 125, 179, 139, 113, 184, 51, 64, 151, 161, 947, 81, 183, 61, 14, 105, 129, 18, 49, 87, 144, 71, 34, 44, 87, 34, 58, 45, 46, 69, 68, 137, 127, 71, 98, 67, 234, 8, 146, 943, 20, 148, 94, 445, 118, 106, 11, 203, 43, 28, 19, 131, 37, 165, 7, 4, 87, 111, 35, 26, 13, 204, 8, 99, 180, 263, 6, 66, 8, 56, 58, 21, 67, 63, 75, 25, 11, 39, 133, 8, 79, 58, 4, 106, 26, 10, 52, 250, 125, 185, 39, 21, 150, 234, 1082, 15, 13, 15, 106, 49, 191, 11, 95, 9, 176, 31, 410, 52, 37, 58, 147, 23, 618, 8, 10], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=4.0<br>name=%{x}<br>total rev=%{y}", "legendgroup": "4.0", "marker": {"color": "#EF553B"}, "name": "4.0", "offsetgroup": "4.0", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Emilio\u2019s Barber Shop", "Daddy\u2019s Barbershop", "Barber & Gent", "Peoples Barber & Shop", "Moe\u2019s Barber and Beauty", "Dick\u2019s International", "Peoples Barber & Shop", "People\u2019s Barber & Shop", "Louies Barbershop", "Eureka Barber Shop", "The District Barbers - Soma District", "Ahmet\u2019s Barber & Hair Styling", "Westside Cuts & Style", "Harry\u2019s Hair Cuts", "Alex\u2019s Barber Shop", "San Francisco Institute of Esthetics and Cosmetology", "The District Barbers - Design District", "Studio Cutz", "Nice Cuts", "Hair Shaper", "Chicago\u2019s Barbershop", "Arcade Barbershop", "Simply Cuts", "Zhen Mei Hair Salon", "Shine Hair Styles", "S & E Style Cut", "Kim\u2019s Precision Haircuts", "Philgood Cuts", "Salon J", "Su\u2019s Hair Salon", "Fresh Cuts", "Population Salon Nopa", "Blanca\u2019s Art Of Hair", "Tye\u2019s Barber Shop", "The Barberhood", "YSA Barbershop", "Perfect Cut Hair Salon", "Cinta Aveda Institute", "Johnny\u2019s Barber Shop", "Hair of the Gods by Geno Valle", "Beauty Style Exchange", "Harry\u2019s Hair Studio", "Nepenji Japan Center Beauty Clinic", "Lisa\u2019s Hair Design", "Fresh Cuts Barbershop", "Mary\u2019s Beauty Salon & Barber Shop"], "xaxis": "x", "y": [253, 220, 50, 953, 50, 116, 245, 86, 90, 51, 120, 78, 67, 32, 30, 487, 5, 5, 171, 160, 93, 80, 100, 86, 122, 54, 56, 72, 5, 16, 15, 383, 46, 5, 14, 12, 321, 1021, 13, 24, 52, 56, 407, 153, 19, 20], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=5.0<br>name=%{x}<br>total rev=%{y}", "legendgroup": "5.0", "marker": {"color": "#00cc96"}, "name": "5.0", "offsetgroup": "5.0", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Locals Barbershop", "Old Mission Barbershop", "Cutthroat Barbershop", "Haight Street Barbershop", "Public Barber Salon", "Sanctuary Barber Studio", "Church Barber & Apothecary", "Black & Gold Barber Lounge", "1512 Barber Shop", "Barber Walter\u2019s Mobile Service", "30SVN", "Ingleside Barber Shop", "Francesco Black", "Healing Cuts", "Cooper Alley & Barber Lane", "Anthony\u2019s Barber Shop", "Topshelf Grooming", "SF Barber", "Gif\u2019d Crowns", "Nils Griffin Barbering", "Viks the Barbershop", "Kyle\u2019s BarberShop", "Right Style Salon", "Beau SF", "The Barber Lounge at Bryan Roberts", "Trym", "Premiere Barbershop", "Shorty Maniace At J P Kempt", "The Requisite Barber", "Annie\u2019s Barbershop", "Clipper Guru Mobile Barber", "Cloak & Dagger Salon", "Enzi Hair", "MACHETE", "David Renshaw Traditional Barber", "Raul Anthony Pro", "Lyfestyle Supply Line", "Sck Salon", "Snip Snip", "Grey Salon", "Jonathan Baker, Stylist", "Dick Troy Hair Salon", "Supreme Clientele Barber Lounge", "Monterey Hair Salon", "Vicktor Stevenson Salon", "Tony Balistreri", "Financial District Haircut By Leo", "Hair Deux", "Beeinsoa Barber & Beauty Shop", "Jane Kennedy", "Up Hair", "Gemini Hair Stylist", "Christina\u2019s Barber Studio", "Long Overdue", "David James", "The Shop", "Flo\u2019s Hair Styling", "Barber service by Kevin Panla", "Futaba Hair Salon", "Charlie\u2019s Hair Design", "Heartzilla Salon", "Geomantic Salon SF", "The Park Salon", "3 Mil Wil Hair Salon", "Jackson Place Salon", "Tony Does Your Hair", "New Looks Salon", "Patrick Evan Hair Salon", "Studio Salon", "More Than A Cut", "Nene\u2019s Beauty & Barber Supply", "EMANstyle", "Tamina", "Mark-Jason Solofa Men\u2019s Grooming", "Shear Inspiration", "Saviours Salon", "Bebo The Barber", "Mary\u2019s Beauty Salon and Barber Shop", "Stanley Weissberg at Up Hair Salon", "Salon 828", "Echos Hair Design", "Levels Barber & Shop", "R&B Barbershop", "Mister Hyde", "Revival Barber + Beauty", "Expert Cut", "United Grooming", "Frank Logan Barbershop", "Maddix Bruyn Traditional Barber", "TokyoSF", "Susan Beauty Salon", "Mz Beauty & Hair salon"], "xaxis": "x", "y": [118, 55, 15, 10, 428, 14, 45, 137, 111, 20, 18, 74, 50, 10, 47, 12, 31, 21, 3, 28, 63, 56, 30, 26, 3, 6, 1, 12, 9, 55, 2, 57, 36, 28, 1, 27, 12, 11, 13, 51, 1, 6, 58, 57, 15, 15, 56, 9, 1, 2, 51, 4, 14, 19, 163, 6, 5, 61, 3, 5, 32, 39, 101, 4, 25, 18, 44, 848, 71, 2, 2, 61, 4, 120, 6, 65, 2, 19, 8, 11, 19, 2, 2, 90, 76, 19, 25, 11, 52, 38, 7, 2], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=3.0<br>name=%{x}<br>total rev=%{y}", "legendgroup": "3.0", "marker": {"color": "#ab63fa"}, "name": "3.0", "offsetgroup": "3.0", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Brothers Barber Shop", "Supercuts"], "xaxis": "x", "y": [58, 155], "yaxis": "y"}, {"alignmentgroup": "True", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=3.5<br>name=%{x}<br>total rev=%{y}", "legendgroup": "3.5", "marker": {"color": "#FFA15A"}, "name": "3.5", "offsetgroup": "3.5", "orientation": "v", "showlegend": true, "textposition": "auto", "type": "bar", "x": ["Nice Cuts", "Talarico\u2019s Barber Shop", "Abner\u2019s Barber Shop", "J & J Hair Salon", "DZ&Y Barbershop", "Amazon Barber", "Taylor / Monroe"], "xaxis": "x", "y": [70, 13, 46, 6, 57, 26, 9], "yaxis": "y"}],
                        {"barmode": "relative", "legend": {"title": {"text": "avg rev"}, "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Top 270 Barber Shops in California, CA Total Review and Average Review"}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "avg rev"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('58c264f3-8db9-45df-b2c2-64caa5aca724');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### Overview of average reviews


```python
byAvgRev = output_toDraw.groupby('avg rev').count().drop(['link', 'total rev'], axis=1)
byAvgRev
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
    </tr>
    <tr>
      <th>avg rev</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3.0</th>
      <td>2</td>
    </tr>
    <tr>
      <th>3.5</th>
      <td>7</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>46</td>
    </tr>
    <tr>
      <th>4.5</th>
      <td>116</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>92</td>
    </tr>
  </tbody>
</table>
</div>




```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(
    x=byAvgRev.index,
    y=byAvgRev['name'])])

fig.update_layout(title_text='Top 270 Barber Shops in California, CA Average Review',
                  yaxis=dict(title='count'),
                  xaxis=dict(title='avg rev'))

fig.show()
```


<div>


            <div id="d541837a-efd8-4127-b278-a0b49ef86d23" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("d541837a-efd8-4127-b278-a0b49ef86d23")) {
                    Plotly.newPlot(
                        'd541837a-efd8-4127-b278-a0b49ef86d23',
                        [{"type": "bar", "x": [3.0, 3.5, 4.0, 4.5, 5.0], "y": [2, 7, 46, 116, 92]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Top 270 Barber Shops in California, CA Average Review"}, "xaxis": {"title": {"text": "avg rev"}}, "yaxis": {"title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('d541837a-efd8-4127-b278-a0b49ef86d23');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>


### A histogram displays reviews in range 4.0-5.0


```python
output_hist = output_toDraw[output_toDraw['avg rev'] >= 4.0]
```


```python
fig = px.histogram(output_hist, x="total rev", nbins=20, color='avg rev')

fig.update_layout(title_text='Top 270 Barber Shops in California, CA Average Review',
                  yaxis=dict(title='count'),
                  xaxis=dict(title='avg rev'))

fig.show()
```


<div>


            <div id="943947e0-6b5a-474d-88df-11cc969d51dd" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("943947e0-6b5a-474d-88df-11cc969d51dd")) {
                    Plotly.newPlot(
                        '943947e0-6b5a-474d-88df-11cc969d51dd',
                        [{"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=4.5<br>total rev=%{x}<br>count=%{y}", "legendgroup": "4.5", "marker": {"color": "#636efa"}, "name": "4.5", "nbinsx": 20, "offsetgroup": "4.5", "orientation": "v", "showlegend": true, "type": "histogram", "x": [170, 240, 125, 179, 139, 113, 184, 51, 64, 151, 161, 947, 81, 183, 61, 14, 105, 129, 18, 49, 87, 144, 71, 34, 44, 87, 34, 58, 45, 46, 69, 68, 137, 127, 71, 98, 67, 234, 8, 146, 943, 20, 148, 94, 445, 118, 106, 11, 203, 43, 28, 19, 131, 37, 165, 7, 4, 87, 111, 35, 26, 13, 204, 8, 99, 180, 263, 6, 66, 8, 56, 58, 21, 67, 63, 75, 25, 11, 39, 133, 8, 79, 58, 4, 106, 26, 10, 52, 250, 125, 185, 39, 21, 150, 234, 1082, 15, 13, 15, 106, 49, 191, 11, 95, 9, 176, 31, 410, 52, 37, 58, 147, 23, 618, 8, 10], "xaxis": "x", "yaxis": "y"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=4.0<br>total rev=%{x}<br>count=%{y}", "legendgroup": "4.0", "marker": {"color": "#EF553B"}, "name": "4.0", "nbinsx": 20, "offsetgroup": "4.0", "orientation": "v", "showlegend": true, "type": "histogram", "x": [253, 220, 50, 953, 50, 116, 245, 86, 90, 51, 120, 78, 67, 32, 30, 487, 5, 5, 171, 160, 93, 80, 100, 86, 122, 54, 56, 72, 5, 16, 15, 383, 46, 5, 14, 12, 321, 1021, 13, 24, 52, 56, 407, 153, 19, 20], "xaxis": "x", "yaxis": "y"}, {"alignmentgroup": "True", "bingroup": "x", "hoverlabel": {"namelength": 0}, "hovertemplate": "avg rev=5.0<br>total rev=%{x}<br>count=%{y}", "legendgroup": "5.0", "marker": {"color": "#00cc96"}, "name": "5.0", "nbinsx": 20, "offsetgroup": "5.0", "orientation": "v", "showlegend": true, "type": "histogram", "x": [118, 55, 15, 10, 428, 14, 45, 137, 111, 20, 18, 74, 50, 10, 47, 12, 31, 21, 3, 28, 63, 56, 30, 26, 3, 6, 1, 12, 9, 55, 2, 57, 36, 28, 1, 27, 12, 11, 13, 51, 1, 6, 58, 57, 15, 15, 56, 9, 1, 2, 51, 4, 14, 19, 163, 6, 5, 61, 3, 5, 32, 39, 101, 4, 25, 18, 44, 848, 71, 2, 2, 61, 4, 120, 6, 65, 2, 19, 8, 11, 19, 2, 2, 90, 76, 19, 25, 11, 52, 38, 7, 2], "xaxis": "x", "yaxis": "y"}],
                        {"barmode": "relative", "legend": {"title": {"text": "avg rev"}, "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Top 270 Barber Shops in California, CA Average Review"}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "title": {"text": "avg rev"}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "title": {"text": "count"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('943947e0-6b5a-474d-88df-11cc969d51dd');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>

