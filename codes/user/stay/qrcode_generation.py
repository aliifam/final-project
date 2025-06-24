hotel = Hotel.query.filter_by(id=pod.pod_type.hotel_id).first()
hotel_timezone = hotel.timezone if hotel and hotel.timezone else "Asia/Jakarta"
checkout_datetime = datetime.combine(booking.check_out, hotel.checkout_time)
hotel_tz = pytz.timezone(hotel_timezone)
localized_checkout = hotel_tz.localize(checkout_datetime)
current_expired = int(localized_checkout.timestamp())
qrcode = QRCode.query.filter_by(pod_id=pod.id).first()
next_code = qr_key_generator()
next_code_image = generate_qr(next_code)
qrcode.current_code=qrcode.next_code
qrcode.current_code_image=qrcode.next_code_image
qrcode.next_code=next_code
qrcode.next_code_image=next_code_image
qrcode.current_expired = current_expired
qrcode.booking_id = booking.id        
booking.status = BookingStatusEnum.CHECKED_IN
pod.status = PodStatusEnum.OCCUPIED