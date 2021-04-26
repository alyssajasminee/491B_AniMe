import axios from "axios"

//const jwt = require("express-jwt");
//const jwksRsa = require("jwks-rsa");
//const jwtAuthz = require("express-jwt-authz");

//const authConfig = {
//    domain: process.env.AUTH0_DOMAIN,
//    audience: process.env.AUTH0_AUDIENCE,
//    clientId: process.env.CLIENT_ID,
//    clientSecret: process.env.CLIENT_SECRET
//};

//const managementAPI = new ManagementClient({
//    domain: authConfig.domain,
//    clientId: authConfig.clientId,
//    clientSecret: authConfig.clientSecret
//});

// Create middleware to validate the JWT using express-jwt
//const checkJwt = jwt({
//    // Provide a signing key based on the key identifier in the header and the signing keys provided by your Auth0 JWKS endpoint.
//    secret: jwksRsa.expressJwtSecret({
//        cache: true,
//        rateLimit: true,
//        jwksRequestsPerMinute: 5,
//        jwksUri: `https://${authConfig.domain}/.well-known/jwks.json`
//    }),

//    // Validate the audience (Identifier) and the issuer (Domain).
//    audience: authConfig.audience,
//    issuer: `https://${authConfig.domain}/`,
//    algorithms: ["HS256"]
//});

// let events = [...]

//const checkPermissions = jwtAuthz(['manage:users'], { customScopeKey: 'permissions' });

const getUsers = async (email) => {
    const res = await axios.get(`https://dev-upkrd-9f.us.auth0.com/api/v2/users`, {
        params: {
            email: `${email}`
        },
        headers: {
            Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNPTnV2MW9Cbl91dWtXcDNXcFRPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi11cGtyZC05Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiSDdOaDVHUVFUcVNZTmZvTVNURFJSQTZPRTNESXRhOEdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZGV2LXVwa3JkLTlmLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjE3NzcxNDM2LCJleHAiOjE2MTc4NTc4MzYsImF6cCI6Ikg3Tmg1R1FRVHFTWU5mb01TVERSUkE2T0UzREl0YThHIiwic2NvcGUiOiJyZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2lkcF90b2tlbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.vEBSBUZda-Pd_cc4tios1XT9egCFlPC0BDRXrOZXAUa_lJWY0rucbj_2KqfdZziCw1Vhf25i2Ar6Yq8CwghUklYoqCIgvWHSSmTABE7_jRvMa4azQnmiuVpaLwMX0LnLjfIrHJgOkH8Up9S54ptWxzash8EyjcMTmyjcOSFsUcU3XehYLymrttSaAedw6L27Vy1rivmgFL99_6dMiWi_5OT9fsSQdBL_2y4B_A-Av-R3FIb2BoiwQfe2Al_pxnc6FYPSHz8uoEjBu7vXgZVbXKnbT0dWlo01iNcTiiRL8p4-xtL-P1sp5cwrr6Sf3GUHEzsv4g9Ls6HC8kSKKINlnw`
        }
    });
    return res.data;
};

const getUserByEmail = async (email) => {
    const res = await axios.get(`https://dev-upkrd-9f.us.auth0.com/api/v2/users-by-email`, {
        params: {
            email: `${email}`
        },
        headers: {
            Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNPTnV2MW9Cbl91dWtXcDNXcFRPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi11cGtyZC05Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiSDdOaDVHUVFUcVNZTmZvTVNURFJSQTZPRTNESXRhOEdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZGV2LXVwa3JkLTlmLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjE3NzcxNDM2LCJleHAiOjE2MTc4NTc4MzYsImF6cCI6Ikg3Tmg1R1FRVHFTWU5mb01TVERSUkE2T0UzREl0YThHIiwic2NvcGUiOiJyZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2lkcF90b2tlbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.vEBSBUZda-Pd_cc4tios1XT9egCFlPC0BDRXrOZXAUa_lJWY0rucbj_2KqfdZziCw1Vhf25i2Ar6Yq8CwghUklYoqCIgvWHSSmTABE7_jRvMa4azQnmiuVpaLwMX0LnLjfIrHJgOkH8Up9S54ptWxzash8EyjcMTmyjcOSFsUcU3XehYLymrttSaAedw6L27Vy1rivmgFL99_6dMiWi_5OT9fsSQdBL_2y4B_A-Av-R3FIb2BoiwQfe2Al_pxnc6FYPSHz8uoEjBu7vXgZVbXKnbT0dWlo01iNcTiiRL8p4-xtL-P1sp5cwrr6Sf3GUHEzsv4g9Ls6HC8kSKKINlnw`
        }
    });
    return res.data;
}

const changeName = async (newName, userId) => {
    var options = {
        method: 'PATCH',
        url: `https://dev-upkrd-9f.us.auth0.com/api/v2/users/${userId}`,
        headers: {
            Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNPTnV2MW9Cbl91dWtXcDNXcFRPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi11cGtyZC05Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiSDdOaDVHUVFUcVNZTmZvTVNURFJSQTZPRTNESXRhOEdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZGV2LXVwa3JkLTlmLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjE3NzcxNDM2LCJleHAiOjE2MTc4NTc4MzYsImF6cCI6Ikg3Tmg1R1FRVHFTWU5mb01TVERSUkE2T0UzREl0YThHIiwic2NvcGUiOiJyZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2lkcF90b2tlbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.vEBSBUZda-Pd_cc4tios1XT9egCFlPC0BDRXrOZXAUa_lJWY0rucbj_2KqfdZziCw1Vhf25i2Ar6Yq8CwghUklYoqCIgvWHSSmTABE7_jRvMa4azQnmiuVpaLwMX0LnLjfIrHJgOkH8Up9S54ptWxzash8EyjcMTmyjcOSFsUcU3XehYLymrttSaAedw6L27Vy1rivmgFL99_6dMiWi_5OT9fsSQdBL_2y4B_A-Av-R3FIb2BoiwQfe2Al_pxnc6FYPSHz8uoEjBu7vXgZVbXKnbT0dWlo01iNcTiiRL8p4-xtL-P1sp5cwrr6Sf3GUHEzsv4g9Ls6HC8kSKKINlnw`
        },
        data: { name: `${newName}` }
    };

    axios.request(options).then(function (response) {
        console.log(response.data);
    }).catch(function (error) {
        console.error(error);
    });
}

const changeNickname = async (newNickname, userId) => {
    var options = {
        method: 'PATCH',
        url: `https://dev-upkrd-9f.us.auth0.com/api/v2/users/${userId}`,
        headers: {
            Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNPTnV2MW9Cbl91dWtXcDNXcFRPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi11cGtyZC05Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiSDdOaDVHUVFUcVNZTmZvTVNURFJSQTZPRTNESXRhOEdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZGV2LXVwa3JkLTlmLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjE3NzcxNDM2LCJleHAiOjE2MTc4NTc4MzYsImF6cCI6Ikg3Tmg1R1FRVHFTWU5mb01TVERSUkE2T0UzREl0YThHIiwic2NvcGUiOiJyZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2lkcF90b2tlbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.vEBSBUZda-Pd_cc4tios1XT9egCFlPC0BDRXrOZXAUa_lJWY0rucbj_2KqfdZziCw1Vhf25i2Ar6Yq8CwghUklYoqCIgvWHSSmTABE7_jRvMa4azQnmiuVpaLwMX0LnLjfIrHJgOkH8Up9S54ptWxzash8EyjcMTmyjcOSFsUcU3XehYLymrttSaAedw6L27Vy1rivmgFL99_6dMiWi_5OT9fsSQdBL_2y4B_A-Av-R3FIb2BoiwQfe2Al_pxnc6FYPSHz8uoEjBu7vXgZVbXKnbT0dWlo01iNcTiiRL8p4-xtL-P1sp5cwrr6Sf3GUHEzsv4g9Ls6HC8kSKKINlnw`
        },
        data: { nickname: `${newNickname}` }
    };

    axios.request(options).then(function (response) {
        console.log(response.data);
    }).catch(function (error) {
        console.error(error);
    });
}

const deleteUser = async (userId) => {
    var options = {
        method: 'GET',
        url: `https://dev-upkrd-9f.us.auth0.com/api/v2/users/${userId}/delete`,
        headers: {
            Authorization: `Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNPTnV2MW9Cbl91dWtXcDNXcFRPUSJ9.eyJpc3MiOiJodHRwczovL2Rldi11cGtyZC05Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiSDdOaDVHUVFUcVNZTmZvTVNURFJSQTZPRTNESXRhOEdAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZGV2LXVwa3JkLTlmLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjE3NzcxNDM2LCJleHAiOjE2MTc4NTc4MzYsImF6cCI6Ikg3Tmg1R1FRVHFTWU5mb01TVERSUkE2T0UzREl0YThHIiwic2NvcGUiOiJyZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2lkcF90b2tlbnMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.vEBSBUZda-Pd_cc4tios1XT9egCFlPC0BDRXrOZXAUa_lJWY0rucbj_2KqfdZziCw1Vhf25i2Ar6Yq8CwghUklYoqCIgvWHSSmTABE7_jRvMa4azQnmiuVpaLwMX0LnLjfIrHJgOkH8Up9S54ptWxzash8EyjcMTmyjcOSFsUcU3XehYLymrttSaAedw6L27Vy1rivmgFL99_6dMiWi_5OT9fsSQdBL_2y4B_A-Av-R3FIb2BoiwQfe2Al_pxnc6FYPSHz8uoEjBu7vXgZVbXKnbT0dWlo01iNcTiiRL8p4-xtL-P1sp5cwrr6Sf3GUHEzsv4g9Ls6HC8kSKKINlnw`
        },
    };

    axios.request(options).then(function (response) {
        console.log(response.data);
    }).catch(function (error) {
        console.error(error);
    });
}
export default {
    getUsers,
    getUserByEmail,
    changeName,
    changeNickname,
    deleteUser
}