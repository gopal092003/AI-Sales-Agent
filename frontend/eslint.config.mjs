import js from "@eslint/js";
import nextPlugin from "@next/eslint-plugin-next";
import tseslint from "typescript-eslint";

export default tseslint.config(
  {
    ignores: [
      ".next/**",
      "node_modules/**",
      "dist/**",
      "build/**",
    ],
  },

  js.configs.recommended,

  ...tseslint.configs.recommended,

  {
    files: ["**/*.{ts,tsx}"],

    languageOptions: {
      parserOptions: {
        project: "./tsconfig.json",
      },
    },

    plugins: {
      "@next/next": nextPlugin,
    },

    rules: {
      ...nextPlugin.configs.recommended.rules,
      ...nextPlugin.configs["core-web-vitals"]
        .rules,

      "@typescript-eslint/no-unused-vars": [
        "warn",
        {
          argsIgnorePattern: "^_",
        },
      ],

      "@typescript-eslint/no-explicit-any":
        "off",

      "no-console": [
        "warn",
        {
          allow: ["warn", "error"],
        },
      ],
    },
  }
);