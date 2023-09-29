import React, { createContext, useContext, useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check local storage for a user session
    const storedUser = localStorage.getItem("token");
    if (storedUser) {
      setToken(storedUser);
    }
  }, []);

  const login = async (username, password) => {
    try {
      // Replace with your actual login API endpoint
      const response = await axios.post("http://127.0.0.1:8000/login/", {
        username,
        password,
      });
      alert("Login success");
      const token = response.data.token;
      setUser(response.data.user);
      setIsAuthenticated(true);
      setToken(response.data.token)
      localStorage.setItem("user", response.data.user)
      localStorage.setItem("token", response.data.token)
    } catch (error) {
      alert("Login failed:", error);
    }
  };

  const logout =async () => {
    const response = await axios.post("http://127.0.0.1:8000/logout/", {
        username,
        password,
      });
    setUser(null);
    localStorage.removeItem("user")
    localStorage.removeItem("token")
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
