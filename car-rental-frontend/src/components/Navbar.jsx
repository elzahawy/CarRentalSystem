import { Link, useNavigate } from "react-router-dom";
import "../styles/main.css";

export default function Navbar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <nav className="navbar">
      <h2>CarRental</h2>
      <div className="nav-links">
        <Link to="/vehicles">Cars</Link>
        <Link to="/bookings">Bookings</Link>
        <button onClick={logout} className="logout-btn">Logout</button>
      </div>
    </nav>
  );
}
