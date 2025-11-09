import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic.v1 import SecretStr

# --- PASTE YOUR API KEY HERE ---
YOUR_API_KEY = "AIzaSyDK9Cv_3s2UE7jhIbvcpWK3TwQDmOqunZU"
# -----------------------------

async def run_async_test():
    print("Testing LangChain's ASYNC Google Generative AI...")
    print("This replicates the server's async behavior...")

    try:
        # 1. Instantiate the model
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=SecretStr(YOUR_API_KEY).get_secret_value(),
            temperature=0.1,
        )

        # 2. Call the model ASYNCHRONOUSLY
        print("\nSending prompt via model.ainvoke()...")
        # This is the line that's different
        response = await model.ainvoke("Explain how AI works in a few words")

        # 3. Print the response
        print("\n--- ASYC LANGCHAIN RESPONSE ---")
        print(response.content)
        print("-------------------------------")

    except Exception as e:
        print(f"\n--- ASYNC LANGCHAIN ERROR ---")
        print(e)
        print("-----------------------------")

if __name__ == "__main__":
    print("Running async test...")
    asyncio.run(run_async_test())