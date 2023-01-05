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

        <HomeForm id="contacts" :data="form"/>
    </main>
</template>

<script>
import HomeHero from '~/components/pages/HomeHero';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAbout from '~/components/pages/about/HomeAbout';
import HomeAboutCourse from '~/components/pages/aboutCourse/HomeAboutCourse';
import HomeForm from '~/components/pages/form/HomeForm';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAbout,
        HomeAboutCourse,
        HomeForm,
    },

    async asyncData({ app }) {
        const [
            hero, about, aboutCourse, form,
        ] = await Promise.all([
            app.$axios.$get(app.$api.hero),
            app.$axios.$get(app.$api.about),
            app.$axios.$get(app.$api.aboutCourse),
            app.$axios.$get(app.$api.form),
        ]);

        return {
            hero: hero,
            about: about,
            aboutCourse: aboutCourse,
            form: form,
        };
    },

    data() {
        return {
            hero: {},
            about: {},
            aboutCourse: {},
            form: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
