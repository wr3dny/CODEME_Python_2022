print('#1 ze "sztywnymi" danymi\n')
usage_fuel = 6.4
distanse = 120
price_of_fuel = 5.04

trip_fuel_usage = distanse / 100 * usage_fuel

print(trip_fuel_usage, 'litrów')

price_of_trip = trip_fuel_usage * price_of_fuel

# z możliwością wyboru danych - zadanie domowe

print('\n#2\n')

average_fuel_usage = float(input('Give Your vehical average fuel usage: '))
predicted_distance = float(input('Whats Your predicted distance: '))
fuel_price = float(input('How much for gas: '))

user_cost_of_traveling = predicted_distance / 100 * average_fuel_usage * fuel_price

print('This trip will cost You', round(user_cost_of_traveling,2), 'coins')