<template>
    <div :class="$style.IndexPage">
        <HomeHero :data="hero"/>

        <SectionTemplate
            :title="projectSteps.title"
        >
            <HomeAboutCourse :data="projectSteps.steps"/>
        </SectionTemplate>

        <SectionTemplate
            :title="workProcess.title"
            is-blue
        >
            <HomeWorkProcess :data="workProcess.steps"/>
        </SectionTemplate>

        <HomeForm/>
    </div>
</template>

<script>
import HomeHero from '~/components/pages/home/HomeHero';
import HomeForm from '~/components/pages/home/form/HomeForm';
import SectionTemplate from '~/components/common/SectionTemplate';
import HomeAboutCourse from '~/components/pages/home/aboutCourse/HomeAboutCourse';
import HomeWorkProcess from '~/components/pages/home/workProcess/HomeWorkProcess';

export default {
    name: 'IndexPage',

    components: {
        HomeHero,
        SectionTemplate,
        HomeAboutCourse,
        HomeWorkProcess,
        HomeForm,
        // HomeReviews,
        // HomeMyWorks,
    },

    async asyncData({ app }) {
        const [
            hero,
            projectSteps,
            workProcess,
        ] = await Promise.all([
            app.$axios.$get(app.$api.header),
            app.$axios.$get(app.$api.projectSteps),
            app.$axios.$get(app.$api.workProcess),
        ]);

        return {
            hero: hero || {},
            projectSteps: projectSteps || {},
            workProcess: workProcess || {},
        };
    },

    data() {
        return {
            hero: {},
            projectSteps: {},
            workProcess: {},
        };
    },
};
</script>

<style lang="scss" module>
    .IndexPage {
        //
    }
</style>
