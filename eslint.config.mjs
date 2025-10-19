// eslint.config.mjs
import js from "@eslint/js";

export default [
  // Base recommended config
  js.configs.recommended,

  {
    languageOptions: {
      globals: {
        ...globals.browser, // Uso de la aplicación en el navegador
        // Habilita jQuery globals para no tener quejas en el código
        $: "readonly",
        jQuery: "readonly",
        Chart: "readonly",
        L: "readonly",
        setTimeout: "readonly",
      },
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
    },
  },
];
