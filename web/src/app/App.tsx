import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { FC } from 'react';
import { Navigate, RouterProvider, createBrowserRouter } from 'react-router-dom';
import { IcoLoader } from '../assets/icons';
import useAuth from './hooks/useAuth';
import LoginPage from './pages/LoginPage';
import { MainPage } from './pages/MainPage';
import RegisterPage from './pages/RegisterPage';
import { ScoutNotificationCenter } from './components/ScoutNotificationCenter';

const basenamePrefix = import.meta.env.VITE_FE_BASENAME_PREFIX;
export const queryClient = new QueryClient({ defaultOptions: { queries: { refetchOnWindowFocus: false } } });

const PrivatePlantRoute: FC = () => {
    const { user, authError, authLoading } = useAuth();

    if (authError || (authLoading === false && user === null)) return <Navigate to="/login" />;
    if (authLoading) return <IcoLoader className={'m-auto animate-spin w-10 fill-blue-50'} />;

    return <MainPage />;
};

export const appRouter = createBrowserRouter(
    [
        { path: 'login', Component: LoginPage },
        { path: 'register', Component: RegisterPage },
        { path: 'new_password', element: <></> },
        {
            path: '*',
            Component: PrivatePlantRoute,
            children: [
                { path: 'home', element: <>HOME</> },
                { path: 'people', element: <>PEOPLE</> },
                { path: 'profile', element: <>PROFILE</> },
                { path: '*', element: <Navigate to="/home" /> }
            ]
        }
    ],
    { basename: basenamePrefix }
);

const App: FC = () => (
    <QueryClientProvider client={queryClient}>
        <div>
            <ScoutNotificationCenter />
            <RouterProvider router={appRouter} />
        </div>
        <ReactQueryDevtools />
    </QueryClientProvider>
);

export default App;
