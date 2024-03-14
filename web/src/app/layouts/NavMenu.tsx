import { FC, ReactNode, useMemo, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Menu, MenuItem, Sidebar, SubMenu } from 'react-pro-sidebar';
import { useMediaQuery } from 'react-responsive';
import { Link } from 'react-router-dom';
import useLogout from 'src/app/hooks/useLogout';
import { IcoHome, IcoPeople, IcoPower } from 'src/assets/icons';
import useAuth from '../hooks/useAuth';

let LARGE_LOGO: string;
import('../../assets/images/large-logo.png').then((res) => (LARGE_LOGO = res.default));

interface IProps {
    className?: string;
    toggled: boolean;
    setToggled: (expanded: boolean) => void;
}

interface INavItem {
    icon?: ReactNode;
    name: string;
    url: string;
    submenu?: INavItem[];
}

export const NavMenu: FC<IProps> = ({ className, toggled, setToggled }) => {
    const { t } = useTranslation();

    const { user } = useAuth();
    const { logout } = useLogout();

    const isMobileDevice = useMediaQuery({ query: '(max-width: 1024px)' });

    const [open, setOpen] = useState<string | undefined>(undefined);
    const [collapsed, setCollapsed] = useState<boolean>(false);
    const [_, setBroken] = useState(window.matchMedia('(max-width: 1024px)').matches);

    const handleOpenSubMenu = (key: string) => {
        if (open === key) {
            setOpen(undefined);
        } else {
            setOpen(key);
        }
    };

    const navItems = useMemo<INavItem[]>(
        () => [
            {
                icon: <IcoHome className="menu-icon" />,
                name: t('Home'),
                url: 'home'
            },
            {
                icon: <IcoPeople className="menu-icon" />,
                name: t('People'),
                url: 'people'
            }
        ],
        [t]
    );

    return (
        <Sidebar
            toggled={toggled}
            collapsed={collapsed}
            onBackdropClick={() => setToggled(false)}
            customBreakPoint="1024px"
            onBreakPoint={setBroken}
            transitionDuration={1000}
            backgroundColor="none"
            className=" menu-bg text-white"
        >
            {/* LOGO element */}
            <div className="flex items-center justify-center h-20 mt-4">
                <img src={LARGE_LOGO} alt="logo" className="w-40" />
            </div>

            {/* USER element */}
            <Menu className="w-full my-4">
                <SubMenu
                    key={'user'}
                    label={
                        <div className=" w-full text-center">
                            {user?.first_name} {user?.last_name}
                        </div>
                    }
                    icon={
                        <span className="flex items-center justify-center rounded-full bg-green-300 text-black px-3 py-1 aspect-square">
                            {user?.first_name[0]}
                            {user?.last_name[0]}
                        </span>
                    }
                    open={open === 'user'}
                    onClick={() => handleOpenSubMenu('user')}
                >
                    <MenuItem
                        icon={<IcoPeople className="menu-icon text-left" />}
                        className="menu-item-bg"
                        key={'profile'}
                        component={<Link onClick={() => setToggled(false)} to={'profile'} />}
                    >
                        Profile
                    </MenuItem>
                </SubMenu>
            </Menu>

            {/* MENU element */}
            <Menu>
                {navItems.map((item) => {
                    if (item.submenu) {
                        return (
                            <SubMenu key={item.url} label={item.name} icon={item.icon} onClick={() => handleOpenSubMenu(item.name)} open={open === item.name}>
                                {item.submenu.map((subitem) => (
                                    <MenuItem
                                        className="menu-item-bg"
                                        icon={subitem.icon}
                                        key={subitem.url}
                                        component={<Link onClick={() => setToggled(false)} to={subitem.url} />}
                                    >
                                        {subitem.name}
                                    </MenuItem>
                                ))}
                            </SubMenu>
                        );
                    } else {
                        return (
                            <MenuItem
                                className="menu-item-bg"
                                key={item.url}
                                icon={item.icon}
                                component={<Link onClick={() => setToggled(false)} to={item.url} />}
                            >
                                {item.name}
                            </MenuItem>
                        );
                    }
                })}
            </Menu>

            {!isMobileDevice && (
                <div
                    className="absolute top-4 -right-6 rounded-md text-red w-12 h-8 bg-green-300 flex items-center justify-center cursor-pointer"
                    onClick={() => setCollapsed((value) => !value)}
                >
                    {collapsed ? '>>' : '<<'}
                </div>
            )}

            {/* Logout MENU element */}
            <Menu className="absolute bottom-4 w-full">
                <MenuItem
                    className="menu-item-bg"
                    key={'lougout'}
                    icon={<IcoPower className="menu-icon" />}
                    component={<Link to={''} onClick={() => logout()} />}
                >
                    {t('Logout')}
                </MenuItem>
            </Menu>
        </Sidebar>
    );
};
