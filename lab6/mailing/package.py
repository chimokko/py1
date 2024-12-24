def calculate_price(distance, time, weight, volume, delivery_type):
    price = distance*0.3 + weight + time*0.1 + volume*0.1
    if delivery_type=="express":
        price*=1.5
    return price    