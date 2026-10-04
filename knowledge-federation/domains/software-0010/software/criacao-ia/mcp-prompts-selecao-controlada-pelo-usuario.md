---
id: software.criacao_ia.tranche03.000217
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/server/prompts", "https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP prompts: distinguir seleção do usuário e autoria do servidor

## Em uma frase
MCP prompts são desenhados para seleção explícita pelo usuário, embora o conteúdo e a descrição do template sejam definidos pelo servidor.

## Por que importa
Uma aplicação pode expor templates como comandos de interface, mas não deve confundir a origem do texto com a decisão de executá-lo. A resposta de `prompts/get` pode conter mensagens, recursos incorporados e argumentos que entram no contexto do modelo, portanto precisa ser revisada como conteúdo de confiança limitada.

## Como funciona
Anuncie a capacidade `prompts` em `server/discover`, disponibilize uma lista paginável e retorne conteúdo por `prompts/get`. A interface deixa claro o nome do servidor e dá ao usuário uma ação de seleção compreensível. Se a resposta depender de credenciais, a disponibilidade pode variar por autorização no request; notificação `list_changed` e cache devem seguir o escopo correto.

## Exemplo
Uma ferramenta de edição oferece o prompt `review_material` numa paleta de comandos. O usuário escolhe o comando, confere argumento de projeto e recebe as mensagens preparadas pelo servidor; o cliente registra a origem e não executa prompts ocultos apenas porque um servidor os listou.

## Limites e trade-offs
A especificação não impõe um desenho visual único nem garante que instruções recebidas sejam seguras. Conteúdo do servidor pode incluir instruções adversariais ou dados embutidos; seleção humana não substitui revisão de segurança do cliente e do modelo.

## Como verificar
Teste seleção, cancelamento, permissões diferentes, mudança na lista e conteúdo que inclui recursos. Confirme que o método só é invocado após a ação definida pela aplicação e que uma resposta não pode ampliar permissões do servidor.

## Conexões
- [[mcp-tools-list-schema-autorizacao]] — MCP tools/list: catálogo determinístico e schema de entrada executável.
- [[mcp-elicitation-form-url-segredos]] — MCP elicitation: reservar URL mode para credenciais e segredos.

## Fontes
- [MCP 2026-07-28 — Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts) — define prompts como user-controlled e os métodos list/get Consulta: 2026-10-04.
- [MCP 2026-07-28 — Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) — detalha revisão de consentimento e riscos em intermediação MCP Consulta: 2026-10-04.
