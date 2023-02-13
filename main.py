from flask import Flask, request, jsonify
from delivery_calculator import surcharge, travel_fee, item_surcharge, is_rush
import datetime

app = Flask(__name__)


# Responds to a post request with the total delivery fee in Cents from the order.
@app.route("/delivery_fee", methods=["POST"])
def calculate_delivery_fee():

    try:
        order = request.get_json()

        required_fields = ["cart_value", "delivery_distance", "number_of_items", "time"]
        missing_fields = []

        # Check that payload has all the required fields.
        for field in required_fields:
            if field not in order:
                missing_fields.append(field)
        if missing_fields:
            raise KeyError(", ".join(missing_fields))

        # Get all the required fields.
        cart_value = order["cart_value"]
        delivery_distance = order["delivery_distance"]
        number_of_items = order["number_of_items"]
        time = order["time"]

        # Check for types in payload.
        if type(cart_value) != int:
            raise TypeError("cart_value should be an integer")
        if type(delivery_distance) != int:
            raise TypeError("delivery_distance should be an integer")
        if type(number_of_items) != int:
            raise TypeError("number_of_items should be an integer")
        if type(time) != str:
            raise TypeError("time should be a string")
        try:
            datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise ValueError("time should be in ISO 8601 format")

        if cart_value >= 10000:
            return 0

        total = surcharge(cart_value / 100) + travel_fee(delivery_distance) + item_surcharge(number_of_items)

        if is_rush(time):
            total *= 1.2

        # Convert from Euros to Cents.
        total = int(round(total * 100, 2))

        if total > 1500:
            total = 1500

        # Response payload
        response = {"delivery_fee": total}
        return jsonify(response), 200
    except KeyError as e:
        return jsonify({"error": f"Bad Request: Missing required fields '{e.args[0]}' in request body"}), 400
    except TypeError as e:
        return jsonify({"error": f"Bad Request: Incorrect type for field: '{e.args[0]}'"}), 400
    except ValueError as e:
        return jsonify({"error": f"Bad Request: {e.args[0]}"}), 400
    except:
        return jsonify({"error": "Bad Request: Invalid JSON in request body"}), 400


if __name__ == "__main__":
    app.run(debug=True)