import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { BaseApiGetType, BaseApiType, IApiParameters } from '../app/types';
import interceptors from './interceptors';

const BASE_URL = `${import.meta.env.VITE_BE_URL}/${import.meta.env.VITE_BE_VERSION}`;
const PAGE_LIMIT = 20;

const axiosInstance = axios.create({
    baseURL: BASE_URL
});

axiosInstance.interceptors.request.use(interceptors.requestAttachToken, (error) => error);
axiosInstance.interceptors.response.use((response) => response, interceptors.responseTokenRevalidation);

function buildParamsUrl(path: string, params: IApiParameters) {
    const paramsList: string[] = [];
    if (params.filter) paramsList.push('filter=' + params.filter);
    if (params.sort) paramsList.push('sort=' + params.sort);
    if (params.limit) paramsList.push('limit=' + params.limit);
    if (params.page) {
        paramsList.push('page=' + params.page);
        if (!params.limit) paramsList.push('limit=' + PAGE_LIMIT);
    }
    return paramsList.length > 0 ? path + '?' + paramsList.join('&') : path;
}

export async function getBase<T>(path: string, params: IApiParameters = {}): Promise<BaseApiGetType<T>> {
    const resp = await axiosInstance.get(buildParamsUrl(path, params));
    return resp.data;
}

export async function deleteBase<T>(path: string): Promise<BaseApiType<T>> {
    const resp = await axiosInstance.delete(path);
    return resp.data;
}

export async function postSingle<T>(path: string, requestData: unknown): Promise<BaseApiType<T>> {
    const resp = await axiosInstance.post(path, requestData);
    return resp.data;
}

export async function post<T>(path: string, requestData?: unknown): Promise<BaseApiType<T>> {
    const resp = await axiosInstance.post(path, requestData);
    return resp.data;
}

export async function postBase<T>(path: string, requestData?: unknown, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return axiosInstance.post<T>(path, requestData, config);
}

export async function put<T>(path: string, requestData: unknown): Promise<BaseApiType<T>> {
    const resp = await axiosInstance.put(path, requestData);
    return resp.data;
}
