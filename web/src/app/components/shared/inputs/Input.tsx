import { forwardRef } from 'react';
import { twMerge as tw } from 'tailwind-merge';

type InputProps = JSX.IntrinsicElements['input'] & {
    label?: string;
    dirty?: boolean;
    error?: string;
    innerClassName?: string;
    labelClassName?: string;
    theme?: 'dark' | 'light';
};

const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
    const { label, className, required, innerClassName, labelClassName, dirty, error, theme = 'dark', ...inputProps } = props;

    return (
        <div className={tw(className, 'relative')}>
            <label htmlFor={`scoutInput-${inputProps.name}`} >
                {label || ''}
            </label>

            <input
                {...inputProps}
                id={`scoutInput-${inputProps.name}`}
                autoComplete="off"
                ref={ref}
                className={"border-[1px] rounded-lg p-2"}
                required={required}
            />

            <div className="text-error-500 bottom-1 pt-1 absolute translate-y-full">{error ? error : ''}</div>
        </div>
    );
});

Input.displayName = 'Input';

export default Input;
