<template>
    <div class="user-info">
        <img :src="user[0].picture" :alt="user.name" style="width:100px;margin-left:auto;margin-right:auto;" />
        <h1>Email: {{user[0].email}}</h1>
        <h1>Nickname: {{user[0].nickname}}</h1>
        <h1>Name: {{user[0].name}}</h1>
        <h1>ID: {{user[0].user_id}}</h1>
        <button @click="$router.push('edit-profile')">Edit</button>
    </div>
</template>

<script>
    import editProfileService from '../services/EditProfileService.js';
    export default {
        name: "userprofile",
        data() {
            return {
                user: {}
            }
        },
        created() {
            console.log(editProfileService.getUserByEmail);
            this.getUser();
        },
        methods: {
            async getUser() {
                const email = await this.$auth.user.email;
                editProfileService.getUserByEmail(email)
                    .then(
                        (user => {
                            this.$set(this, "user", user);
                        }).bind(this)
                    );
            }
        }
    }
</script>

<style lang="scss" scoped>
    .event-single {
        margin-top: 30px;
    }

    .hero {
        margin-bottom: 70px;
    }

    .event-images {
        margin-top: 50px;
    }

    .description {
        margin-bottom: 30px;
    }

    .user-info {
        text-align: center;
    }
</style>