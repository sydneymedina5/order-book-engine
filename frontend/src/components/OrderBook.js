// src/components/OrderBook.js

import React, { useEffect, useState } from "react";

function OrderBook() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // Replace this with your real fetch or WebSocket call
    fetch("/api/orders")
      .then((res) => res.json())
      .then((data) => setOrders(data));
  }, []);

  return (
    <div>
      <h2>Order Book</h2>
      <table>
        <thead>
          <tr>
            <th>Price</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order, i) => (
            <tr key={i}>
              <td>{order.price}</td>
              <td>{order.amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default OrderBook;
