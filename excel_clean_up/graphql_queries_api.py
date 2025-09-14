import httpx
import asyncio
from main import read_excel

API_URL = "https://cbhi.habtechsolution.com/api/graphql"

read_excel('excel_file/Lideta SC 2nd round export_active_members_07-05-17.xlsx')

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

    openimis_session, JWT_token, X_CSRFToken = token.split(".")
    print(openimis_session, JWT_token, X_CSRFToken)
    
    
    headers = {
        "Authorization": f"openimis_session={openimis_session}; JWT={token};",
        "Content-Type": "application/json"
    }

    
    cookies = {
        "openimis_session": f"{openimis_session}",
        "X-CSRFToken": f"{X_CSRFToken}"
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

    create_family = """ 
        mutation {
            createFamily(
                input: {
                clientMutationId: "d4a802ed-ea10-4ae4-a8eb-148d21411a09"
                clientMutationLabel: "Create family - idk idk (ui34298348)"
                headInsuree: {
                    chfId: "ui34298348"
                    lastName: "idk"
                    otherNames: "idk"
                    genderId: "M"
                    dob: "1995-08-13"
                    head: true
                    marital: "N"
                    cardIssued: false
                    status: "AC"
                }
                locationId: 35
                poverty: false
                familyTypeId: "G"
                address: "somwhere"
                confirmationTypeId: "A"
                confirmationNo: "787967"
                jsonExt: "{}"
                }
            ) {
                clientMutationId
                internalId
            }
            }

    """

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
