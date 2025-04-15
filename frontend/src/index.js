// Import required React modules and components
import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";  // Import global styles

// Get the root DOM element
const container = document.getElementById("root");
// Create a root for the React application
const root = createRoot(container);

// Render the App component in StrictMode for development
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
