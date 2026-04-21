from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# 🔹 Models
class BookingRequest(BaseModel):
    guest_name: str = Field(..., min_length=2)
    room_id: int = Field(..., gt=0)
    nights: int = Field(..., gt=0, le=30)
    phone: str = Field(..., min_length=10)
    meal_plan: str = "none"
    early_checkout: bool = False


class NewRoom(BaseModel):
    room_number: str = Field(..., min_length=1)
    type: str = Field(..., min_length=2)
    price_per_night: int = Field(..., gt=0)
    floor: int = Field(..., gt=0)
    is_available: bool = True


# 🔹 Data
rooms = [
    {"id": 1, "room_number": "101", "type": "Single", "price_per_night": 2000, "floor": 1, "is_available": True},
    {"id": 2, "room_number": "102", "type": "Double", "price_per_night": 3000, "floor": 1, "is_available": True},
    {"id": 3, "room_number": "201", "type": "Suite", "price_per_night": 5000, "floor": 2, "is_available": False},
    {"id": 4, "room_number": "202", "type": "Deluxe", "price_per_night": 4000, "floor": 2, "is_available": True},
    {"id": 5, "room_number": "301", "type": "Single", "price_per_night": 2200, "floor": 3, "is_available": True},
    {"id": 6, "room_number": "302", "type": "Suite", "price_per_night": 5500, "floor": 3, "is_available": False}
]

bookings = []
booking_counter = 1


# 🔹 Helper Functions
def find_room(room_id: int):
    for room in rooms:
        if room["id"] == room_id:
            return room
    return None


def calculate_stay_cost(price_per_night: int, nights: int, meal_plan: str):
    total = price_per_night * nights

    if meal_plan == "breakfast":
        total += 500 * nights
    elif meal_plan == "all-inclusive":
        total += 1200 * nights

    return total


def filter_rooms_logic(type=None, max_price=None, floor=None, is_available=None):
    filtered = []

    for room in rooms:
        if type is not None and room["type"].lower() != type.lower():
            continue
        if max_price is not None and room["price_per_night"] > max_price:
            continue
        if floor is not None and room["floor"] != floor:
            continue
        if is_available is not None and room["is_available"] != is_available:
            continue

        filtered.append(room)

    return filtered


# 🔹 Routes

@app.get("/")
def home():
    return {"message": "Welcome to Grand Stay Hotel"}


@app.get("/rooms")
def get_rooms():
    total = len(rooms)
    available_count = sum(1 for room in rooms if room["is_available"])

    return {
        "total_rooms": total,
        "available_rooms": available_count,
        "rooms": rooms
    }

@app.post("/checkin/{booking_id}")
def checkin(booking_id: int):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            booking["status"] = "checked_in"
            return booking

    return {"error": "Booking not found"}

@app.post("/checkout/{booking_id}")
def checkout(booking_id: int):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            booking["status"] = "checked_out"

            room = find_room(booking["room_id"])
            if room:
                room["is_available"] = True

            return booking

    return {"error": "Booking not found"}

@app.get("/rooms/summary")
def rooms_summary():
    total = len(rooms)
    available = sum(1 for room in rooms if room["is_available"])
    occupied = total - available

    prices = [room["price_per_night"] for room in rooms]

    type_count = {}
    for room in rooms:
        room_type = room["type"]
        type_count[room_type] = type_count.get(room_type, 0) + 1

    return {
        "total_rooms": total,
        "available_rooms": available,
        "occupied_rooms": occupied,
        "cheapest_price": min(prices),
        "most_expensive_price": max(prices),
        "room_type_breakdown": type_count
    }


@app.get("/rooms/filter")
def filter_rooms(
    type: str = None,
    max_price: int = None,
    floor: int = None,
    is_available: bool = None
):
    result = filter_rooms_logic(type, max_price, floor, is_available)

    return {
        "total_found": len(result),
        "rooms": result
    }


@app.post("/rooms", status_code=201)
def add_room(new_room: NewRoom):
    for room in rooms:
        if room["room_number"].lower() == new_room.room_number.lower():
            return {"error": "Room number already exists"}

    new_id = max(room["id"] for room in rooms) + 1

    room = {
        "id": new_id,
        "room_number": new_room.room_number,
        "type": new_room.type,
        "price_per_night": new_room.price_per_night,
        "floor": new_room.floor,
        "is_available": new_room.is_available
    }

    rooms.append(room)
    return room

@app.get("/rooms/browse")
def browse_rooms(
    keyword: str = None,
    sort_by: str = "price_per_night",
    order: str = "asc",
    page: int = 1,
    limit: int = 2
):
    
    # 🔹 Step 1: Start with all rooms
    data = rooms

    # 🔹 Step 2: Filter (search)
    if keyword:
        data = [
            room for room in data
            if keyword.lower() in room["room_number"].lower()
            or keyword.lower() in room["type"].lower()
        ]

    # 🔹 Step 3: Sort
    valid_fields = ["price_per_night", "floor", "type"]

    if sort_by not in valid_fields:
        return {"error": "Invalid sort field"}

    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    reverse = True if order == "desc" else False
    data = sorted(data, key=lambda x: x[sort_by], reverse=reverse)

    # 🔹 Step 4: Pagination
    if page < 1 or limit < 1 or limit > 10:
        return {"error": "Invalid page or limit"}

    total = len(data)
    start = (page - 1) * limit
    end = start + limit

    paginated_data = data[start:end]
    total_pages = (total + limit - 1) // limit

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_results": total,
        "total_pages": total_pages,
        "rooms": paginated_data
    }

@app.put("/rooms/{room_id}")
def update_room(
    room_id: int,
    price_per_night: int = None,
    is_available: bool = None
):
    room = find_room(room_id)

    if not room:
        return {"error": "Room not found"}

    # update only if values provided
    if price_per_night is not None:
        room["price_per_night"] = price_per_night

    if is_available is not None:
        room["is_available"] = is_available

    return room
@app.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    room = find_room(room_id)

    if not room:
        return {"error": "Room not found"}

   
    if not room["is_available"]:
        return {"error": "Cannot delete an occupied room"}

    rooms.remove(room)

    return {
        "message": "Room deleted successfully",
        "room_number": room["room_number"]
    }

@app.get("/rooms/search")
def search_rooms(keyword: str):
    results = []

    for room in rooms:
        if (
            keyword.lower() in room["room_number"].lower()
            or keyword.lower() in room["type"].lower()
        ):
            results.append(room)

    if not results:
        return {"message": "No matching rooms found"}

    return {
        "total_found": len(results),
        "rooms": results
    }

@app.get("/rooms/sort")
def sort_rooms(sort_by: str = "price_per_night", order: str = "asc"):
    
    valid_fields = ["price_per_night", "floor", "type"]

    #  invalid sort_by
    if sort_by not in valid_fields:
        return {"error": "Invalid sort field"}

    # invalid order
    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    reverse = True if order == "desc" else False

    sorted_rooms = sorted(rooms, key=lambda x: x[sort_by], reverse=reverse)

    return {
        "sorted_by": sort_by,
        "order": order,
        "rooms": sorted_rooms
    }

@app.get("/rooms/page")
def paginate_rooms(page: int = 1, limit: int = 2):
    
    # ❌ validation
    if page < 1 or limit < 1 or limit > 10:
        return {"error": "Invalid page or limit"}

    total = len(rooms)

    start = (page - 1) * limit
    end = start + limit

    data = rooms[start:end]

    total_pages = (total + limit - 1) // limit  

    return {
        "page": page,
        "limit": limit,
        "total_rooms": total,
        "total_pages": total_pages,
        "rooms": data
    }

@app.get("/rooms/{room_id}")
def get_room(room_id: int):
    room = find_room(room_id)
    if room:
        return room
    return {"error": "Room not found"}

@app.get("/bookings/search")
def search_bookings(guest_name: str):
    results = []

    for booking in bookings:
        if guest_name.lower() in booking["guest_name"].lower():
            results.append(booking)

    return {
        "total_found": len(results),
        "bookings": results
    }

@app.get("/bookings/sort")
def sort_bookings(order: str = "asc"):

    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    reverse = True if order == "desc" else False

    sorted_data = sorted(bookings, key=lambda x: x["total_cost"], reverse=reverse)

    return {
        "order": order,
        "bookings": sorted_data
    }

@app.get("/bookings/active")
def get_active_bookings():
    active = []

    for booking in bookings:
        if booking["status"] in ["confirmed", "checked_in"]:
            active.append(booking)

    return {
        "total_active": len(active),
        "bookings": active
    }



@app.post("/bookings")
def create_booking(request: BookingRequest):
    global booking_counter

    room = find_room(request.room_id)
    if not room:
        return {"error": "Room not found"}

    if not room["is_available"]:
        return {"error": "Room is not available"}

    total_cost = calculate_stay_cost(
        room["price_per_night"],
        request.nights,
        request.meal_plan
    )

    discount = 0
    if request.early_checkout:
        discount = total_cost * 0.10
        total_cost -= discount

    booking = {
        "booking_id": booking_counter,
        "guest_name": request.guest_name,
        "room_id": request.room_id,
        "room_number": room["room_number"],
        "nights": request.nights,
        "meal_plan": request.meal_plan,
        "total_cost": total_cost,
        "discount_applied": discount,
        "status": "confirmed"
    }

    room["is_available"] = False

    bookings.append(booking)
    booking_counter += 1

    return booking


@app.get("/bookings")
def get_bookings():
    return {
        "total_bookings": len(bookings),
        "bookings": bookings
    }