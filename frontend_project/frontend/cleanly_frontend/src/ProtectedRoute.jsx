import React from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";

export default function ProtectedRoute({ children }) {
  const [isAuthenticated, setIsAuthenticated] = React.useState(null);

  React.useEffect(() => {
    const checkAuth = async () => {
      try {
        await axios.get("http://localhost:8000/api/v1/login/", {
          withCredentials: true, // セッションCookieを利用
        });
        setIsAuthenticated(true);
      } catch {
        setIsAuthenticated(false);
      }
    };
    checkAuth();
  }, []);

  if (isAuthenticated === null) {
    return <p>認証確認中...</p>;
  }

  return isAuthenticated ? children : <Navigate to="/" />;
}