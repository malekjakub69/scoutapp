import { clsx } from 'clsx';
import { FC, Fragment, ReactNode, useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { NavLink } from 'react-router-dom';
import { IcoDelete } from 'src/assets/icons';

let LARGE_LOGO: string;
import('../../assets/images/large-logo.png').then((res) => (LARGE_LOGO = res.default));

interface IProps {
    className?: string;
    expanded: boolean;
}

interface INavItem {
    icon?: ReactNode;
    name: string;
    url: string;
}

export const NavMenu: FC<IProps> = ({ className, expanded }) => {
    const { t } = useTranslation();

    const navItems = useMemo<INavItem[]>(
        () => [
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('Order material'), url: 'order-material', }, 
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('Order BOM'), url: 'bom', },
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('Orders'), url: 'orders' },
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('In transit'), url: 'in-transit' },
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('Completed'), url: 'completed' },
            {icon: <IcoDelete className='fill-white w-6'/> , name: t('Call of material'), url: 'call-of-material' }
        ],
        [t]
    );

        const navBarMenuStyle = clsx({"flex flex-col items-stretch nav-menu-grad overflow-auto bg-green-800 bg-opacity-70": true,
        "hidden": !expanded,}, className)

    return (
        <div className={navBarMenuStyle}>
            <div
                className={"h-[5.5rem] w-full flex justify-center align-center shrink-0 sticky z-10"}
            >
                <img src={LARGE_LOGO} className={'w-5/6 object-contain'} alt={'Logo'} />
            </div>
            {navItems.map(({ icon, name, url }) => {
                return (
                    <NavLink
                        to={url}
                        className={`h-12 flex flex-row items-center gap-1.5 relative pl-2 `}
                        key={url}
                    >
                        {({ isActive }) => (
                            <Fragment>
                                {isActive && <span className=" bg-scout-logo-yellow1 absolute h-full w-1 left-0"></span>}
                                <div className=' aspect-square rounded-lg border-[1px] border-white p-1'>{icon}</div>
                                <span className="text-white text-[0.85rem]">{name}</span>
                            </Fragment>
                        )}
                    </NavLink>
                );
            })}
        </div>
    );
};
