const fetchHotel = async (slug, checkin, checkout) => {
  try {
    isLoading.value = true;
    const response = await axios.get(
      `${
        import.meta.env.VITE_API_URL
      }/hotel/${slug}?checkin=${checkin}&checkout=${checkout}`
    );

    hotel.value = response.data.hotel;
    roomCounts.value = hotel.value.pod_types.reduce((acc, room) => {
      //based on room.id
      acc[room.id] = 1; // Set default count to 1 for each room type
      return acc;
    }, {});
    // console.log("hotel", hotel.value.images);
  } catch (error) {
    console.error("Error fetching hotel data:", error);
    router.push({ name: "notfound" });
    // toast.error("Gagal mengambil data hotel");
  } finally {
    isLoading.value = false;
  }
};