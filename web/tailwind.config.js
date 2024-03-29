module.exports = {
    mode: 'jit',
    content: ['./src/**/*.{js,jsx,ts,tsx}'],
    theme: {
        screens: {
            mobile: '320px',
            tablet: '1024px',
            desktop: '1280px'
        },
        extend: {
        },
        colors: {
            'green': {
                '50': '#f6fbea',
                '100': '#ebf5d2',
                '200': '#d7ebab',
                '300': '#bbdd79',
                '400': '#a1cc4f',
                '500': '#82b131',
                '600': '#648d23',
                '700': '#48651d',
                '800': '#40561e',
                '900': '#364a1d',
                '950': '#1b280b',
                DEFAULT: '#48651d'
            },
            'red': {
                '50': '#fdf3f3',
                '100': '#fbe9e8',
                '200': '#f7d4d4',
                '300': '#f1b0b1',
                '400': '#e88488',
                '500': '#db5860',
                '600': '#c83e4d',
                '700': '#a62a3a',
                '800': '#8b2637',
                '900': '#782334',
                '950': '#420f17',
                DEFAULT: '#c83e4d'
            },
            'beige': {
                '50': '#faf6f2',
                '100': '#f2e9dc',
                '200': '#e7d6c1',
                '300': '#d8ba99',
                '400': '#c79970',
                '500': '#bc8053',
                '600': '#ae6d48',
                '700': '#91583d',
                '800': '#754737',
                '900': '#5f3c2f',
                '950': '#331e17',
                DEFAULT: '#f2e9dc'
            },
            'blue': {
                '50': '#f5f7fa',
                '100': '#eaeef4',
                '200': '#cfdbe8',
                '300': '#a6bdd3',
                '400': '#7699ba',
                '500': '#547ca3',
                '600': '#456990',
                '700': '#36506e',
                '800': '#2f455d',
                '900': '#2b3c4f',
                '950': '#1d2734',
                DEFAULT: '#456990'
            },
            'green-black': {
                '50': '#f5f8f6',
                '100': '#ddeae1',
                '200': '#bbd4c3',
                '300': '#91b79f',
                '400': '#6a977d',
                '500': '#507c63',
                '600': '#3e634e',
                '700': '#345140',
                '800': '#2d4237',
                '900': '#28392f',
                '950': '#020303',
                DEFAULT: '#020303'
            },
            white: '#fff',
            black: '#000',
            transparent: {
                DEFAULT: ' #00000000',
                50: '#00000011',
                100: '#00000022',
                200: '#00000033',
                300: '#00000055',
                400: '#00000066',
                500: '#00000088',
                600: '#000000aa',
                700: '#000000cc',
                800: '#000000dd',
                900: '#000000ff'
            },
        },
        fontFamily: {
            body: ['Titillium Web', 'sans-serif']
        }
    }
};
