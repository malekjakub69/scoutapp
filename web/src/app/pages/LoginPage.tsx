import { FC } from 'react';
import { LoginForm } from 'src/app/layouts/auth/LoginForm';

const LoginPage: FC = () => {
    return (
            <div className="grow shrink flex w-full tabletSm:w-[38rem] tablet:w-[50rem] shadow-lg">
                <LoginForm className={'basis-1/2 grow bg-white'} />
            </div>
    );
};

export default LoginPage;
