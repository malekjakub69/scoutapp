import { FC, useCallback, useState } from 'react';
import { Outlet } from 'react-router-dom';
import { AppMenu } from '../layouts/AppMenu';
import { NavMenu } from '../layouts/NavMenu';
import { QuickMenu } from '../layouts/QuickMenu';

export const MainPage: FC = () => {
    const [toggledMenu, setToggledMenu] = useState<boolean>(false);

    const toggleMenu = useCallback(() => setToggledMenu((s) => !s), [setToggledMenu]);

    return (
        <div className="bg-green-black flex absolute top-0 left-0 right-0 bottom-0">
            <NavMenu toggled={toggledMenu} setToggled={setToggledMenu} className={' shrink-0 grow-0'} />
            <div className="flex flex-col basis-full shrink bg-tuna w-[100vw] max-h-full h-full overflow-hidden">
                <AppMenu toggleMenu={toggleMenu} className={'basis-12 shrink-0 grow-0'} />
                <div className="basis-full shrink px-10 py-7 overflow-hidden">
                    <Outlet />
                </div>
                {false && <QuickMenu className={'basis-12 shrink-0 grow-0'} />}
            </div>
        </div>
    );
};
