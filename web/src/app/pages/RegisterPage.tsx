import { FC } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from '../components/shared/inputs/Button';
import { RegisterForm } from '../layouts/auth/RegisterForm';

const RegisterPage: FC = () => {

    const navigate = useNavigate();

    return (
            <div className="flex flex-col">
                <RegisterForm className={'grow bg-white'} />
                <Button onClick={() => navigate("/login")}>Log in</Button>
            </div>
    );
};

export default RegisterPage;
