import { BaseApiType, LoginResponse, Password, UserFull, UserLogin, UserUpdate } from '../app/types';
import { BaseApi } from './index';

export async function authenticate(): Promise<UserFull> {
    const resp = await BaseApi.postBase<UserFull[]>('/authenticate');
    return resp.data[0];
}

export async function logout(): Promise<{ message: string }> {
    const tokenAccess = localStorage.getItem('access_token');
    const requestAccessConfig = { headers: { Authorization: `Bearer ${tokenAccess}` } };

    await BaseApi.postBase<{ message: string }>('/logout/access', {}, requestAccessConfig);

    const tokenRefresh = localStorage.getItem('refresh_token');
    const requestRefreshConfig = { headers: { Authorization: `Bearer ${tokenRefresh}` } };

    const { data } = await BaseApi.postBase<{ message: string }>('/logout/refresh', {}, requestRefreshConfig);
    return data;
}

export async function logIn(login: UserLogin): Promise<LoginResponse> {
    const resp = await BaseApi.postBase<LoginResponse>('/login', login);
    return resp.data;
}

export async function refreshAccessToken(): Promise<{ token: string }> {
    const tokenRefresh = localStorage.getItem('refresh_token');
    const requestConfig = { headers: { Authorization: `Bearer ${tokenRefresh}` } };

    const resp = await BaseApi.postBase<{ access_token: string }>('/token/refresh', {}, requestConfig);
    return { token: resp.data.access_token };
}

export async function updateUser(user: UserUpdate): Promise<BaseApiType<UserFull>> {
    const response = await BaseApi.put<UserFull>('/users/profile', user);
    return response;
}

export async function updatePassword(password: Password): Promise<BaseApiType<UserFull>> {
    const response = await BaseApi.put<UserFull>('/users/change-password', password);
    return response;
}
