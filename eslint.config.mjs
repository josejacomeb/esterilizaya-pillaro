import globals from "globals";

export default [
  // JavaScript rules
  {
    files: ["**/*.js"],
    languageOptions: {
      globals: {
        ...globals.browser, // adds setTimeout, window, document, etc.
        Chart: "readonly",  // Chart.js
        L: "readonly",      // Leaflet
        $: "readonly"       // jQuery
      }
    },
    rules: {
      // Allow exported functions used in HTML
      "no-unused-vars": "off",
      // Allow new for side effects (Chart.js instantiation)
      "no-new": "off"
    }
  }

  // Remove JSON linting section - handle separately
];