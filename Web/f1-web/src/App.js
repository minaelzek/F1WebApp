import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import React, { useEffect, useRef } from 'react';
import sound from "./login-sound-engines.mp3"
import { LoginHeader, LoginForm } from "./login/login.js";

function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <AudioPlayer/>
        <video className="videoTag" autoPlay loop muted>
          <source src="https://s3.eu-west-1.amazonaws.com/eu-west-1.vimeo.com/videos/700/879/700879408.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZRUUNWVAWWO32QM7%2F20240103%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240103T030233Z&X-Amz-Expires=86399&X-Amz-SignedHeaders=host&X-Amz-Signature=04ddcd4fbcdbd1e9fd7c7179b39bd0166ca09def90c5a14cb61fc39c3f29016a" type="video/mp4" />
        </video>
        <div className="login d-flex align-items-center justify-content-center">
          <LoginHeader className="p-2" />
          <LoginForm />
        </div>
      </header>
    </div>
  );
}

const AudioPlayer = () => {
  const audioRef = useRef(null);

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.play();
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
