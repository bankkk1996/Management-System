import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('1234567q+');
  const navigate = useNavigate()

  useEffect(()=>{
    if (localStorage.getItem("token")!==null){
      navigate("/")
    }

  },[])

  const handleLogin = async () => {
    try {
      // Replace with your API endpoint for authentication
      const response = await axios.post('http://127.0.0.1:8000/login/', { username, password });
      if (response.status === 200) {
        // Assuming the response contains a token upon successful login
        const token = response.data.token;
        const user = response.data.user;
        localStorage.setItem("token", token)
        localStorage.setItem("user", user)
        // onLogin(token);
        navigate("/")
      }
    } catch (error) {
      console.log('Login failed:', error);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
