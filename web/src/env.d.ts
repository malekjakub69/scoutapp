export {};

interface ImportMetaEnv {
    readonly VITE_BE_URL: string;
    readonly VITE_FE_URL: string;
    readonly VITE_BE_VERSION: string;
    readonly VITE_ENV_TITLE: string;
    readonly VITE_ENV: 'DEV' | 'PROD' | 'DEMO';
    readonly VITE_APP_VERSION: string;
    readonly VITE_FE_BASENAME_PREFIX: string | undefined;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}
