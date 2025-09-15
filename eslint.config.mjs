// eslint.config.mjs
import js from "@eslint/js";

export default [
  // Base recommended config
  js.configs.recommended,

  {
    languageOptions: {
      globals: {
        // Enable jQuery globals so ESLint doesn’t complain
        $: "readonly",
        jQuery: "readonly",
        Chart: "readonly",
        L: "readonly",
        setTimeout: "readonly"
      },
    },
    rules: {
      // Example overrides (adjust as needed)
      "no-unused-vars": "warn",
      "no-console": "off",
    },
  },
];