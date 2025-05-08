// // Get references to DOM elements
// const quantityInput = document.getElementById("quantity");
// const itemPrice = document.getElementById("item-price");
// const itemTotal = document.getElementById("item-total");
// const totalPrice = document.getElementById("total-price");

// const unitPrice = 25.00; // The price of one unit of the product

// // Function to update the quantity and total price
// function updateQuantity(change) {
//     let currentQuantity = parseInt(quantityInput.value);
//     currentQuantity += change;

//     // Prevent the quantity from going below 1
//     if (currentQuantity < 1) return;

//     // Update the quantity display
//     quantityInput.value = currentQuantity;

//     // Calculate the new total price for this item
//     const newTotal = (unitPrice * currentQuantity).toFixed(2);
//     itemTotal.textContent = `$${newTotal}`;

//     // Update the overall total price (you can add more items to this logic)
//     updateOverallTotal();
// }

// // Function to update the total price of all items
// function updateOverallTotal() {
//     const currentQuantity = parseInt(quantityInput.value);
//     const newTotal = (unitPrice * currentQuantity).toFixed(2);
//     totalPrice.textContent = `$${newTotal}`;
// }






// Assuming you want to update the quantity and price for a specific item
function updateQuantity(itemId, change) {
    const quantityInput = document.getElementById(`quantity-${itemId}`);
    const itemPriceElement = document.getElementById(`item-price-${itemId}`);
    const itemTotalElement = document.getElementById(`item-total-${itemId}`);

    let currentQuantity = parseInt(quantityInput.value);
    currentQuantity += change;

    // Prevent the quantity from going below 1
    if (currentQuantity < 1) return;

    // Update the quantity value
    quantityInput.value = currentQuantity;

    // Get the price per unit
    const unitPrice = parseFloat(itemPriceElement.innerText.replace('RS.', ''));

    // Calculate and update the total price for this item
    const newTotal = (unitPrice * currentQuantity).toFixed(2);
    itemTotalElement.innerText = `Rs ${newTotal}`;

    // Optionally, update the overall cart total
    updateCartTotal();
}

// Update the overall cart total
function updateCartTotal() {
    let total = 0;

    // Loop through all the cart items to sum the totals
    document.querySelectorAll('.cart-item').forEach(function(item) {
        const itemTotalElement = item.querySelector('.item-total');
        const itemTotal = parseFloat(itemTotalElement.innerText.replace('Rs ', ''));
        total += itemTotal;
    });

    // Update the cart's total price
    document.getElementById('total-price').innerText = `Rs ${total.toFixed(2)}`;
}
