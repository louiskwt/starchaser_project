// Request for key
console.log("Requesting key...");

fetch("/payment/config/")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
  });
