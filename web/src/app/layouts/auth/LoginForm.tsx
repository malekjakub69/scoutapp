import { yupResolver } from '@hookform/resolvers/yup';
import { FC } from "react";
import { useForm } from "react-hook-form";
import { AuthApi } from 'src/api';
import { Button } from 'src/app/components/shared/inputs/Button';
import Input from 'src/app/components/shared/inputs/Input';
import { object, string } from 'yup';

interface FormValues {
    login: string;
    password: string;
}

interface IProps {
    className?: string;
}

const formSchema = object().shape({
    login: string().required('Please enter your login or email'),
    password: string().required('Please enter your password')
});

export const LoginForm: FC<IProps> = ({  }) => {
 

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
        <form onSubmit={handleSubmit(handleSend)} className="w-1/2 flex flex-col justify-center gap-2 m-2">
            <Input name="login" label="Login" error={errors.login?.message} />
            <Input name="password" label="Password" type="password" error={errors.password?.message} />
            <Button type="submit">Log in</Button>
            
        </form>
    )
}