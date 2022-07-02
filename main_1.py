from fastapi import FastAPI
import fastapi
from enum import Enum

app = FastAPI()

# asyncio is used as a foundation for multiple Python asynchronous frameworks
# that provide high-performance network and web-servers, database connection 
# libraries, distributed task queues, etc.

class AvailableCuisines(str, Enum) :
    indian = 'indian'
    american = "american"
    italian = 'italian'

food_items = {
    'indian' : [ 'Samosa', 'Dosa' ],
    'american' : [ 'Hot Dog', 'Apple pie' ],
    'italian' : [ 'Ravioli', 'pizza' ]
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}") # Entity point it should be written the request
async def hello(cuisine: AvailableCuisines) :

    # In flask
    # if cuisine not in valid_cuisines :
    #     return f'Supported cuisines are {valid_cuisines}'

    # In fastapi
    return food_items.get(cuisine)


coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

# http://127.0.0.1:8000/doc This will give you the documentation of fast api
# http://127.0.0.1:8000/redoc This will give you another documentation of fast api

# If you give an invliad integer it will give an error
@app.get('/get_coupon/{code}')
async def get_items(code: int):
    return { 'discount_amount' : coupon_code.get(code)}