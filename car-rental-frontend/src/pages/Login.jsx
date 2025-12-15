import { useState } from "react";
import api from "../api/axios";
import "../styles/main.css";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await api.post("auth/login/", form);
    localStorage.setItem("token", res.data.access);
    window.location.href = "/vehicles";
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input placeholder="Username" onChange={(e)=>setForm({...form,username:e.target.value})} />
        <input type="password" placeholder="Password" onChange={(e)=>setForm({...form,password:e.target.value})} />
        <button>Login</button>
      </form>
    </div>
  );
}
