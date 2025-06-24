def get_stays():
    try:
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404
        automate_booking_lifecycle()
        stays = Booking.query.options(
            joinedload(Booking.pod_type).joinedload(PodType.hotel),
            joinedload(Booking.pod),
        ).filter(
            Booking.user_id == user.id,
            Booking.status.in_([BookingStatusEnum.BOOKED, BookingStatusEnum.CHECKED_IN, BookingStatusEnum.CHECKED_OUT, BookingStatusEnum.CANCELLED]),
        ).order_by(Booking.check_in.desc()).all()
        results = []
        for stay in stays:
            results.append({
                "id": stay.id,
                "hotel_name": stay.pod_type.hotel.name if stay.pod_type and stay.pod_type.hotel else None,
                "hotel_check_in": stay.pod_type.hotel.checkin_time.strftime("%H:%M") if stay.pod_type and stay.pod_type.hotel else None,
                "hotel_check_out": stay.pod_type.hotel.checkout_time.strftime("%H:%M") if stay.pod_type and stay.pod_type.hotel else None,
                "room_type": stay.pod_type.name if stay.pod_type else None,
                "room_type_id": stay.pod_type.id if stay.pod_type else None,
                "check_in": stay.check_in.isoformat() if stay.check_in else None,
                "check_out": stay.check_out.isoformat() if stay.check_out else None,
                "night" : (stay.check_out - stay.check_in).days if stay.check_in and stay.check_out else None,
                "status": stay.status.value,
                "pod": {
                    "id": stay.pod.id,
                    "name": stay.pod.name,
                } if stay.pod else None,
            })

        return jsonify(results), 200
    except Exception as e:
        logging.error(str(e), exc_info=True)
        return jsonify({"error": "Internal server error"}), 500