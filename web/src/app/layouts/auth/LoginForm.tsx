import { yupResolver } from '@hookform/resolvers/yup';
import { FC } from "react";
import { useForm } from "react-hook-form";
import { Button } from 'src/app/components/shared/inputs/Button';
import Input from 'src/app/components/shared/inputs/Input';
import useLogin from 'src/app/hooks/useLogin';
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
    
    const { login, isLoading, isError } = useLogin();

    const {
        handleSubmit,
        register,
        formState: { errors }
    } = useForm<FormValues>({
        resolver: yupResolver<FormValues>(formSchema)
    });

    const handleSend = (data: FormValues) => {
        login(data)
    }

    return (
        <form onSubmit={handleSubmit(handleSend)} className="flex flex-col justify-center gap-2 m-2">
            <Input {...register('login')} label="Login" error={errors.login?.message} />
            <Input {...register('password')}  label="Password" type="password" error={errors.password?.message} />
            <div className={'basis-full text-sm text-error h-4 mb-2'}>{isError ? 'Nesprávné přihlašovací údaje' : undefined}</div>
            <Button status={isLoading ? "loading" : undefined } type="submit">Log in</Button>
            
        </form>
    )
}