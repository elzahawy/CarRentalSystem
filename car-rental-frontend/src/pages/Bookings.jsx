import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Bookings() {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    api.get("bookings/").then(res => setBookings(res.data));
  }, []);

  return (
    <div className="container">
      <h1>My Bookings</h1>
      {bookings.map(b => (
        <div key={b.id} className="card">
          <h3>{b.vehicle_name}</h3>
          <p>Total: ${b.total_price}</p>
          <p>Status: {b.status}</p>
        </div>
      ))}
    </div>
  );
}
