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
            "scout-logo": {
                DEFAULT: '#1A1A1A',
                blue1: '#294885',
                blue2: '#255C9E',
                blue3: '#336CAA',
                blue4: '#3979B5',
                yellow1: '#FCC11E',
                yellow2: '#F9B200',
                yellow3: '#F49E00',
            },
            error: {
                DEFAULT: '#9F2A2A',
                50: '#EEC0C0',
                100: '#E9ACAC',
                200: '#DE8484',
                300: '#D45B5B',
                400: '#C73535',
                500: '#9F2A2A',
                600: '#832323',
                700: '#661B1B',
                800: '#4A1414',
                900: '#2E0C0C'
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
