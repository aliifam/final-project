const approveReview = async (reviewId) => {
    if (!reviewId) return;
    try {
        await axios.put(
            `${import.meta.env.VITE_API_URL}/review/${reviewId}/approve`,
            {},
            {
                headers: { Authorization: `Bearer ${authStore.accessToken}` }
            }
        );
        toast.add({ severity: 'success', summary: 'Success', detail: 'Review approved successfully' });
        fetchReviews();
        if (selectedReview.value && selectedReview.value.id === reviewId) {
            selectedReview.value.showed = true;
        }
        dialog.value = false;
    } catch (error) {
        console.error('Failed to approve review:', error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to approve review' });
    }
};

const rejectReview = async (reviewId) => {
    if (!reviewId) return;
    try {
        await axios.put(
            `${import.meta.env.VITE_API_URL}/review/${reviewId}/hide`, // Assuming 'hide' is the correct endpoint for reject/hide
            {},
            {
                headers: { Authorization: `Bearer ${authStore.accessToken}` }
            }
        );
        toast.add({ severity: 'success', summary: 'Success', detail: 'Review hidden successfully' }); // Updated message
        fetchReviews();
        if (selectedReview.value && selectedReview.value.id === reviewId) {
            selectedReview.value.showed = false;
        }
        dialog.value = false;
    } catch (error) {
        console.error('Failed to hide review:', error);
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to hide review' });
    }
};