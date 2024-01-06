export default defineNuxtRouteMiddleware(
    async (to, from) => {
        if (process.server) return navigateTo("/")

        if (process.client) {
            const token = localStorage.getItem('token');
            const validateFlg = await userLogin(token)
            if (!validateFlg) {
                console.log("トークンの検証失敗")
                return navigateTo("/")
            } else {
                console.log("トークンの検証成功")
                return
            }
        }
    }
)
