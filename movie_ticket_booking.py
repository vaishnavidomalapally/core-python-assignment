def available_seats(total_seats, booked):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked]

def book_seat(booked, seat):
    if seat in booked:
        print("Seat already booked!")
    else:
        booked.append(seat)

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print("Seat was not booked")

total_seats = 10
booked_seats = [2, 5, 7]

book_seat_value = 3
cancel_seat_value = 5

book_seat(booked_seats, book_seat_value)
cancel_seat(booked_seats, cancel_seat_value)

print("Available seats:", available_seats(total_seats, booked_seats))
