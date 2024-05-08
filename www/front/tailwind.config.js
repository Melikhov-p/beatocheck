/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue, js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'base': '#090c15',
        'grey-blue': '#314065',
        'light-submarine': '#131728',
        'dark-submarine': '#0c111d',
        'deep-purple': '#333fd1',
        'midnight-purple': '#3541ff',
        'deep-ocean': '#1e258b',
        'ocean-breath': '#57ccfc',
        'deep-galaxy': '#141fff',
        'dark-galaxy': '#333fff',
        'light-galaxy': '#4651f9',
        'sunrise-yellow': '#f4df58',
        'smooth-pink': '#ffe1ff',
        'mate-pink': '#f8abdd',
        'cool-mint': '#51bce8',
        'input-disabled': '#0f1220',
        'input-focus': '#1e2339',
        'input-dark-success': '#0c1d22',
        'input-light-success': '#16323b',
        'dark-success': '#21a48b',
        'light-success': '#3dd598',
        'input-error': '#27101c',
        'light-input-error': '#351526',
        'text-error': '#a01c3a',
        'light-text-error': '#b92143'
      },
      width: {
        'avatar-big': '4rem',
        'avatar-md': '2rem',
        'avatar-sm': '1.5rem',
      },
    },
  },
  plugins: [],
}
