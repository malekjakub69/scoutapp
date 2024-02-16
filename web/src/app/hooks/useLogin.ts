import { useMutation, useQueryClient } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';
import { AuthApi } from '../../api';
import { UserLogin } from '../types';
import queryKeys from './queryKeys';

const useLogin = () => {
    const navigate = useNavigate();
    const queryClient = useQueryClient();

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
        }
    });

    return { login, isLoading, isError };
};

export default useLogin;
