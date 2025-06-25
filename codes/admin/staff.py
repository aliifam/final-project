def get_staffs_by_hotel(hotel_id):
    try:
        hotel = Hotel.query.get(int(hotel_id))
        if not hotel:
            return jsonify({"error": "Hotel not found"}), 404
        staffs = (
            db.session.query(Admin)
            .join(AdminHotel, AdminHotel.admin_id == Admin.id)
            .filter(AdminHotel.hotel_id == hotel.id)
            .all()
        )
        result = [{
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "role": s.role.value if isinstance(s.role, RoleEnum) else s.role,
            "hotel_ids": get_staff_hotels(s.id),
        } for s in staffs]
        return jsonify(result), 200
    except:
        # log error stack
        logging.error("Error getting staffs by hotel", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500