import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Routes, Route, Navigate } from "react-router-dom";
import React, { Fragment, useEffect, useRef } from "react";
import sound from "./login-sound-engines.mp3";
import { LoginHeader, LoginForm } from "./login/login.js";
import RegisterPage from "./login/register.js";
import { HomePage } from "./user-home/home.js";
import ProtectedRoutes from "./ProtectedRoutes.js";
import TopNavigation from "./user-home/nav.js";

function App() {
  return (
    <div className="App">
      <TopNavigation />
      <Routes>
        <Route>
          <Route exact path="/" element={<LoginPage />} />
          <Route
            exact
            path="/register"
            element={
              <div className="login-wrapper">
                <Video />
                <RegisterPage />
              </div>
            }
          />
          <Route element={<ProtectedRoutes />}>
            <Route exact path="/home" element={<HomePage />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </div>
  );
}

const LoginPage = () => {
  return (
    <div className="login-wrapper">
      <Video />
      <div className="login align-items-center justify-content-center">
        <LoginHeader />
        <div className="mt-5">
          <LoginForm />
        </div>
      </div>
      {/* <AudioPlayer /> */}
    </div>
  );
};

const Video = () => {
  return (
    <video className="videoTag" autoPlay loop muted>
      <source
        src="https://s3.eu-west-1.amazonaws.com/eu-west-1.vimeo.com/videos/700/879/700879408.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZRUUNWVAWWO32QM7%2F20240103%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240103T030233Z&X-Amz-Expires=86399&X-Amz-SignedHeaders=host&X-Amz-Signature=04ddcd4fbcdbd1e9fd7c7179b39bd0166ca09def90c5a14cb61fc39c3f29016a"
        type="video/mp4"
      />
    </video>
  );
};

const AudioPlayer = () => {
  const audioRef = useRef(null);

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = 0.025;
      audioRef.current.play().catch((error) => {
        console.error("Autoplay prevented:", error);
      });
    }
  }, []);

  return (
    <div>
      <audio ref={audioRef}>
        <source src={sound} type="audio/mp3" />
      </audio>
    </div>
  );
};

export default App;
