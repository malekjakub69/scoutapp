import { useMutation, useQueryClient } from '@tanstack/react-query';
import { AxiosError } from 'axios';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthApi } from '../../api';
import { UserLogin } from '../types';
import queryKeys from './queryKeys';

const useLogin = () => {
    const navigate = useNavigate();
    const queryClient = useQueryClient();
    const [errorMessage, setErrorMessage] = useState<string | undefined>(undefined);

    const {
        mutateAsync: login,
        isLoading,
        isError
    } = useMutation({
        mutationFn: (credentials: UserLogin) => AuthApi.logIn(credentials),
        onSuccess: (data) => {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            queryClient.resetQueries(queryKeys.AUTH_KEY);
            navigate('/');
        },
        onError: (response: AxiosError<{ message: string }>) => {
            setErrorMessage(response.response?.data.message);
        }
    });

    return { login, isLoading, isError, errorMessage };
};

export default useLogin;
