import { useState } from "react";
import axios from "axios";

function SeaShipmentForm() {
  const [form, setForm] = useState({
    cliente_id: "",
    producto_id: "",
    cantidad: "",
    fecha_registro: "",
    fecha_entrega: "",
    bodega_id: "",
    precio_envio: "",
    numero_flota: "",
    numero_guia: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:8000/envios-maritimos", form, {
        headers: { Authorization: "Bearer secret123" },
      });
      alert("Envío creado");
    } catch (error) {
      alert("Error");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Crear Envío Marítimo</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(form).map((key) => (
          <div key={key}>
            <input
              type="text"
              name={key}
              placeholder={key}
              value={form[key]}
              onChange={handleChange}
            />
          </div>
        ))}
        <button type="submit">Crear</button>
      </form>
    </div>
  );
}

export default SeaShipmentForm;
