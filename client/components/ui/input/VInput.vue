<template>
    <label :class="$style.label">
        {{ labelValue }}
        <textarea
            v-if="type === 'textarea'"
            :value="value"
            :class="$style.textarea"
            :placeholder="placeholder"
            @input="$emit('input', $event.target.value)"
        />
        <input
            v-else
            :value="value"
            :type="type"
            :class="$style.input"
            :placeholder="placeholder"
            @input="$emit('input', $event.target.value)"
        />
        <span v-if="error" :class="$style.error">{{ error }}</span>
    </label>
</template>

<script>
export default {
    name: 'VInput',

    props: {
        type: {
            type: String,
            default: 'text',
        },

        labelValue: {
            type: String,
            default: 'text',
        },

        placeholder: {
            type: String,
            default: '',
        },

        error: {
            type: String,
            default: '',
        },
    },

    data() {
        return {
            value: '',
        };
    },
};
</script>

<style lang="scss" module>
    .label {
        @extend .p16b;

        position: relative;
        display: grid;
        gap: .4rem;

        @include respond-to(mobile) {
            font-size: 1.4rem;
        }
    }

    .input,
    .textarea {
        @extend .p14;

        padding: .9rem 1.8rem;
        border-radius: 2rem;
        border: 1px solid var(--border);
    }

    .textarea {
        resize: none;
        min-height: 10rem;
    }

    .error {
        @extend .p14;

        position: absolute;
        bottom: -2.4rem;
        left: 0;
        color: $error;
    }
</style>
