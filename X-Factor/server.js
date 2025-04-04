const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

// Serve static files from "public" folder
app.use(express.static("public"));

// Serve index.html on root URL "/"
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start the server
app.listen(port, async () => {
  console.log(`Server running at http://localhost:${port}`);
  
  // Import 'open' dynamically
  const open = (await import("open")).default;
  open(`http://localhost:${port}`);
});
