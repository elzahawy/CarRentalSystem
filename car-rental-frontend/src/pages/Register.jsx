import { useState } from "react";
import api from "../api/axios";
import "../styles/main.css";

export default function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("auth/register/", form);
    window.location.href = "/";
  };

  return (
    <div className="auth-container">
      <h2>Create Account</h2>
      <form onSubmit={handleSubmit}>
        <input placeholder="Username" onChange={(e)=>setForm({...form,username:e.target.value})} />
        <input placeholder="Email" onChange={(e)=>setForm({...form,email:e.target.value})} />
        <input type="password" placeholder="Password" onChange={(e)=>setForm({...form,password:e.target.value})} />
        <button>Register</button>
      </form>
    </div>
  );
}
