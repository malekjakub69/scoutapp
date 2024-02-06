import revalidateAccessToken from './responseInterceptors';
import attachToken from './requestInterceptors';
const interceptors = {
    responseTokenRevalidation: revalidateAccessToken,
    requestAttachToken: attachToken
};

export default interceptors;
