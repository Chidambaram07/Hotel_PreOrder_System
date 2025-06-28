function updateOrderStatus(orderId, status, button) {
    const csrfToken = document.getElementById("csrf-token").value;

    fetch(`/update-order-status/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ order_id: orderId, status: status })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Disable the clicked button
            button.disabled = true;

            // Disable all lower-status buttons
            const buttons = document.querySelectorAll(`[data-order-id="${orderId}"]`);
            buttons.forEach(btn => {
                const btnStatus = parseInt(btn.getAttribute("data-status"));
                if (btnStatus < status) {
                    btn.disabled = true;
                }
            });
        } else {
            alert("Failed to update the order status.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong.");
    });
}
