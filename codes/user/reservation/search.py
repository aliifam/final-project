def count_available_pods(pod_type_id, checkin_date, checkout_date):
    # Total pod dari tipe ini yang avail dan tidak maintenance
    total_pods = db.session.query(Pod).filter(Pod.pod_type_id == pod_type_id).count()

    # Booking aktif pada rentang waktu itu untuk tipe ini
    overlapping_bookings = db.session.query(Booking).filter(
        Booking.pod_type_id == pod_type_id,  # <- asumsi kamu simpan ini di tabel booking
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