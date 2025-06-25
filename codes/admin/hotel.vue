const fetchHotels = async () => {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/hotel/${id}`, {
        headers: { Authorization: `Bearer ${authStore.accessToken}` }
    });
    if (response.status !== 200) {
        console.error('Failed to fetch hotels:', response);
        return;
    }
    data.value = response.data;
    data.value.facilities_id = response.data.facilities.map((facility) => facility);
    data.value.city_id = response.data.city_id;
    images.value = response.data.images.map((image) => ({
        url: image.url,
        caption: image.caption,
        order: image.order
    }));
    console.log('Hotel data:', data.value);
    initMap();
    data.value.latitude = response.data.latitude;
    data.value.longitude = response.data.longitude;
};