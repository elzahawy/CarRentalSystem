import { useEffect, useState } from "react";
import api from "../api/axios";
import "../styles/main.css";

export default function Vehicles() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    api.get("vehicles/").then(res => setCars(res.data));
  }, []);

  return (
    <div className="container">
      <h1>Available Cars</h1>
      <div className="grid">
        {cars.map(car => (
          <div key={car.id} className="card">
            <h3>{car.name}</h3>
            <p>{car.year}</p>
            <p>${car.price_per_day}/day</p>
            <button>Book Now</button>
          </div>
        ))}
      </div>
    </div>
  );
}
