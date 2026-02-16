import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import LandShipmentForm from "./pages/LandShipmentForm";
import SeaShipmentForm from "./pages/SeaShipmentForm";
import LandShipmentList from "./pages/LandShipmentList";
import SeaShipmentList from "./pages/SeaShipmentList";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/terrestre" element={<LandShipmentForm />} />
        <Route path="/maritimo" element={<SeaShipmentForm />} />
        <Route path="/terrestres" element={<LandShipmentList />} />
        <Route path="/maritimos" element={<SeaShipmentList />} />
      </Routes>
    </Router>
  );
}

export default App;
