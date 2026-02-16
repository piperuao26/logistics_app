import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div style={{ padding: 10, background: "#eee" }}>
      <Link to="/">Inicio</Link> |{" "}
      <Link to="/terrestre">Crear Terrestre</Link> |{" "}
      <Link to="/terrestres">Ver Terrestres</Link> |{" "}
      <Link to="/maritimo">Crear Marítimo</Link> |{" "}
      <Link to="/maritimos">Ver Marítimos</Link>
    </div>
  );
}

export default Navbar;
