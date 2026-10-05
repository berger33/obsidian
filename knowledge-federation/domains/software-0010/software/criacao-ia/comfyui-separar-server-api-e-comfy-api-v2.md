---
id: software.criacao_ia.tranche05.000420
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://docs.comfy.org/development/comfy-api/overview.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: separar a Server API da superfície versionada Comfy API v2

## Em uma frase
As rotas HTTP/WebSocket do ComfyUI Server e a Comfy API v2 são contratos distintos; a v2 também pode acessar instalações open-source por meio do API Proxy.

## Por que importa
Misturar interfaces pode levar a base URL, autenticação e payloads errados, mesmo quando ambas iniciam workflows no ecossistema ComfyUI.

## Como funciona
Use a documentação de Server Routes para chamadas diretas ao processo, como `/prompt` e `/ws`. A visão geral oficial descreve Comfy API v2 como API versionada para open-source via API Proxy, Comfy Cloud e deployments; a antiga Cloud API v1 está depreciada. Escolha host, credenciais e formato a partir da superfície efetivamente configurada.

## Exemplo
Um aplicativo conectado ao servidor instalado usa as rotas diretas documentadas; uma integração que adota Comfy API v2 segue o contrato e a autenticação dessa versão, mesmo quando o alvo open-source é alcançado por proxy.

## Limites e trade-offs
A depreciação citada pela documentação é da antiga Cloud API v1; ela não declara obsoletas as rotas diretas do Server API. Tampouco significa que a API v2 seja apenas um produto cloud.

## Como verificar
Registre em configuração qual interface está ativa e teste host, autenticação e payload com um workflow pequeno; mantenha testes separados para rotas diretas e Comfy API v2 se ambos forem suportados.

## Conexões
- [[comfyui-api-upload-image-referencia]] — ComfyUI: usar a referência devolvida por upload/image em vez de caminho local.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Define as rotas HTTP e WebSocket embutidas no servidor, incluindo prompt, fila e histórico. Consulta: 2026-10-04.
- [Comfy API — Overview](https://docs.comfy.org/development/comfy-api/overview.md) — Descreve a superfície versionada v2, onde ela está disponível e que a antiga Cloud API v1 está depreciada. Consulta: 2026-10-04.
