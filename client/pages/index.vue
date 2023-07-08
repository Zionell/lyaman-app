<template>
    <div :class="$style.IndexPage">
        <HomeHero v-if="hero && hero.title" :data="hero"/>

        <SectionTemplate
            v-if="projectSteps && projectSteps.steps"
            :title="projectSteps.title"
        >
            <HomeAboutCourse :data="projectSteps.steps"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="workProcess && workProcess.steps"
            :title="workProcess.title"
            is-blue
        >
            <HomeWorkProcess :data="workProcess.steps"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="certificates && certificates.certs"
            :title="certificates.title"
        >
            <HomeCertificates :data="certificates.certs"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="reviews && reviews.review"
            :title="reviews.title"
            is-blue
        >
            <HomeReviews :data="reviews.review"/>
        </SectionTemplate>

        <HomeForm id="contacts"/>
    </div>
</template>

<script>
import HomeHero from '~/components/pages/home/HomeHero';
import HomeForm from '~/components/pages/home/form/HomeForm';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAboutCourse from '~/components/pages/home/aboutCourse/HomeAboutCourse';
import HomeWorkProcess from '~/components/pages/home/workProcess/HomeWorkProcess';
import HomeCertificates from '~/components/pages/HomeCertificates';
import HomeReviews from '~/components/pages/home/HomeReviews';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAboutCourse,
        HomeWorkProcess,
        HomeForm,
        HomeCertificates,
        HomeReviews,
    },

    async asyncData({ app }) {
        try {
            const [
                hero,
                projectSteps,
                workProcess,
                certificates,
                reviews,
            ] = await Promise.all([
                app.$axios.$get(app.$api.header),
                app.$axios.$get(app.$api.projectSteps),
                app.$axios.$get(app.$api.workProcess),
                app.$axios.$get(app.$api.certificates),
                app.$axios.$get(app.$api.reviews),
            ]);

            return {
                hero: hero || {},
                projectSteps: projectSteps || {},
                workProcess: workProcess || {},
                certificates: certificates || {},
                reviews: reviews || {},
            };
        } catch (e) {
            console.warn(e);
        }
    },

    data() {
        return {
            hero: {},
            projectSteps: {},
            workProcess: {},
            certificates: {},
            reviews: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
