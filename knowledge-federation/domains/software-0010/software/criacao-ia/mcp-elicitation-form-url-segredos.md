---
id: software.criacao_ia.tranche03.000218
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation", "https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP elicitation: reservar URL mode para credenciais e segredos

## Em uma frase
Elicitation form coleta campos estruturados dentro do cliente MCP; URL mode encaminha uma interação sensível para fora dele.

## Por que importa
Formulários são úteis para contexto e parâmetros comuns, mas expor credenciais em trânsito pelo cliente amplia a superfície de armazenamento e logging. O protocolo define uma separação obrigatória para segredos e requer que o usuário consiga entender quem pede os dados e para onde irá ao sair do cliente.

## Como funciona
Declare `form` e/ou `url` nas capacidades do cliente por request. Use `requestedSchema` restrito para dados estruturados não secretos e permita revisar, editar, recusar ou cancelar antes de enviar. Senhas, API keys, access tokens e credenciais de pagamento não podem ser solicitados por form mode; o servidor precisa usar URL mode, cujo domínio o cliente exibe e para cuja navegação obtém consentimento.

## Exemplo
Um servidor pode perguntar o nome de um workspace num formulário simples. Para conectar uma conta de nuvem, ele devolve uma URL de login do provedor; o cliente identifica o host e pede confirmação, e os campos secretos são digitados no fluxo externo em vez de retornarem como resposta do formulário MCP.

## Limites e trade-offs
URL mode não autentica automaticamente o destino nem garante que a navegação externa seja legítima. Clientes devem validar exibição de domínio e aplicar defesas contra redirecionamentos enganosos. Campos pessoais comuns não são proibidos categoricamente, mas precisam de revisão e opção de recusa.

## Como verificar
Teste schemas não suportados, capability ausente, recusa do usuário, host externo inesperado e tentativa de solicitar um token em form mode. Inspecione logs para garantir que conteúdo sensível não é registrado no caminho MCP.

## Conexões
- [[mcp-prompts-selecao-controlada-pelo-usuario]] — MCP prompts: distinguir seleção do usuário e autoria do servidor.
- [[mcp-oauth-discovery-e-client-registration]] — MCP HTTP OAuth: descobrir recurso protegido e registrar cliente.

## Fontes
- [MCP 2026-07-28 — Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) — define modos form/URL, segredos proibidos em form e consentimento de navegação Consulta: 2026-10-04.
- [MCP 2026-07-28 — Multi Round-Trip Requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) — descreve como elicitation é transportada em inputRequests e respondida pelo cliente Consulta: 2026-10-04.
