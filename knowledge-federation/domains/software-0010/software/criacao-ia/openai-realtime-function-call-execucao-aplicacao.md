---
id: software.criacao_ia.tranche05.000447
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://developers.openai.com/api/docs/guides/realtime-mcp", "https://developers.openai.com/api/docs/guides/realtime-conversations"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime: executar function calls no aplicativo e devolver function_call_output

## Em uma frase
Uma ferramenta function descreve uma chamada que o modelo pode solicitar, mas a lógica de negócio roda na aplicação e seu resultado retorna como `function_call_output`.

## Por que importa
A separação deixa verificações de autorização, validação de argumentos e efeitos externos sob controle do serviço responsável, não do texto gerado.

## Como funciona
Declare esquema e política de seleção no nível de sessão ou resposta; detecte o item de chamada, valide argumentos, execute a função e envie `conversation.item.create` com o call_id e o resultado antes de solicitar continuação.

## Exemplo
O modelo solicita consulta de pedido; o servidor valida o usuário e o número, consulta o banco, envia estado limitado como saída da função e então pede uma resposta em linguagem natural.

## Limites e trade-offs
O esquema ajuda a formar argumentos, mas não autoriza acesso nem torna uma operação segura ou idempotente. MCP remoto é outra modalidade e pode ser executado pela API.

## Como verificar
Teste argumentos malformados, usuário sem permissão, erro de dependência e resultado bem-sucedido; confirme que nenhuma ação externa ocorre antes das checagens do servidor.

## Conexões
- [[openai-realtime-interromper-audio-e-truncate]] — OpenAI Realtime: sincronizar áudio interrompido com conversation.item.truncate.
- [[openai-realtime-out-of-band-conversation-none]] — OpenAI Realtime: isolar respostas auxiliares com conversation none e metadata.

## Fontes
- [OpenAI Realtime — Realtime with tools](https://developers.openai.com/api/docs/guides/realtime-mcp) — Distingue execução local de function tools de ferramentas MCP executadas remotamente pela API. Consulta: 2026-10-04.
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Demonstra o ciclo de chamada, criação de function_call_output e resposta subsequente. Consulta: 2026-10-04.
