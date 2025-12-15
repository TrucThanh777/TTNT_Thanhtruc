/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        board: '#f7f2ed',
        charcoal: '#1e1e20',
        accent: '#f97316',
        emerald: '#0ea5e9',
      },
      fontFamily: {
        sans: ['"Inter"', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        tile: '0 4px 20px rgba(0,0,0,0.15)',
      },
      keyframes: {
        'pulse-strong': {
          '0%, 100%': { transform: 'scale(1)', opacity: '1' },
          '50%': { transform: 'scale(1.12)', opacity: '0.6' },
        },
        ripple: {
          '0%': { transform: 'scale(0)', opacity: '0.6' },
          '80%': { opacity: '0.2' },
          '100%': { transform: 'scale(2.5)', opacity: '0' },
        },
      },
      animation: {
        'pulse-strong': 'pulse-strong 1.4s ease-in-out infinite',
        ripple: 'ripple 0.8s ease-out forwards',
      },
    },
  },
  plugins: [],
}
