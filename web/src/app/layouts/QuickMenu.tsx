import clsx from 'clsx';
import { FC } from 'react';
import { useTranslation } from 'react-i18next';
import { NavLink } from 'react-router-dom';
import { IcoDelete } from 'src/assets/icons';

interface IProps {
    className?: string;
}

const menuItems = [
    {
        name: 'Home',
        url: '/',
        icon: <IcoDelete className='fill-beige w-8' />,
    },
    {
        name: 'About',
        url: '/about', 
        icon: <IcoDelete className='fill-beige w-8' />,
    },
    {
        name: 'Contact',
        url: '/contact',
        icon: <IcoDelete className='fill-beige w-8' />,
    },
    {
        name: 'Login',
        url: '/login',
        icon: <IcoDelete className='fill-beige w-8' />,
    },
    {
        name: 'Register',
        url: '/register',
        icon: <IcoDelete className='fill-beige w-8' />,
    },
]

export const QuickMenu: FC<IProps> = ({ className }) => {
    const { t } = useTranslation();

    const appMenuStyle = clsx({"bg-green-black flex items-center justify-center justify-around w-full": true}, className);

    return (
        <div className={appMenuStyle}>
            {
                menuItems.map((item, index) => (
                    <NavLink
                        to={item.url}
                        className={`h-12 flex flex-row items-center gap-1.5 relative pl-2 hover:bg-scout-logo-blue2 `}
                        key={item.url}
                    >
                    <div key={index} className='flex flex-col items-center justify-center gap-1.5'>
                        <div className='aspect-square '>{item.icon}</div>
                    </div>
                    </NavLink>
                ))
            }
        </div>
    );
};
