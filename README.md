# deliveryCalculator
Back-end preliminary assignment https://github.com/woltapp/engineering-summer-intern-2023/blob/main/README.md

<br>
<br>
Implement an HTTP API (single endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and 
includes the calculated delivery fee in the response payload (JSON).
<br>
<br>
<br>
Request
Example:<br>
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}

Field details:<br>
cart_value:<br>	        Integer	Value of the shopping cart in cents.	790 (790 cents = 7.90€)<br>
delivery_distance:<br>	Integer	The distance between the store and customer’s location in meters.	2235 (2235 meters = 2.235 km)<br>
number_of_items:<br> 	Integer	The number of items in the customer's shopping cart.	4 (customer has 4 items in the cart)<br>
time:<br>	            String	Order time in ISO format.	2021-01-16T13:00:00Z<br>

<br>
Response
Example:<br>
{"delivery_fee": 710}

Field details:<br>
delivery_fee:<br>	    Integer	Calculated delivery fee in cents.	710 (710 cents = 7.10€)
