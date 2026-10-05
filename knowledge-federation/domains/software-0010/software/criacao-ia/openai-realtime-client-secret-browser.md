---
id: software.criacao_ia.tranche05.000450
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
fontes: ["https://developers.openai.com/api/reference/resources/realtime/subresources/client_secrets/methods/create", "https://developers.openai.com/api/docs/guides/realtime"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime: usar client secret temporário no browser em vez da API key principal

## Em uma frase
Um client secret de curta duração permite iniciar sessão Realtime em cliente web ou móvel sem expor a chave de projeto permanente.

## Por que importa
Código distribuído ao browser pode ser inspecionado pelo usuário; incluir nele a credencial principal permite reutilização fora do escopo e controle do serviço.

## Como funciona
O servidor confiável cria o client secret e associa configuração de sessão; entrega somente esse token limitado ao cliente e mantém a API key principal no backend. Escolha TTL apropriado e não grave o segredo em logs públicos.

## Exemplo
O backend autentica a pessoa, chama a criação de client secret com o modelo e áudio permitidos e devolve o token efêmero para o navegador abrir sua conexão Realtime.

## Limites e trade-offs
A validade do secret controla criação de sessões; a documentação observa que uma sessão já iniciada pode continuar após expiração. Proteja também endpoint de emissão e limite sessões por usuário.

## Como verificar
Inspecione bundle e tráfego do browser para garantir que a chave principal nunca aparece; teste expiração do token, sessão existente e recusa de usuário não autenticado.

## Conexões
- [[openai-realtime-session-update-estado-efetivo]] — OpenAI Realtime: tratar session.updated como confirmação do estado efetivo.

## Fontes
- [OpenAI Realtime — Create client secret](https://developers.openai.com/api/reference/resources/realtime/subresources/client_secrets/methods/create) — Define tokens curtos para clientes e sua finalidade de não expor a chave principal. Consulta: 2026-10-04.
- [OpenAI Realtime — Getting started](https://developers.openai.com/api/docs/guides/realtime) — Mostra o servidor criando credencial efêmera antes da conexão do frontend. Consulta: 2026-10-04.
