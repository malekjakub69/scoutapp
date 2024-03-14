import { Unit } from './';

export type UserFull = User & {
    last_login: string;
    login?: string;
    id: number;
    current_unit: Unit;
    active: boolean;
};

export type User = {
    id: number;
    first_name: string;
    last_name: string;
    email: string;
};

export type UserLogin = {
    login: string;
    password: string;
};

export type LoginResponse = {
    access_token: string;
    refresh_token: string;
    item: UserFull;
};

export type Password = {
    current_password: string;
    new_password: string;
    new_password_repeat: string;
};
