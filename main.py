from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#INPUTS : Price[*] , Quantity[*] , Name[*] , Duration[*].
#Im gonna use nested Dics

quantity = 1
duration = 2

spotifyFamily = {
    "title" :"Family plan",
    "prices" : ["50,000", "150,000", "300,000"],
    "quantityDict" : quantity,
    "durationDict" : duration
}

spotifySolo = {
    "title" :"اسپاتیفای شخصی",
    "prices" : ["100,000","250,000","550,000","970,000"],
    "quantityDict" : quantity,
    "durationDict" : duration
}

canva = {
    "title" :"کانوا پریمیوم",
    "prices" : ["100,000","200,000"],
    "quantityDict" : quantity,
    "durationDict" : duration
}


products = {

    "Sporify_Family": spotifyFamily,
    "Spotify_Solo" : spotifySolo,
    "canva_premium" : canva 

}

#ورود عکس
image = Image.open("source.png")

#read abbout Pillow
#calling ImageDraw in an var + Font & Font Size
IM = ImageDraw.Draw(image)
vazir = ImageFont.truetype('Vazirmatn-Regular',125)
 
#Writing Part
IM.text((80,200), "Mohsen", (50,50,50), vazir)


#Exporting
image.show
image.save("mm.png")
