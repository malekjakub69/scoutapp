import { clsx } from 'clsx';
import { forwardRef } from 'react';
import { twMerge as tw } from 'tailwind-merge';

type InputProps = JSX.IntrinsicElements['input'] & {
    label?: string;
    dirty?: boolean;
    error?: string;
    innerClassName?: string;
    labelClassName?: string;
};

const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
    const { label, className, required, innerClassName, labelClassName, dirty, error, ...inputProps } = props;

    const labeltClassNames = clsx(
        {
            'block text-white mb-0': true,
            "after:content-['*'] after:ml-1": required
        },
        labelClassName
    );

    const inputClassNames = clsx(
        {
            'w-full border-b-[1px] text-black bg-white rounded-lg p-2 text-xl': true,
            'focus:outline-none focus:border-b-carrot-orange': true,
            'disabled:bg-mid-gray-400 disabled:cursor-not-allowed disabled:text-mid-gray-700': true,
            'border-b-[#77cbcb]': dirty,
            'border-error': error
        },
        innerClassName
    );

    return (
        <div className={tw('relative mb-6', className)}>
            <label htmlFor={`kanbanInput-${inputProps.name}`} className={labeltClassNames}>
                {label || ''}
            </label>

            <input
                {...inputProps}
                id={`kanbanInput-${inputProps.name}`}
                data-testid={`kanban-input--${inputProps.name}`}
                className={inputClassNames}
                autoComplete="off"
                ref={ref}
            />

            <div className="text-error-500 bottom-0 pt-1 absolute translate-y-full">{error ? error : ''}</div>
        </div>
    );
});

Input.displayName = 'Input';

export default Input;
