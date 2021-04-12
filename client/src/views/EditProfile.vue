<template>
    <div class="editForm">
        <form id="editFormInput">
            <label c="nameLabel" for="name">Name: </label>
            <input type="text" name="name" id="name" :value="user[0].name" />
            <br />
            <label for="nickname">Nickname: </label>
            <input type="text" name="nickname" id="nickname" :value="user[0].nickname" />
            <br />
            <input type="button" @click="submitName" value="Submit">

            <br /><br /><br />
            <button class="deleteButton" @click="deleteAccount">Delete Account</button>
        </form>
    </div>
</template>

<script>
    import editProfileService from '../services/EditProfileService.js';
    export default {
        name: "editprofile",
        data() {
            return {
                user: {}
            }
        },
        created() {
            this.getUser();
        },
        methods: {
            async getUser() {
                const email = this.$auth.user.email;
                editProfileService.getUserByEmail(email)
                    .then(
                        (user => {
                            this.$set(this, "user", user);
                        }).bind(this)
                    );
            },
            async submitName() {
                this.getUser();
                var nameValue = document.getElementById("name").value;
                var userid = this.user[0].user_id;
                console.log(userid);
                editProfileService.changeName(nameValue, userid);
            },
            async submitNickname() {
                this.getUser();
                var nameValue = document.getElementById("nickname").value;
                var userid = this.user[0].user_id;
                console.log(userid);
                editProfileService.changeNickname(nameValue, userid);
            },
            async deleteAccount() {
                this.getUser();
                var userid = this.user[0].user_id;
                editProfileService.deleteUser(userid);
            }
        }
    }
</script>

<style>
    .editForm {
        text-align: center
    }
</style>