hotel = Hotel.query.filter_by(id=pod.pod_type.hotel_id).first()
hotel_timezone = hotel.timezone if hotel and hotel.timezone else "Asia/Jakarta"
expired_cleaning_token = datetime.now(pytz.timezone(hotel_timezone)) + timedelta(hours=3)
expired_cleaning_token = int(expired_cleaning_token.timestamp())
qr_code = QRCode.query.filter_by(pod_id=pod.id).first()
next_code = qr_key_generator()
next_code_image = generate_qr(next_code)
qr_code.current_code = qr_code.next_code
qr_code.current_code_image = qr_code.next_code_image
qr_code.next_code = next_code
qr_code.next_code_image = next_code_image
qr_code.current_expired = expired_cleaning_token
qr_code.cleaning_id = cleaning.id