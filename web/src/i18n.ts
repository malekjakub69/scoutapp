import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

export default i18n.use(initReactI18next).init({
    fallbackLng: 'en',
    debug: true,
    interpolation: {
        escapeValue: false
    }
});
