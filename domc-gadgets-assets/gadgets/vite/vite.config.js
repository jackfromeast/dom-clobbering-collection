import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    format: "cjs",
    assetsInlineLimit: 0,
    rollupOptions: {
      output: {
        format: "cjs"
      },
    },
  },
  base: "./",
});