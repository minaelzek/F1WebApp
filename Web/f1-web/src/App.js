import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
import video from "./f1.mp4";
import LoginForm from "./login/login.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <video className="videoTag" autoPlay loop muted>
          <source src={video} type="video/mp4" />
        </video>
        <LoginForm />
      </header>
    </div>
  );
}

export default App;
