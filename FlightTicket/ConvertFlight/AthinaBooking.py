def return_Athina_booking_text(airline: str, flight_number: str,
                               departure_airport: str, arrival_airport: str,
                               departure_time: str, arrival_time: str):
    r = f"1. {airline}  {flight_number} E  30JUN {departure_airport}{arrival_airport} HS1  " \
        f"{departure_time}   {arrival_time}  O        E SU"

    return r
