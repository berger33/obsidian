---
id: software.criacao_ia.tranche05.000417
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://docs.comfy.org/development/comfyui-server/comms_overview.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: consultar object_info para descobrir o esquema dos nós disponíveis

## Em uma frase
`/object_info` permite consultar informações dos tipos de nós reconhecidos pelo servidor atual em vez de tratar o catálogo de nós como universal.

## Por que importa
Workflows dependem de nós padrão e personalizados; comparar o esquema disponível ajuda a diagnosticar incompatibilidade antes de enviar uma fila que não pode ser validada.

## Como funciona
Consulte a rota de informações de nós, globalmente ou para uma classe nomeada conforme a API documentada. Use os dados recebidos para conferir nomes de classes e entradas disponíveis na instalação que executará o workflow.

## Exemplo
Um editor de workflows carrega metadados do servidor de destino, sinaliza uma classe ausente antes do envio e deixa claro quando um nó customizado precisa ser instalado.

## Limites e trade-offs
Metadados de nó descrevem a instalação consultada naquele momento; não garantem comportamento idêntico de extensões de terceiros nem tornam compatíveis todos os pesos, versões e valores.

## Como verificar
Compare a resposta de `/object_info` para um nó padrão e um nó customizado, depois valide o workflow com `/prompt` para cobrir o contrato real de execução.

## Conexões
- [[comfyui-api-view-parametros-de-arquivo]] — ComfyUI: recuperar arquivos de saída pela rota view e seus parâmetros.
- [[comfyui-api-distinguir-fila-de-interrupt]] — ComfyUI: separar controle da fila de interrupção da execução ativa.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Lista rotas object_info para consultar tipos de nós e metadados expostos pelo servidor. Consulta: 2026-10-04.
- [ComfyUI Server — Communication Overview](https://docs.comfy.org/development/comfyui-server/comms_overview.md) — Situa as rotas HTTP como parte da interface de comunicação do servidor ComfyUI. Consulta: 2026-10-04.
