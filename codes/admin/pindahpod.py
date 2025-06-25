old_pod_status = old_pod_status.upper() if old_pod_status else PodStatusEnum.AVAILABLE.value
# update pod status
old_pod.status = PodStatusEnum[old_pod_status]
new_pod.status = PodStatusEnum.OCCUPIED
# generate new qr next and get qr old from new pod
old_qr_code = QRCode.query.filter_by(pod_id=old_pod.id).first()
new_qr_code = QRCode.query.filter_by(pod_id=new_pod.id).first()

hotel = Hotel.query.filter_by(id=new_pod.pod_type.hotel_id).first()
hotel_timezone = hotel.timezone if hotel and hotel.timezone else "Asia/Jakarta"
# get the timezone from hotel
checkout_datetime = datetime.combine(booking.check_out, hotel.checkout_time)
hotel_tz = pytz.timezone(hotel_timezone)
localized_checkout = hotel_tz.localize(checkout_datetime)
current_expired = int(localized_checkout.timestamp())

next_code = qr_key_generator()
next_code_image = generate_qr(next_code)

old_qr_code.booking_id = None

new_qr_code.booking_id = booking.id
new_qr_code.cleaning_id = None
new_qr_code.current_code = new_qr_code.next_code
new_qr_code.current_code_image = new_qr_code.next_code_image
new_qr_code.next_code = next_code
new_qr_code.next_code_image = next_code_image
new_qr_code.current_expired = current_expired

db.session.commit()