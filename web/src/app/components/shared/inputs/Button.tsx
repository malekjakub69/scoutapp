import { FC, MouseEvent, MouseEventHandler, ReactNode } from 'react';
import { FormSubmitStatus } from 'src/app/types';
import { IcoCheck, IcoDelete, IcoLoader } from 'src/assets/icons';

interface IProps {
    onClick?: MouseEventHandler;
    disabled?: boolean;
    type?: 'button' | 'submit' | 'reset';
    status?: FormSubmitStatus;
    children?: ReactNode ;
}

export const Button: FC<IProps> = ({ onClick, disabled, type = 'button', status, children }) => {
    return (
        <button
            onClick={(e: MouseEvent) => {
                if (onClick) onClick(e);
            }}
            disabled={disabled}
            type={type}
            className='border-2 rounded-lg'
        >
            {children}

            {/* Success */}
            <span className={`absolute h-1/2 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 ${status === 'success' ? 'visible' : 'invisible'}`}>
                <IcoCheck className={'h-full fill-white'} />
            </span>

            {/* Error */}
            <span className={`absolute h-2/5 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 ${status === 'error' ? 'visible' : 'invisible'}`}>
                <IcoDelete className={'h-full fill-white'} />
            </span>

            {/* Loader */}
            <span className={`absolute h-1/2 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 ${status === 'loading' ? 'visible' : 'invisible'}`}>
                <IcoLoader className={'h-full animate-spin fill-white'} />
            </span>
        </button>
    );
};
