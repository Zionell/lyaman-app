<template>
    <main :class="$style.IndexPage">
        <HomeHero id="main" :data="hero"/>

        <SectionTemplate
            v-if="aboutCourse.steps.length"
            id="about-course"
            :title="aboutCourse.title"
        >
            <HomeAboutCourse :data="aboutCourse.steps"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="myWorks.works.length"
            id="my-works"
            :title="myWorks.title"
        >
            <HomeMyWorks :data="myWorks.works"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="reviews.length"
            id="my-works"
            title="Отзывы"
        >
            <HomeReviews :slides="reviews"/>
        </SectionTemplate>

        <HomeForm id="contacts" :data="form"/>
    </main>
</template>

<script>
import HomeHero from '~/components/pages/home/HomeHero';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAboutCourse from '~/components/pages/home/aboutCourse/HomeAboutCourse';
import HomeForm from '~/components/pages/home/form/HomeForm';
import HomeMyWorks from '~/components/pages/home/works/HomeMyWorks';
import HomeReviews from '~/components/pages/home/HomeReviews';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAboutCourse,
        HomeForm,
        HomeReviews,
        HomeMyWorks,
    },

    async asyncData({ app }) {
        const [
            hero, aboutCourse, reviews, form, myWorks,
        ] = await Promise.all([
            app.$axios.$get(app.$api.hero),
            app.$axios.$get(app.$api.aboutCourse),
            app.$axios.$get(app.$api.reviews),
            app.$axios.$get(app.$api.form),
            app.$axios.$get(app.$api.myWorks),
        ]);

        return {
            hero: hero || {},
            aboutCourse: aboutCourse || {},
            reviews: reviews?.reviews || [],
            form: form || {},
            myWorks: myWorks || {},
        };
    },

    data() {
        return {
            hero: {},
            about: {},
            aboutCourse: {},
            reviews: [],
            form: {},
            myWorks: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
