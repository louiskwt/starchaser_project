/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.{html,js}"],
  theme: {
    extend: {
      keyframes: {
        "fade-in-down": {
          "0%": {
            opacity: "0",
            transform: "translateY(-20px)",
          },
          "100%": {
            opacity: "1",
            transform: "translateY(0)",
          },
        },
        "fade-in-right": {
          "0%": {
            opacity: "0",
            transform: "translateX(50px)",
          },
          "100%": {
            opacity: "1",
            transform: "translateX(0)",
          },
        },
        "press-down": {
          "0%": {
            "box-shadow": "black, 7px 7px 0",
          },
          "100%": {
            "box-shadow": "black, 2px 2px 0",
          },
        },
      },
      animation: {
        "fade-in-down": "fade-in-down 1.5s ease-out",
        "fade-in-right": "fade-in-right 1.0s ease-out",
        "press-down": "press-down 0.5s ease-out",
      },
    },
  },
  variants: {},
  plugins: [],
};
