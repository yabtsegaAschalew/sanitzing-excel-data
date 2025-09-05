import httpx
import asyncio

API_URL = "http://127.0.0.1:8000/api/graphql"

async def authenticate(username: str, password: str):
    mutation = f"""
    mutation {{
        tokenAuth(username: "{username}", password: "{password}") {{
            refreshExpiresIn
            payload
            token
        }}
    }}
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL,
            json={"query": mutation},
            headers={"Content-Type": "application/json"}
        )

    data = response.json()["data"]["tokenAuth"]

    token = data["token"]
    refresh_expires_in = data["refreshExpiresIn"]

    
    headers = {
        "Authorization": f"JWT {token}",
        "Content-Type": "application/json"
    }

    
    cookies = {
        "openimis_session": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
        "X_CSRFToken": "ssM9oXqlBXOeP3Cgto_llM9ZYghZG6SJhBkxJAQf63E"
    }

    return headers, cookies


async def send_mutation(headers, mutation: str, variables: dict = None, cookies: dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL,
            json={"query": mutation, "variables": variables or {}},
            headers=headers,
            cookies=cookies
        )
    return response.json()


async def main():
    headers, cookies = await authenticate("Admin", "admin123")

    create_mutation = """
        mutation {
            createInsuree(
                input: {
                clientMutationId: "create-minimal-insuree"
                # This chfid is not required. However if provided it will add it to the legacyID column
                lastName: "ASHEEEEEEEEEEE"
                middleName: "MIDDLE_NAME_PLACEHOLDER"
                otherNames: "OTHER_NAMES_PLACEHOLDER"
                genderId: "M"
                dob: "1990-01-15"
                marital: "S"
                passport: "P12345678"
                phone: "+251900000000"
                email: "john.doe@example.com"
                currentAddress: "CURRENT ADDRESS"
                disabilityStatus: "no_disability"
                cardIssued: false
                professionId: 2
                educationId: 3
                typeOfIdId: "P"
                offline: false
                status: "AC"
                statusDate: "2025-07-24"
                chfIdFormat: 3
                familyId: 1
                isActive: true
                addOnExistingPolicy: false
                }
            ) {
                internalId
            }
        }
    """

    result = await send_mutation(headers, create_mutation, cookies=cookies)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
