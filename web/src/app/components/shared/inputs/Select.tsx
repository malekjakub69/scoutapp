import { Combobox, Transition } from '@headlessui/react';
import { FC, useRef, useState } from 'react';
import { UseControllerProps, useController } from 'react-hook-form';
import { IcoCheck } from 'src/assets/icons';
import { twMerge as tw } from 'tailwind-merge';

interface ISelectOpt {
    id: string | number | boolean | null;
    name: string;
    deleted?: boolean;
    notVisible?: boolean;
}

interface ISearchSelectProps {
    className?: string;
    inputClassName?: string;
    labelClassName?: string;
    label?: string;
    opts: ISelectOpt[];
    disabled?: boolean;
    required?: boolean;
    dirty?: boolean;
    error?: string;
}

const SEARCH_DEFAULT_STYLES = 'border-b-[1px] text-gray-700 bg-light-gray-200 p-2 text-xl rounded-lg';
const SEARCH_DISABLED_STYLES = 'disabled:bg-light-gray-400 disabled:cursor-not-allowed disabled:text-light-gray-700';
const SEARCH_FOCUS_STYLES = 'focus:outline-none';
const ALL_SEARCH_STYLES = [SEARCH_DEFAULT_STYLES, SEARCH_DISABLED_STYLES, SEARCH_FOCUS_STYLES].join(' ');

const OPTS_MENU_STYLES = 'absolute w-full py-3 mt-2 overflow-auto text-base bg-white rounded-[1.5rem] shadow-lg focus:outline-none kaizen-scroll z-50';
const OPT_DEFAULT_STYLES = 'select-none cursor-pointer flex justify-between items-stretch text-option-md text-gray-dark';
const OPT_ACTIVE_STYLES = 'text-carrot-orange-500 bg-light-gray-200';

const ARROW_BG_DEFAULT_STYLES = 'rounded-full w-10 h-10';
const ARROW_DEFAULT_STYLES = 'fill-gray-400 w-5 h-5 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2';
const ARROW_UP_STYLES = 'absolute right-0 top-1 rotate-180 transition duration-500';
const ARROW_DOWN_STYLES = 'absolute right-0 top-1 rotate-0 transition duration-500';

export const SearchSelect: FC<ISearchSelectProps & UseControllerProps<any>> = ({
    opts,
    label,
    className,
    disabled,
    required,
    dirty,
    error,
    inputClassName,
    labelClassName,
    ...props
}) => {
    const {
        field: { value, onChange }
    } = useController(props);

    const [query, setQuery] = useState('');
    const filteredOpts =
        query === '' ? opts : opts.filter((opt) => opt.id && opt.name.toLowerCase().replace(/\s+/g, '').includes(query.toLowerCase().replace(/\s+/g, '')));
    const inputRef = useRef<HTMLInputElement>(null);
    const node = useRef<HTMLDivElement>(null);

    return (
        <div className={`${className}`} ref={node}>
            <Combobox
                value={opts?.find((opt) => opt.id === value) || null}
                onChange={(v) => {
                    if (onChange) onChange(v?.id);
                }}
                disabled={disabled}
            >
                {({ open }) => (
                    <div className={'relative'}>
                        <Combobox.Label
                            className={tw(`text-label-gray text-label-md mb-0 ${required ? "after:content-['*'] after:ml-1" : ''}`, labelClassName)}
                        >
                            {label || ''}
                        </Combobox.Label>
                        <Combobox.Button className="w-full bg-transparent text-left flex justify-between items-stretch">
                            <div
                                className="basis-full relative text-input-md"
                                onClick={(event) => {
                                    if (open) event.preventDefault();
                                }}
                            >
                                <Combobox.Input
                                    ref={inputRef}
                                    autoComplete="off"
                                    displayValue={(opt: ISelectOpt) => {
                                        return opt && opt.id !== undefined ? opt.name : '';
                                    }}
                                    onChange={(event) => setQuery(event.target.value)}
                                    className={`w-full text-input-md ${tw(ALL_SEARCH_STYLES, inputClassName)} ${dirty ? 'border-b-[#77cbcb]' : ''} ${
                                        error ? 'border-error' : ''
                                    } focus:border-b-[#323e99]`}
                                    data-testid={`kaizen-search-select--${props.name}`}
                                ></Combobox.Input>
                                <div className={`${open ? ARROW_UP_STYLES : ARROW_DOWN_STYLES}`}>
                                    <div className={`${ARROW_BG_DEFAULT_STYLES}`}>
                                        ^
                                    </div>
                                </div>
                            </div>
                            <div className="text-error-500 bottom-1 pt-1 absolute translate-y-full">{error}</div>
                        </Combobox.Button>
                        <Transition
                            as={'div'}
                            show={open}
                            afterLeave={() => {
                                setQuery('');
                                inputRef.current?.blur();
                            }}
                        >
                            <Combobox.Options className={`${OPTS_MENU_STYLES} max-h-[20rem]`}>
                                {filteredOpts
                                    .filter((opt) => !opt.notVisible || opt.id === value)
                                    .filter((opt) => !opt.deleted || opt.id === value)
                                    .map((opt, optIdx) => (
                                        <Combobox.Option
                                            key={optIdx}
                                            value={opt}
                                            className={({ active }) => `${OPT_DEFAULT_STYLES} ${active && OPT_ACTIVE_STYLES}`}
                                        >
                                            {({ selected }) => (
                                                <>
                                                    <div key="check" className="basis-10 flex justify-center items-center">
                                                        {selected && <IcoCheck className="w-1/2 fill-carrot-orange ml-3" />}
                                                    </div>
                                                    <div
                                                        key="value"
                                                        className={`basis-full truncate pl-3 py-2.5 ${
                                                            selected ? 'font-semibold text-carrot-orange' : 'font-normal'
                                                        }`}
                                                    >
                                                        {opt.name}
                                                    </div>
                                                </>
                                            )}
                                        </Combobox.Option>
                                    ))}
                            </Combobox.Options>
                        </Transition>
                    </div>
                )}
            </Combobox>
        </div>
    );
};
