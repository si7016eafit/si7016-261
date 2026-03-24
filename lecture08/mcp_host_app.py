 from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-5",
    tools=[
        {
            "type": "mcp",
            "server_label": "openai_docs",
            "server_description": "Servidor MCP oficial de documentación de OpenAI",
            "server_url": "https://developers.openai.com/mcp",
            "require_approval": "never"
        }
    ],
    input=(
        "Busca en la documentación de OpenAI qué es MCP y "
        "resúmeme las diferencias entre MCP Host, MCP Client y MCP Server."
    ),
)

print(resp.output_text)