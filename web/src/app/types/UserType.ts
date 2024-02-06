export type UserFull = User & {
    last_login: string;
    language?: Language;
    last_visited_chat?: string;
    unread_messages: number;
    workplace_id: number;
    role_id: number;
    language_id?: number;
    is_active: boolean;
    available_workplaces_ids?: number[];
    login?: string;
    password?: string;
    registration_date: string;
    state: boolean;
};

export type Language = {
    code: string;
    title: string;
};

export type UserUpdate = {
    first_name: string;
    surname: string;
    login: string;
    password: string;
    password2: string;
};

export type User = {
    id: number;
    first_name: string;
    surname: string;
    email: string;
};

export enum RoleCode {
    operator = 7,
    filler = 6,
    packer = 5,
    warehouseman = 4,
    admin = 3,
    logistics = 2,
    manipulator = 1,
    noCheck = 0
}

export type UserLogin = {
    login: string;
    password: string;
};

export type LoginResponse = {
    access_token: string;
    refresh_token: string;
    items: UserFull[];
};

export type Password = {
    current_password: string;
    new_password: string;
    new_password_repeat: string;
};
