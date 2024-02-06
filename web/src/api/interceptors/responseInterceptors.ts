import axios, { AxiosError, AxiosRequestConfig } from 'axios';
import { queryClient } from 'src/app/App';
import queryKeys from 'src/app/hooks/queryKeys';
import { AuthApi } from '..';

let accessTokenRefreshCall: Promise<{ token: string }> | undefined = undefined;

const isUnauthorizedError = (error: AxiosError) => error?.response?.status === 401;

const isEndpointStrict = (config: AxiosRequestConfig, endpoint: string) => config?.url && config.url.endsWith(endpoint);

const invalidateAuthState = () => {
    queryClient.setQueryData(queryKeys.AUTH_KEY, () => null);
};

const revalidateAccessToken = async (error: AxiosError): Promise<AxiosError | undefined> => {
    const originalConfig = error.config;

    if (!error?.response || error.response.status !== 401) throw error;
    if (isEndpointStrict(originalConfig, '/login')) throw error;
    if (isEndpointStrict(originalConfig, '/token/refresh')) invalidateAuthState();

    try {
        if (!accessTokenRefreshCall) accessTokenRefreshCall = AuthApi.refreshAccessToken();

        const { token: newAccessToken } = await accessTokenRefreshCall;
        localStorage.setItem('access_token', newAccessToken);

        if (originalConfig.headers) {
            originalConfig.headers.Authorization = `Bearer ${newAccessToken}`;
        }

        try {
            return await axios.request(originalConfig);
        } catch (innerError) {
            if (isUnauthorizedError(innerError as AxiosError)) throw innerError;
        }
    } catch (innerError) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        invalidateAuthState();
    } finally {
        accessTokenRefreshCall = undefined;
    }
};

export default revalidateAccessToken;
