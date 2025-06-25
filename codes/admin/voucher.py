def get_vouchers_for_hotel(hotel_id):
    try:
        vouchers = Voucher.query.join(VoucherHotel).filter(VoucherHotel.hotel_id == int(hotel_id)).order_by(Voucher.created_at.desc()).all()
        voucher_list = []
        for voucher in vouchers:
            voucher_data = {
                "id": voucher.id,
                "name": voucher.name,
                "description": voucher.description,
                "code": voucher.code,
                "discount_type": voucher.type.name,
                "discount_max": voucher.discount_max,
                "discount_amount": voucher.discount_amount,
                "current_usage":  voucher.current_usage or 0,
                "current_budget": voucher.current_budget or 0,
                "discount_percentage": voucher.discount_percentage,
                "min_transaction": voucher.min_transaction,
                "image": voucher.image,
                "max_usage": voucher.max_usage,
                "max_budget": voucher.max_budget,
                "start_at": voucher.start_at,
                "end_at": voucher.end_at,
                "checkin_at": voucher.checkin_at,
                "checkout_at": voucher.checkout_at,
                "showed_in_customer": voucher.showed_in_customer,
                "is_active": voucher.is_active,
                "hotel_ids": [vh.hotel.id for vh in voucher.hotels],
                "hotels": [{"id": vh.hotel.id, "name": vh.hotel.name} for vh in voucher.hotels],
            }
            voucher_list.append(voucher_data)
        return jsonify(voucher_list), 200
    except Exception:
        logging.error("Failed to get vouchers", exc_info=True)
        return jsonify({"message": "Failed to get vouchers"}), 500