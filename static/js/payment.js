const paymentBtn = document.querySelector("#payment-btn");

// Request for key
console.log("Requesting key...");

fetch("/payment/config/")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    // listener for payment button click event
    document.querySelector("#payment-btn").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("/payment/create-checkout-session/")
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          return stripe.redirectToCheckout({ sessionId: data.sessionId });
        })
        .then((res) => {
          console.log(res);
        });
    });
  });
