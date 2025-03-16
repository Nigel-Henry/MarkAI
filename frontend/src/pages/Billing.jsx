import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('pk_test_your_stripe_key');

export default function Billing() {
  const handleSubscribe = async (planId) => {
    const stripe = await stripePromise;
    const { error } = await stripe.redirectToCheckout({
      lineItems: [{ price: planId, quantity: 1 }],
      mode: 'subscription',
      successUrl: 'https://your-domain.com/success',
      cancelUrl: 'https://your-domain.com/cancel'
    });
  };

  return (
    <div>
      <button onClick={() => handleSubscribe('price_free')}>Free Plan</button>
      <button onClick={() => handleSubscribe('price_premium')}>Premium Plan ($10/month)</button>
    </div>
  );
}