---
id: software.criacao_ia.tranche04.000307
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://www.w3.org/TR/webgpu/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: declarar cada uso de textura no momento certo

## Em uma frase
Flags de uso de textura são cumulativas e imutáveis: cada papel — amostragem, anexo de render, destino de cópia — precisa ser declarado na criação.

## Por que importa
O hardware organiza memória por intenção de uso; a WebGPU expõe isso como contrato. Esquecer TEXTURE_BINDING faz o shader não conseguir amostrar; esquecer RENDER_ATTACHMENT invalida o pipeline; e toda flag adicionada pode custar layout de memória maior. A falha aparece tarde se a validação não for monitorada.

## Como funciona
No GPUTextureDescriptor, componha usage: TEXTURE_BINDING para leitura no shader, RENDER_ATTACHMENT para render passes, COPY_DST quando writeTexture ou copyExternalImageToTexture alimentam o recurso, e STORAGE_BINDING apenas para escrita (o estágio não lê uma storage texture sem formato read-write apropriado). Para ler um anexo de profundidade depois, crie a textura com TEXTURE_BINDING adicional e declare viewFormats coerentes no render pass. Prefira a menor combinação de flags que o frame exige.

## Exemplo
Um passes de sombra escreve num depth texture com RENDER_ATTACHMENT | TEXTURE_BINDING e viewFormats contendo o formato read para sampling; o pass principal amostra a mesma textura para PCF.

## Limites e trade-offs
Multisample não combina com STORAGE_BINDING e formatos de armazenamento carregáveis limitam o par TEXTURE_BINDING+STORAGE. Recriar uma textura para trocar de uso implica alocar de novo — desenhe o conjunto de flags por estágio desde o início. Os formatos suportados variam por plataforma; o desc apenas define o espaço de formatos.

## Como verificar
Ative um error scope de validação e remova intencionalmente uma flag esperada: a descrição do pipeline deve falhar com mensagem apontando o uso. Rode o mesmo código em outra GPU e confirme a compatibilidade do formato escolhido. Audite o conjunto de flags de cada textura listando as criadas no carregamento.

## Conexões
- [[webgpu-mappedatcreation-dado-inicial]] — WebGPU: mappedAtCreation para dados iniciais sem cópia adicional.
- [[webgpu-bindgrouplayout-compatibilidade]] — WebGPU: bind groups só valem se o layout for compatível com o pipeline.

## Fontes
- [W3C — WebGPU: GPUTexture](https://www.w3.org/TR/webgpu/) — define as flags de uso de textura e as regras por formato Consulta: 2026-10-04.
- [MDN — GPUBindGroup](https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup) — contextualiza o binding de textura amostrável que exige TEXTURE_BINDING Consulta: 2026-10-04.
