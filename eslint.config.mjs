// eslint.config.mjs
import js from "@eslint/js";
import globals from "globals";

export default [
  // Base recommended config
  js.configs.recommended,

  {
    languageOptions: {
      globals: {
        // Habilita jQuery globals para no tener quejas en el código
        $: "readonly",
        jQuery: "readonly",
        Chart: "readonly",
        L: "readonly",
        setTimeout: "readonly",
        ...globals.browser, // Uso de la aplicación en el navegador
      },
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
    },
  },
];
