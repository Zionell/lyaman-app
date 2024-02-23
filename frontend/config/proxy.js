export const proxy = () => ({
    '/api': {
        target: process.env.SERVER_API_URL,
        secure: false,
    },
});
