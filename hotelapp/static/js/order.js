let cartItems = [
    { id: 1, name: "Tasty Dish 01", quantity: 2, price: 10 },
    { id: 2, name: "Delicious Dish 02", quantity: 1, price: 15 },
];

// Load cart items
function loadCart() {
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';

    let totalCost = 0;
    cartItems.forEach(item => {
        totalCost += item.price * item.quantity;
        
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('cart-item');
        
        itemDiv.innerHTML = `
            <span>${item.name} (x${item.quantity})</span>
            <span>$${(item.price * item.quantity).toFixed(2)}</span>
            <button onclick="removeItem(${item.id})">Remove</button>
        `;
        
        cartItemsContainer.appendChild(itemDiv);
    });

    document.getElementById('total-cost').textContent = `$${totalCost.toFixed(2)}`;
}

// Remove item from cart
function removeItem(itemId) {
    cartItems = cartItems.filter(item => item.id !== itemId);
    loadCart();
}

// Function for continuing shopping (redirects to menu page)
function continueShopping() {
    window.location.href = "menu.html";
}

// Place order function
function placeOrder() {
    const pickupTime = document.getElementById('pickup-time').value;
    const instructions = document.getElementById('instructions').value;
    const paymentMethod = document.getElementById('payment-method').value;

    if (!pickupTime || !paymentMethod) {
        alert("Please select a pickup time and payment method.");
        return;
    }

    const orderDetails = {
        items: cartItems,
        pickupTime: pickupTime,
        instructions: instructions,
        paymentMethod: paymentMethod
    };

    console.log("Order Placed:", orderDetails);
    alert("Order placed successfully!");

    // Clear cart
    cartItems = [];
    loadCart();
}

document.addEventListener("DOMContentLoaded", loadCart);
