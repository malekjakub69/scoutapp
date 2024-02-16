import { yupResolver } from '@hookform/resolvers/yup';
import { FC } from "react";
import { useForm } from "react-hook-form";
import { AuthApi } from 'src/api';
import { Button } from 'src/app/components/shared/inputs/Button';
import Input from 'src/app/components/shared/inputs/Input';
import { object, string } from 'yup';

interface FormValues {
    login: string;
    email: string;
    first_name: string;
    nickname?: string;
    last_name: string;
    password: string;
    password_2: string;
}

interface IProps {
    className?: string;
}

const formSchema = object().shape({
    login: string().required('Please enter your login'),
    email: string().required('Please enter your email').email('Please enter a valid email'),
    first_name: string().required('Please enter your first name'),
    nickname: string(),
    last_name: string().required('Please enter your last name'),
    password: string().required('Please enter your password'),
    password_2: string().required('Please enter your password again')
});

export const RegisterForm: FC<IProps> = ({  }) => {
 

    const {
        handleSubmit,
        formState: { errors }
    } = useForm<FormValues>({
        resolver: yupResolver(formSchema)
    });

    const handleSend = (data: FormValues) => {
        AuthApi.logIn(data);
    }

    return (
        <form onSubmit={handleSubmit(handleSend)} className="flex flex-col justify-center gap-2 m-2">
            <Input name="login" label="Login" error={errors.login?.message} />
            <Input name="email" label="Email" error={errors.email?.message} />
            <Input name="first_name" label="First name" error={errors.first_name?.message} />
            <Input name="nickname" label="Nickname" error={errors.nickname?.message} />
            <Input name="last_name" label="Last name" error={errors.last_name?.message} />
            <Input name="password" label="Password" type="password" error={errors.password?.message} />
            <Input name="password_2" label="Password again" type="password" error={errors.password_2?.message} />
            <Button type="submit">Register</Button>
            
        </form>
    )
}