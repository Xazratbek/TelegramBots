from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
import requests
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/info - Yordam",
            )

    await message.answer("\n".join(text))

@dp.message_handler(commands=['info'])
async def bot_info(message: types.Message):
    text = ("Imkoniyatlarim: ",
            "Facebook - Video va Reels yuklab berish",
            "Instagram - Reels, Istoriya, Post yuklab berish",
            "Youtube - Videoni istalgan sifatda yoki audio ko'rinishida yuklab berish",
            "Twitter - Video yuklash",
            "Snapchat - Video yuklash",
            "Pinterest - Rasm va Video yuklash",
            )

    await message.answer("\n".join(text))

# async def reverse_geocode(latitude, longitude):

#     url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key=7680723fe9ed42899e7e8288061132a0"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         if 'results' in data and data['results']:
#             result = data['results'][0]
#             formatted_address = result.get('formatted', 'Address not found')
#             return formatted_address
#         else:
#             return 'No results found'
#     else:
#         return 'Error fetching data'

# # Usage in your Aiogram handler
# @dp.message_handler(content_types=['location'])
# async def handle_location(message: types.Message):
#     location = message.location
#     latitude = location.latitude
#     longitude = location.longitude

#     # Get the address from reverse geocoding
#     address = await reverse_geocode(latitude, longitude)

#     # Send the address back to the user
#     await message.answer(f"Location Address: {address}")


from geopy.geocoders import Nominatim

async def reverse_geocode(latitude, longitude):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="reverse_geocode_bot")

    # Combine latitude and longitude into a single string
    location = f"{latitude}, {longitude}"

    try:
        # Perform reverse geocoding
        location_info = geolocator.reverse(location)

        # Extract the formatted address
        formatted_address = location_info.address if location_info else "Address not found"
        return formatted_address

    except Exception as e:
        return f"Error: {str(e)}"

# Usage in your Aiogram handler
@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude

    # Get the address from reverse geocoding
    address = await reverse_geocode(latitude, longitude)

    # Send the address back to the user
    await message.answer(f"Location Address: {address}")
