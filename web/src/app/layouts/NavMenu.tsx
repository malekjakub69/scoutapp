import { FC, ReactNode, useMemo, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Menu, MenuItem, Sidebar, SubMenu } from 'react-pro-sidebar';
import { Link } from 'react-router-dom';
import { IcoCheck, IcoDelete } from 'src/assets/icons';
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
                icon: <IcoDelete className="fill-white w-5" />,
                name: t('Order material'),
                url: 'order-material',
                submenu: [
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('AAAA BOM'), url: 'bom' },
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('OrAAAAder BOM'), url: 'bom' }
                ]
            },
            {
                icon: <IcoDelete className="fill-white w-5" />,
                name: t('Order BOM'),
                url: 'bom',
                submenu: [
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('AAAA BOM'), url: 'bom' },
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('OrAAAAder BOM'), url: 'bom' }
                ]
            },
            {
                icon: <IcoDelete className="fill-white w-5" />,
                name: t('Orders'),
                url: 'orders',
                submenu: [
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('AAAA BOM'), url: 'bom' },
                    { icon: <IcoDelete className="fill-black w-5" />, name: t('OrAAAAder BOM'), url: 'bom' }
                ]
            },
            { icon: <IcoDelete className="fill-white w-5" />, name: t('In transit'), url: 'in-transit' },
            { icon: <IcoDelete className="fill-white w-5" />, name: t('Completed'), url: 'completed' },
            { icon: <IcoDelete className="fill-white w-5" />, name: t('Call of material'), url: 'call-of-material' }
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
        >
            {/* LOGO element */}
            <div className="flex items-center justify-center h-20 mt-6">
                <img src={LARGE_LOGO} alt="logo" className="w-40" />
            </div>

            {/* USER element */}
            <div className="flex items-center flex-col justify-center my-4">
                <span className="text-center rounded-full bg-green-300 text-black p-4 font-bold text-2xl mb-2">
                    {user?.first_name[0]}
                    {user?.last_name[0]}
                </span>
                {!collapsed && (
                    <span>
                        {user?.first_name} {user?.last_name}
                    </span>
                )}
            </div>

            {/* MENU element */}
            <Menu>
                {navItems.map((item) => {
                    if (item.submenu) {
                        return (
                            <SubMenu key={item.url} label={item.name} icon={item.icon} onClick={() => handleOpenSubMenu(item.name)} open={open === item.name}>
                                {item.submenu.map((subitem) => (
                                    <MenuItem icon={subitem.icon} key={subitem.url} component={<Link onClick={() => setToggled(false)} to={subitem.url} />}>
                                        {subitem.name}
                                    </MenuItem>
                                ))}
                            </SubMenu>
                        );
                    } else {
                        return (
                            <MenuItem key={item.url} icon={item.icon} component={<Link onClick={() => setToggled(false)} to={item.url} />}>
                                {item.name}
                            </MenuItem>
                        );
                    }
                })}
            </Menu>
            <div className="hidden tablet:block absolute top-2 right-2">
                <span onClick={() => setCollapsed((value) => !value)} className="text-2xl ">
                    X
                </span>
            </div>
            <div className="absolute bottom-0">
                <Menu>
                    <MenuItem icon={<IcoCheck />} key={'logout'} component={<Link onClick={() => setToggled(false)} to={'logout'} />} />
                </Menu>
            </div>
        </Sidebar>
    );
};
