import "../styles/main.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h2>CarRental</h2>
      <div>
        <a href="/vehicles">Cars</a>
        <a href="/bookings">Bookings</a>
        <a href="/" onClick={() => localStorage.clear()}>Logout</a>
      </div>
    </nav>
  );
}
