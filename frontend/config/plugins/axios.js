export default ({ $axios, req }) => {
    // const headers = req && req.headers ? Object.assign({}, req.headers) : {};
    // $axios.setHeader('X-Forwarded-Host', headers['x-forwarded-host']);
    // $axios.setHeader('X-Forwarded-Port', headers['x-forwarded-port']);
    // $axios.setHeader('X-Forwarded-Proto', headers['x-forwarded-proto']);
    $axios.setHeader('Access-Control-Allow-Origin', '*');

    // $axios.setBaseURL(process.env.SERVER_API_URL)
};
