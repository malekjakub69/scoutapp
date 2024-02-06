export interface BaseApiType<T> {
    items: T[];
    message: string;
    updated?: T[];
}

export interface BaseApiAuthType<T> {
    items: T;
    message: string;
}

export interface BaseApiGetType<T> extends BaseApiType<T> {
    page: number;
    total: number;
    prev_num: number | null;
    next_num: number | null;
    pages: number;
    has_next: boolean;
}

export interface BaseType {
    id: number;
    created_on: string;
    updated_on: string;
}

export interface IApiParameters {
    filter?: string;
    sort?: string;
    page?: number;
    limit?: number;
}
