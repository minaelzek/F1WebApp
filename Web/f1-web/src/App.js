import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect, useRef } from "react";
import sound from "./login-sound-engines.mp3";
import { LoginHeader, LoginForm } from "./login/login.js";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route>
            <Route exact path ="/" element={<LoginPage/>}/>
            <Route exact path ="/register" element={<RegisterPage/>}/>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

const LoginPage = () => {
  return (
    <div className="login-wrapper">
      <video className="videoTag" autoPlay loop muted>
        <source
          src="https://s3.eu-west-1.amazonaws.com/eu-west-1.vimeo.com/videos/700/879/700879408.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZRUUNWVAWWO32QM7%2F20240103%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240103T030233Z&X-Amz-Expires=86399&X-Amz-SignedHeaders=host&X-Amz-Signature=04ddcd4fbcdbd1e9fd7c7179b39bd0166ca09def90c5a14cb61fc39c3f29016a"
          type="video/mp4"
        />
      </video>
      <div className="login d-flex align-items-center justify-content-center">
        <LoginHeader className="p-2" />
        <LoginForm />
      </div>
      <AudioPlayer />
    </div>
  );
};


const RegisterPage = () => {
  return (
    <div className="login-wrapper">
      <h2>Register Page</h2>
      {/* Add your register form or content here */}
    </div>
  );
};

const AudioPlayer = () => {
  const audioRef = useRef(null);

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = 0.1;
      audioRef.current.play().catch((error) => {
        console.error("Autoplay prevented:", error);
      });
    }
  }, []);

  return (
    <div>
      <audio ref={audioRef} autoPlay>
        <source src={sound} type="audio/mp3" />
      </audio>
    </div>
  );
};

export default App;
