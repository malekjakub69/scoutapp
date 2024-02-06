import React, { FC } from 'react';
import { IcoLoader } from '../../../assets/icons';

interface IProps {
    children?: JSX.Element | JSX.Element[];
    loading: boolean;
}

export const Loading: FC<IProps> = ({ children, loading }) => {
    if (loading) return <IcoLoader className={'m-auto animate-spin w-10 fill-gray-500'} />;
    return <>{children}</>;
};
