---
id: software.criacao_ia.tranche03.000214
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr", "https://modelcontextprotocol.io/specification/2026-07-28/server/tools"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP MRTR: retomar requests com inputResponses e requestState opaco

## Em uma frase
Multi Round-Trip Requests permite que um servidor peça dados adicionais dentro de um resultado e o cliente reenvie a operação original com as respostas.

## Por que importa
O padrão substitui requests JSON-RPC espontâneos iniciados pelo servidor na revisão 2026-07-28 e não depende de sessão compartilhada entre instâncias. Aplicações podem pausar um tool ou leitura, solicitar consentimento e continuar a mesma intenção mesmo quando o balanceador direciona a repetição a outro processo.

## Como funciona
O servidor responde `resultType=input_required` com um mapa de `inputRequests` e, opcionalmente, `requestState`. O cliente reúne respostas sob as mesmas chaves e reenvia o método original com `inputResponses`; quando fornecido, repassa `requestState` sem examinar, interpretar ou modificar seu conteúdo. O novo JSON-RPC request usa ID diferente. O servidor então conclui ou devolve outro input requerido.

## Exemplo
Um tool de reserva solicita confirmação por elicitation, recebe `requestState` que codifica seu trabalho pendente e devolve input requerido. Depois do usuário aceitar, o cliente repete `tools/call` com a resposta e o estado opaco, usando novo ID; o servidor confere novamente os parâmetros e finaliza a reserva.

## Limites e trade-offs
MRTR não é uma sessão de navegador nem autorização implícita. Só os métodos enumerados pela especificação podem devolver input requerido. O estado continua controlado pelo servidor; não reutilize uma resposta antiga para outro método ou outro conjunto de argumentos sem validação.

## Como verificar
Teste respostas aceitas, recusadas e canceladas; altere deliberadamente uma chave, o `requestState` e o ID na repetição. Confirme que o servidor rejeita estado inválido e que duas instâncias podem processar as duas etapas sem afinidade de sessão.

## Conexões
- [[mcp-meta-protocolo-capacidades-por-request]] — MCP 2026: carregar versão e capacidades em _meta por request.
- [[mcp-cache-ttl-scope-e-invalidacao]] — MCP: combinar ttlMs, cacheScope e notificações de invalidação.

## Fontes
- [MCP 2026-07-28 — Multi Round-Trip Requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) — define `InputRequiredResult`, mapas de input e caráter opaco de `requestState` Consulta: 2026-10-04.
- [MCP 2026-07-28 — Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — mostra a repetição concreta de `tools/call` com novo ID e inputResponses Consulta: 2026-10-04.
