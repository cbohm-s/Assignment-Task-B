import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''

    # Check if it's a restocking day (every 7 days starting from day 0)
    if current_day % 7 == 0:
        restocked_items = 2000 - available_items  # Restock to max of 2000
        available_items = 2000  # Update inventory to the maximum
        sales = 0  # No sales on restocking day
    else:
        restocked_items = 0  # No restocking on non-restocking days
        # Generate a random sales number up to 200, constrained by available items
        sales = random.randint(0, min(200, available_items))
        available_items -= sales  # Reduce available items by the number of sales

    # Update inventory records with the current day's data
    inventory_records.append((current_day, sales, restocked_items, available_items))


    return available_items
