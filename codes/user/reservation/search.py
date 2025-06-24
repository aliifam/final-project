def count_available_pods(pod_type_id, checkin_date, checkout_date):
    total_pods = db.session.query(Pod).filter(Pod.pod_type_id == pod_type_id).count()
    overlapping_bookings = db.session.query(Booking).filter(
        Booking.pod_type_id == pod_type_id, 
        Booking.status.in_([
            BookingStatusEnum.PENDING,
            BookingStatusEnum.BOOKED,
            BookingStatusEnum.CHECKED_IN,
        ]),
        db.or_(
            db.and_(Booking.check_in <= checkin_date, Booking.check_out > checkin_date),
            db.and_(Booking.check_in >= checkin_date, Booking.check_in < checkout_date)
        )
    ).count()
    return total_pods - overlapping_bookings