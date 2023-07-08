import SwiperCore, {
    Mousewheel,
    Navigation,
    Pagination,
    Autoplay,
    Lazy,
    Controller,
    Scrollbar,
} from 'swiper';
import 'swiper/swiper-bundle.css';

export default (ctx, inject) => {
    SwiperCore.use([Navigation, Scrollbar, Pagination, Mousewheel, Autoplay, Lazy, Controller]);

    inject('Swiper', SwiperCore);
};
