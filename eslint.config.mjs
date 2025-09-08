// @ts-check

// Import the recommended ESLint configuration from @eslint/js.
import js from "@eslint/js";

// Import the globals object to easily manage global variables.
import globals from "globals";

// Import the defineConfig helper for a better configuration experience.
import { defineConfig } from "eslint/config";

/**
 * The new "flat config" for ESLint is an array of configuration objects.
 * Each object can define its own rules, files to apply to, and settings.
 *
 * This configuration file sets up:
 * 1. The recommended set of ESLint rules.
 * 2. Support for browser-based JavaScript.
 * 3. Correct handling of jQuery's global variables ($ and jQuery).
 */
export default defineConfig([
  // This object applies the recommended ESLint rules to all JavaScript files.
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: {
      // Use the 'browser' globals preset and add jQuery's globals.
      // This ensures that $ and jQuery are recognized as valid global variables.
      globals: {
        ...globals.browser,
        ...globals.jquery,
      },
    },
  },

  // This object specifically sets the source type to 'commonjs' for .js files.
  // Note: This rule may not be necessary if your project is configured as a module.
  { files: ["**/*.js"], languageOptions: { sourceType: "commonjs" } },
]);
