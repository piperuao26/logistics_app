import { useEffect, useState } from "react";
import axios from "axios";

function LandShipmentList() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/envios-terrestres", {
        headers: { Authorization: "Bearer secret123" },
      })
      .then((res) => setData(res.data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>Envíos Terrestres</h2>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            Guía: {item.numero_guia} | Precio Final: {item.precio_final}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default LandShipmentList;
