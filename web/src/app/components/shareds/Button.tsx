import clsx from 'clsx';
import { Children, FC, MouseEvent, MouseEventHandler, ReactNode } from 'react';
import { BTN_DARK_VARIANTS, BTN_VARIANTS } from 'src/app/hooks';
import { FormSubmitStatus } from 'src/app/types';
import { IcoCheck, IcoDelete, IcoLoader } from 'src/assets/icons';

interface IProps {
    className?: string;
    mode?: 'light' | 'dark';
    children?: ReactNode | ReactNode[];
    onClick?: MouseEventHandler;
    variant?: 'primary' | 'secondary' | 'delete';
    disabled?: boolean;
    type?: 'button' | 'submit' | 'reset';
    status?: FormSubmitStatus;
    removeState?: () => void;
}

export const Button: FC<IProps> = ({ className, children, onClick, variant = 'primary', disabled, type = 'button', status = 'idle', mode = 'light' }) => {
    const BTN_VARIANT = mode === 'light' ? BTN_VARIANTS : BTN_DARK_VARIANTS;

    const btnStyle = clsx(
        {
            'min-w-[12rem]': true,
            'scout-btn': mode === 'light',
            'scout-btn-dark': mode === 'light'
        },
        status !== 'error' ? BTN_VARIANT[variant] : BTN_VARIANT.delete,
        className
    );

    return (
        <button
            onClick={(e: MouseEvent) => {
                if (onClick) onClick(e);
            }}
            disabled={disabled}
            className={btnStyle}
            type={type}
        >
            <span className={`${status !== 'idle' ? 'invisible' : 'visible'}`}>{Children.map(children, (child) => child)}</span>

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
