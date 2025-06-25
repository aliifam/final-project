def calculate_dynamic_price(pod_type, checkin_date, checkout_date):
    delta_days = (checkout_date - checkin_date).days
    total_price = 0
    pricing_map = {
        dp.date: dp.price for dp in pod_type.dynamic_pricing if dp.active
    }
    for i in range(delta_days):
        date = checkin_date + datetime.timedelta(days=i)
        price = pricing_map.get(date, pod_type.price)
        total_price += price
    total_price = int(total_price) 
    per_night_price = total_price // delta_days if delta_days > 0 else 0
    markup_percent = deterministic_markup_percentage(pod_type.id, checkin_date, checkout_date)
    original_price = int(total_price * (1 + markup_percent / 100))
    return total_price, original_price, markup_percent, per_night_price
    
def deterministic_markup_percentage(pod_type_id, checkin_date, checkout_date):
    key = f"{pod_type_id}-{checkin_date}-{checkout_date}"
    hash_value = hashlib.md5(key.encode()).hexdigest()
    seed = int(hash_value, 16)
    random.seed(seed)
    return random.randint(10, 30)  # percent 10-30%