import clsx from 'clsx';
import { FC } from 'react';
import { useTranslation } from 'react-i18next';
import useAuth from '../hooks/useAuth';

interface IProps {
    className?: string;
    toggleMenu: () => void;
}
export const AppMenu: FC<IProps> = ({ className, toggleMenu }) => {
    const { t } = useTranslation();
    const { user } = useAuth();

    const appMenuStyle = clsx({ 'bg-green-black flex items-center justify-center relative border-b-[1px] border-b-beige w-full': true }, className);

    return (
        <div className={appMenuStyle}>
            <div className="absolute left-2 top-0 tablet:hidden text-[2rem] text-beige" onClick={toggleMenu}>
                #
            </div>
            <span className=" text-beige">{user?.current_unit.name}</span>
        </div>
    );
};
