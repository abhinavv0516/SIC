# Constants
total_land_acres = 80
segments = 5
land_per_segment = total_land_acres / segments

# Crop yields and selling prices
tomato_yield_1 = 10  # tonnes per acre (30% of land)
tomato_yield_2 = 12  # tonnes per acre (70% of land)
tomato_price = 7     # Rs. per kg
potato_yield = 10    # tonnes per acre
potato_price = 20    # Rs. per kg
cabbage_yield = 14   # tonnes per acre
cabbage_price = 24   # Rs. per kg
sunflower_yield = 0.7 # tonnes per acre
sunflower_price = 200 # Rs. per kg
sugarcane_yield = 45  # tonnes per acre
sugarcane_price = 4000 # Rs. per tonne

# Calculating overall sales
# Tomato sales
tomato_land_acres = land_per_segment
tomato_sales_1 = (tomato_land_acres * 0.3 * tomato_yield_1) * 1000 * tomato_price
tomato_sales_2 = (tomato_land_acres * 0.7 * tomato_yield_2) * 1000 * tomato_price
total_tomato_sales = tomato_sales_1 + tomato_sales_2

# Potato sales
potato_land_acres = land_per_segment
total_potato_sales = (potato_land_acres * potato_yield) * 1000 * potato_price

# Cabbage sales
cabbage_land_acres = land_per_segment
total_cabbage_sales = (cabbage_land_acres * cabbage_yield) * 1000 * cabbage_price

# Sunflower sales
sunflower_land_acres = land_per_segment
total_sunflower_sales = (sunflower_land_acres * sunflower_yield) * 1000 * sunflower_price

# Sugarcane sales
sugarcane_land_acres = land_per_segment
total_sugarcane_sales = (sugarcane_land_acres * sugarcane_yield) * sugarcane_price

# Total overall sales
total_overall_sales = (total_tomato_sales + total_potato_sales + total_cabbage_sales +
                       total_sunflower_sales + total_sugarcane_sales)

# Sales realisation from chemical-free farming after 11 months
# Chemical-free farming for tomatoes, potatoes, cabbage, and sunflower
total_chemical_free_sales = (total_tomato_sales + total_potato_sales + total_cabbage_sales +
                             total_sunflower_sales)
# Sugarcane will be chemical-free after 11 months, so exclude sugarcane sales
total_chemical_free_sales_11_months = total_chemical_free_sales

# Print results
print(f"Overall sales achieved by Mahesh from 80 acres of land: Rs. {total_overall_sales:.2f}")
print(f"Sales realization from chemical-free farming at the end of 11 months: Rs. {total_chemical_free_sales_11_months:.2f}")
