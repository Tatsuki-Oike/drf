async function tokenValidate(token: string | null) {
    try {
        await $fetch(
            `http://localhost:8000/api-auth/token/verify/`, 
            {
                "method": "POST", 
                body: {"token": token}
            })
        return true
    } catch (error) {
        console.log("tokenValidateでERROR")
        return false
    }
}

type ResponseType = 
{
    "data": Ref<{
        "access": string
    }>
}
async function tokenRefresh() {
    try {
        const refresh = localStorage.getItem('refresh');
        const response: ResponseType = await useLazyFetch(
            `http://localhost:8000/api-auth/token/refresh/`,
            {
                key: "refresh",
                method: "POST",
                body: {"refresh": refresh}
            }
        )
        const newToken = response.data.value.access
        const validateFlg = await tokenValidate(newToken)
        if (validateFlg) localStorage.setItem('token', newToken);
        return validateFlg
    } catch (error) {
        console.log("tokenRefreshでERROR")
        return false
    }
}

export async function userLogin(token: string | null) {
    if(!token){
        return false
    } else {
        const validateFlg = await tokenValidate(token)
        if (!validateFlg) {
            const refreshFlg = await tokenRefresh()
            return refreshFlg
        } 
        return true
    }
  }