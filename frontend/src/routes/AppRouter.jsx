import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Home from "../pages/home/Home";
import Login from "../pages/login/Login";
// import Dashboard from '../components/Dashboard';

const AppRouter = ({ token }) => {
  return (
    <Router>
      <Routes>
        <Route
          path="/login"
          element={token ? <Navigate to="/dashboard" /> : <Login />}
        />
        <Route
          path="/dashboard"
          element={token ? <Home /> : <Navigate to="/login" />}
        />
        <Route path="/logout">
          {/* Implement your logout logic here */}
          {() => {
            // Implement your logout logic here, and navigate to the login page

            return <Navigate to="/login" />;
          }}
        </Route>
        <Route path="/*" element={<Navigate to="/login" />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;
