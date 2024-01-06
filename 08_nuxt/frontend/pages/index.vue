<script setup lang="ts">

type UserType = {
            username: string;
            password: string;
        }
type ResponseType = 
{
    "data": Ref<{
        "access": string,
        "refresh": string
    }>
}
const router = useRouter()

const login = async () => {

    const adminUser: UserType = {
        username: "admin",
        password: "userpass"
    }

    const response: ResponseType = await useLazyFetch(
        `http://localhost:8000/api-auth/token/`,
        {
            key: "login",
            method: "POST",
            body: adminUser
        }
    )
    const data = response.data
    localStorage.setItem('token', response.data.value.access);
    localStorage.setItem('refresh', data.value.refresh);
    router.push({name: "app"})
}

const logout = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("refresh")
    console.log("ログアウトしました")
}

</script>

<template>
    <h3 class="mt-5"> Login </h3>
    <button v-on:click="login" 
        class="btn btn-outline-primary mt-3"> Login </button>  
    <button v-on:click="logout" 
        class="btn btn-outline-danger mt-3 mx-3"> Logout </button>  
</template>
