export const proxy = base_url => ({
    '/strapi/v1/': {
        target: base_url,
        secure: false,
    },
});
