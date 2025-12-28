import React from "react";
import Editor from "./Editor";

function App() {
  // ⚠️ yahan apna pdf_id paste karo
  const pdfId = "30f37fca-8f89-4dd6-8814-e9ee44acd999";

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>PDF Editor</h2>
      <Editor pdfId={pdfId} />
    </div>
  );
}

export default App;
