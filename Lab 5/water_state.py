def water_state(temp):
    if temp > 100:
        print("Steam")
    elif temp < 0:
        print("Ice")
    else:
        print("Liquid")
        
water_state(89)
water_state(-1)
water_state(101)