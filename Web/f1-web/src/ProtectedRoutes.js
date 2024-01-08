// ProtectedRoute.js

import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import Cookies from 'js-cookie';

const ProtectedRoute = () => {
  const sessionId = Cookies.get('sessionid');
  const csrfToken = Cookies.get('csrftoken');

  return (sessionId && csrfToken) ? <Outlet/> : <Navigate to="/" />;
};

export default ProtectedRoute;
