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
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}<br>
<br>
Field details:<br><br>
<b>cart_value</b><br>	        Integer	Value of the shopping cart in cents.	790 (790 cents = 7.90€)<br><br>
<b>delivery_distance</b><br>	Integer	The distance between the store and customer’s location in meters.	2235 (2235 meters = 2.235 km)<br><br>
<b>number_of_items</b><br> 	Integer	The number of items in the customer's shopping cart.	4 (customer has 4 items in the cart)<br><br>
<b>time</b><br>	            String	Order time in ISO format.	2021-01-16T13:00:00Z<br><br>

<br>
<br>
Response
Example:<br>
{"delivery_fee": 710}<br>
<br>
Field details:<br><br>
<b>delivery_fee</b><br>	    Integer	Calculated delivery fee in cents.	710 (710 cents = 7.10€)
