import React, { useEffect, useState } from "react";
import Draggable from "react-draggable";

const API_BASE = "http://localhost:8000/api/v1";

function Editor({ pdfId }) {
  const [page, setPage] = useState(null);
  const [texts, setTexts] = useState([]);

  // 🔹 STEP 4.1 — pages API call
useEffect(() => {
  async function loadPages() {
    try {
      const res = await fetch(
        `http://localhost:8000/api/v1/pdf/${pdfId}/pages`
      );

      if (!res.ok) {
        throw new Error("API error");
      }

      const data = await res.json();
      const p = data.pages[0];
      setPage(p);

      setTexts(
        p.texts.map(t => ({
          text: t.text,
          x: t.bbox.x,
          y: t.bbox.y + 15,
          font_size: t.font_size
        }))
      );
    } catch (err) {
      console.error("FETCH ERROR:", err);
      alert("Backend connected, but frontend fetch blocked. Check image/static.");
    }
  }

  loadPages();
}, [pdfId]);


  // 🔹 text update
  const updateText = (index, value) => {
    const copy = [...texts];
    copy[index].text = value;
    setTexts(copy);
  };

  // 🔹 position update
  const updatePosition = (index, x, y) => {
    const copy = [...texts];
    copy[index].x = x;
    copy[index].y = y;
    setTexts(copy);
  };

  // 🔹 export API call
  const exportPdf = () => {
    const edits = texts.map(t => ({
      page_number: 1,
      text: t.text,
      x: t.x,
      y: t.y,
      font_size: t.font_size
    }));

    fetch(`${API_BASE}/pdf/${pdfId}/export`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ edits })
    })
      .then(res => res.json())
      .then(data => {
        alert("PDF Exported!\n" + data.output_pdf);
      });
  };

  if (!page) return <p>Loading...</p>;

  return (
    <div>
      {/* PAGE */}
      <div
        style={{
          position: "relative",
          width: page.width,
          border: "1px solid #ccc",
          margin: "auto"
        }}
      >
       <img
        src={`http://localhost:8000/static/pages/${pdfId}/page_1.png`}
        alt="PDF Page"
        style={{ width: "100%" }}
/>


        {/* TEXT BOXES */}
        {texts.map((t, i) => (
          <Draggable
            key={i}
            position={{ x: t.x, y: t.y }}
            onStop={(e, d) => updatePosition(i, d.x, d.y)}
          >
            <input
              value={t.text}
              onChange={(e) => updateText(i, e.target.value)}
              style={{
                position: "absolute",
                fontSize: t.font_size,
                border: "1px dashed gray",
                background: "rgba(255,255,255,0.8)",
                padding: "2px"
              }}
            />
          </Draggable>
        ))}
      </div>

      {/* EXPORT BUTTON */}
      <div style={{ textAlign: "center", marginTop: 20 }}>
        <button onClick={exportPdf}>Export PDF</button>
      </div>
    </div>
  );
}

export default Editor;
