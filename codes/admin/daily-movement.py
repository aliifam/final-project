return jsonify({
    "date_in_hotel_tz": today_in_hotel_tz.isoformat(),
    "hotel_name": hotel.name,
    "expected_checkins": expected_checkins_list,
    "current_checkins": current_checkins_list,
    "expected_checkouts": expected_checkouts_list
}), 200