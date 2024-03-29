import { FC } from 'react';
import { useNavigate } from 'react-router-dom';
import { LoginForm } from 'src/app/layouts/auth/LoginForm';
import { Button } from '../components/shared/inputs/Button';

const LoginPage: FC = () => {

    const navigate = useNavigate();
    return (
            <div className="flex flex-col">
                <LoginForm className={'grow bg-white'} />
                <Button onClick={() => navigate("/register")}>Register</Button>
            </div>
    );
};

export default LoginPage;
 