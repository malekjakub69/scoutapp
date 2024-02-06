import { Children, ComponentType, FC, ReactNode } from 'react';
import { NavLink } from 'react-router-dom';
import { AuthorizationCode } from '../../../types';

export interface ITabPage {
    tabName: string;
    tabUrl: string;
    authCode: AuthorizationCode | AuthorizationCode[];
    component: ComponentType;
}

interface ITabsContainerProps {
    className?: string;
    children?: ReactNode | ReactNode[];
}

const TabsContainer: FC<ITabsContainerProps> = ({ className, children }) => {
    return <div className={`flex ${className}`}>{Children.map(children, (child) => child)}</div>;
};

interface ITabProps {
    className?: string;
    to: React.ComponentProps<typeof NavLink>['to'];
    children?: ReactNode;
}

const Tab: FC<ITabProps> = ({ className, to, children }) => {
    return (
        <NavLink to={to} className={({ isActive }) => `ekanban-tab__secondary ${className || ''} ${isActive ? 'ekanban-tab__secondary--active' : ''}`}>
            {children}
        </NavLink>
    );
};

export const SecondaryTabs = Object.assign(TabsContainer, { Tab });
