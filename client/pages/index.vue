<template>
    <main :class="$style.IndexPage">
        <HomeHero id="main" :data="hero"/>

        <SectionTemplate
            v-if="about.ways"
            id="about"
            :title="about.title"
        >
            <HomeAbout :data="about.ways"/>
        </SectionTemplate>

        <SectionTemplate
            v-if="aboutCourse.steps"
            id="about-course"
            :title="aboutCourse.title"
        >
            <HomeAboutCourse :data="aboutCourse.steps"/>
        </SectionTemplate>
    </main>
</template>

<script>
import HomeHero from '~/components/pages/HomeHero';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAbout from '~/components/pages/about/HomeAbout';
import HomeAboutCourse from '~/components/pages/aboutCourse/HomeAboutCourse';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAbout,
        HomeAboutCourse,
    },

    async asyncData({ app }) {
        const [
            hero, about, aboutCourse,
        ] = await Promise.all([
            app.$axios.$get(app.$api.hero),
            app.$axios.$get(app.$api.about),
            app.$axios.$get(app.$api.aboutCourse),
        ]);

        return {
            hero: hero,
            about: about,
            aboutCourse: aboutCourse,
        };
    },

    data() {
        return {
            hero: {},
            about: {},
            aboutCourse: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
