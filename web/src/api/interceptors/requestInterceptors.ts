import { AxiosRequestConfig } from 'axios';

const IGNORED_URLS = ['reset-password', 'logout/refresh', 'logout/access', 'login', 'token/refresh', 'login-info'];

const isEndpointStrict = (config: AxiosRequestConfig, endpoint: string) => config?.url && config.url.endsWith(endpoint);

const attachToken = (config: AxiosRequestConfig) => {
    const token = localStorage.getItem('access_token');

    if (!token) return config;
    if (config.url?.includes('s3.eu-west-2.amazonaws.com')) return config;
    if (IGNORED_URLS.some((url) => isEndpointStrict(config, url))) return config;

    if (!config.headers) config.headers = {};
    config.headers.Authorization = 'Bearer ' + token;

    return config;
};

export default attachToken;
