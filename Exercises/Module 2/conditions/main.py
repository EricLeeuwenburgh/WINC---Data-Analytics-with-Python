# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather,time_of_day,cow_milking_status,location_of_cows,season,slurry_tank,grass_status):  # input 7 factors for function to work
   
    #actions:
    cows_to_shed = location_of_cows == "pasture" and time_of_day == "night" or location_of_cows == "pasture" and weather == "rain"
    milk_cows = cow_milking_status == True and location_of_cows == "cowshed"
    fertilize_pasture = location_of_cows == "cowshed" and slurry_tank == True and weather != ("windy" or "sunny")
    mow_grass = grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "cowshed"
    wait = cows_to_shed == False and milk_cows == False and fertilize_pasture == False and mow_grass == False and cow_milking_status == False

    if cow_milking_status == True and location_of_cows == "pasture":
       print("take cows to cowshed")
       print("milk cows")
       print("take cows back to pasture")
    
    elif cows_to_shed:
        print("take cows to cowshed")

    elif milk_cows:
        print("Milk cows") 
        location_of_cows = "pasture"
   
    elif fertilize_pasture:
        print("Fertilize pasture")

    elif mow_grass:
        print("Mow grass")
    
    elif wait:
        print("Wait")

#farm_action("rainy", "night", False, 'cowshed', 'winter', True, True)   # fertilize pasture
#farm_action("rainy", "night", False, 'cowshed', 'winter', False, True)  # wait
#farm_action("windy", "night", True, 'cowshed', 'winter', True, True)    # milk cows
farm_action("sunny", "day", True, 'pasture', 'spring', False, True)     # take cows to cowshed + milk cows + take cows back to pasture