---
id: software.criacao_ia.tranche05.000419
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/server.py"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: usar a referência devolvida por upload/image em vez de caminho local

## Em uma frase
`POST /upload/image` recebe um arquivo e devolve `name`, `subfolder` e `type`, valores que o cliente pode encaminhar ao nó de entrada apropriado.

## Por que importa
Um caminho como `~/Pictures/input.png` existe apenas no ambiente que o digitou e não é acessível de forma confiável pelo processo remoto ou container ComfyUI.

## Como funciona
Envie o arquivo como multipart para `/upload/image`, examine a resposta JSON e use os campos retornados ao preencher a entrada do workflow. Preserve o `type` e a subpasta reportados em vez de construir um caminho do computador do usuário.

## Exemplo
Um cliente web envia a imagem de referência, guarda o `name`, `subfolder` e `type` devolvidos e preenche a entrada `LoadImage` antes de enviar o grafo para `/prompt`.

## Limites e trade-offs
O endpoint não valida se a imagem tem dimensão, modo de cor ou conteúdo aceito pelo nó; aplique limites de tamanho e formato. `/upload/mask` é um fluxo especializado que recebe `original_ref` e altera o alpha de uma imagem existente, não um upload genérico de máscara.

## Como verificar
Teste imagem com e sem subpasta, colisão de nome e arquivo inválido; confira a resposta e confirme que o workflow lê a referência devolvida. Teste `/upload/mask` separadamente apenas quando houver uma referência original válida.

## Conexões
- [[comfyui-api-distinguir-fila-de-interrupt]] — ComfyUI: separar controle da fila de interrupção da execução ativa.
- [[comfyui-separar-server-api-e-comfy-api-v2]] — ComfyUI: separar a Server API da superfície versionada Comfy API v2.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Lista separadamente os endpoints de upload de imagem, upload de máscara e a rota de submissão. Consulta: 2026-10-04.
- [ComfyUI Server — server.py upload implementation](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/server.py) — Implementa a resposta JSON com `name`, `subfolder` e `type`, além do tratamento específico de `original_ref` em upload/mask. Consulta: 2026-10-04.
