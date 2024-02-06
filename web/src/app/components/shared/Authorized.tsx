import { FC, Fragment } from 'react';
import useAuth from 'src/app/hooks/useAuth';
import { RoleCode } from 'src/types';

type IProps = {
    children?: JSX.Element;
    roles: RoleCode[];
};

export const Authorized: FC<IProps> = ({ roles, children }) => {
    const { user } = useAuth();

    const isAuthorized = (): boolean => {
        if (!user) return false;
        for (const role in roles) {
            if (role == RoleCode[user.role_id]) return true;
        }
        return false;
    };

    return <Fragment>{isAuthorized() && children}</Fragment>;
};
