import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import video from "./f1.mp4";
import { LoginHeader, LoginForm } from "./login/login.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <video className="videoTag" autoPlay loop muted>
          <source src={video} type="video/mp4" />
        </video>
        <div className="login d-flex align-items-center justify-content-center">
          <LoginHeader className="p-2" />
          <LoginForm />
        </div>
      </header>
    </div>
  );
}

export default App;
