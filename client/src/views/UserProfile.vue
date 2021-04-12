<template>
    <div class="user-info">
        <!-- <img :src="user[0].picture" :alt="user.name" style="width:100px;margin-left:auto;margin-right:auto;" /> -->
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
            this.token();
        },
        methods: {
            async getUser() {
                const email = await this.$auth.user.email;
                const token = await this.$auth.getTokenSilently();
                editProfileService.getUserByEmail(email,token)
                    .then(
                        (user => {
                            this.$set(this, "user", user);
                        }).bind(this)
                    );
            },
            async token(){
                var axios = require("axios").default;

                var options = {
                method: 'POST',
                url: 'https://dev-upkrd-9f.us.auth0.com/oauth/token',
                headers: {'content-type': 'application/x-www-form-urlencoded'},
                data: {
                    grant_type: 'client_credentials',
                    client_id: 'H7Nh5GQQTqSYNfoMSTDRRA6OE3DIta8G',
                    client_secret: 'TxYBn2bkEbsxNMgQ23dmR-xNhWKt3kBM1O71pCGlZWGZNsi7KUrbN2zGjqDUycUT',
                    audience: 'https://dev-upkrd-9f.us.auth0.com/api/v2/'
                }
                };

                axios.request(options).then(function (response) {
                    console.log(response.data);
                }).catch(function (error) {
                    console.error(error);
                });
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