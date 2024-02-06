import { clsx } from 'clsx';
import { DateTime } from 'luxon';
import { FC } from 'react';
import { UseControllerProps, useController } from 'react-hook-form';
import { twMerge as tw } from 'tailwind-merge';

type InputProps = JSX.IntrinsicElements['input'] & {
    label?: string;
    dirty?: boolean;
    error?: string;
    innerClassName?: string;
    labelClassName?: string;
    theme?: 'dark' | 'light';
};

const roundMinutes = (timeValue: DateTime) => {
    if (DateTime.now().plus({ minutes: 30 }) > timeValue) return DateTime.now().plus({ minutes: 30 });
    const roundedMinutes = Math.round(timeValue.minute / 30) * 30;
    return timeValue.set({ minute: roundedMinutes, second: 0, millisecond: 0 });
};

export const DateTimePick: FC<InputProps & UseControllerProps<any>> = ({
    theme,
    label,
    labelClassName,
    className,
    innerClassName,
    disabled,
    required,
    dirty,
    error,
    ...props
}) => {
    const {
        field: { value, onChange, name }
    } = useController(props);

    const handleMinus = () => {
        onChange(roundMinutes(value?.minus({ minutes: 30 })));
    };

    const handlePlus = () => {
        onChange(roundMinutes(value?.plus({ minutes: 30 })));
    };

    const labeltClassNames = clsx(
        {
            'text-[1.45rem]': true,
            'text-gray': theme == 'light',
            'text-white': theme == 'dark',
            'block mb-0': true,
            "after:content-['*'] after:ml-1": required
        },
        labelClassName
    );

    const inputClassNames = clsx(
        {
            'w-full border-b-[1px] text-black bg-light-gray-200 rounded-lg p-2 text-center text-[1.7rem]': true,
            'focus:outline-none focus:border-b-carrot-orange': true,
            'border-b-[#77cbcb]': dirty,
            'border-error': error
        },
        innerClassName
    );

    const controllButtonClassNames = clsx({
        'h-14 aspect-square center-container rounded-md self-end cursor-pointer': true
    });

    return (
        <div className={tw(className, 'relative')}>
            <div className="flex">
                <div className={tw(controllButtonClassNames, 'bg-error')} onClick={handleMinus}>
                    V
                </div>
                <div className="basis-full mx-2">
                    <label htmlFor={`kanbanInput-${name}`} className={labeltClassNames}>
                        {label || ''}
                    </label>
                    <input
                        id={`kanbanInput-${name}`}
                        value={value}
                        autoComplete="off"
                        disabled
                        data-testid={`kanban-input--${name}`}
                        className={inputClassNames}
                    />
                </div>
                <div className={tw(controllButtonClassNames, 'bg-green')} onClick={handlePlus}>
                    ^
                </div>
            </div>
            <div className="text-error-500 bottom-1 pt-1 absolute translate-y-full">{error ? error : ''}</div>
        </div>
    );
};
