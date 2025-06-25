admin_hotels = []
if admin.role != RoleEnum.SUPERADMIN:
    logging.info(f"Admin ID: {admin.id}, {admin.role.value}")
    hotels = (
        db.session.query(Hotel)
        .join(AdminHotel, AdminHotel.hotel_id == Hotel.id)
        .filter(AdminHotel.admin_id == admin.id)
        .all()
    )
    admin_hotels = [
        {field: getattr(hotel, field) for field in [
            "id", "name", "address", "slug"
        ]}
        for hotel in hotels
    ]

access_token = create_access_token(identity=admin.id, additional_claims={"role": admin.role.value})
refresh_token = create_refresh_token(identity=admin.id, additional_claims={"role": admin.role.value})
# returning all admin data
return jsonify({
    "message": "Login success",
    "admin" : {
        "id": admin.id,
        "email": admin.email,
        "avatar": admin.avatar,
        "role": admin.role.value,
        "name": admin.name,
        "hotels": admin_hotels 
    },
    "access_token": access_token,
    "refresh_token": refresh_token
})