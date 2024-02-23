export default {
    messengers: '/api/messengers/?fields[0]=link&populate[icon][fields][0]=url',
    menuItems: '/api/menu-items/?fields[0]=label&fields[1]=value',
    heroBlock: '/api/hero-block/?populate[image][fields][0]=url',
    workProcesses: '/api/work-process-section/?populate[title][fields][0]=label&populate[title][fields][1]=value&populate[work_process_items][fields][0]=title&populate[work_process_items][fields][1]=text',
    cases: '/api/case-section/?populate[title][fields][0]=label&populate[title][fields][1]=value&populate[case_items][fields][0]=title&populate[case_items][fields][1]=text&populate[case_items][fields][2]=tasks&populate[case_items][fields][3]=imageTitle&populate[case_items][populate][image][fields][0]=url',
    reviews: '/api/review-items/?populate[image][fields][0]=url',
    services: '/api/services-section/?populate[title][fields][0]=label&populate[title][fields][1]=value&populate[services][fields][0]=title&populate[services][fields][1]=items',
    request: '/api/requests/',
};
