---
id: software.criacao_ia.tranche04.000306
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer/mappedAtCreation", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: mappedAtCreation para dados iniciais sem cópia adicional

## Em uma frase
Buffers criados com mappedAtCreation nascem mapeados para escrita, permitindo preencher o conteúdo antes de qualquer submissão à fila.

## Por que importa
Sem essa via, o dado inicial de geometria, índices ou uniforms exigiria um staging com MAP_WRITE, cópia e limpeza — três operações a mais no setup. O caminho direto reduz código e picos de memória em cenas com muitos recursos carregados na inicialização.

## Como funciona
Passe mappedAtCreation: true no dicionário de criação; o uso não pode incluir MAP_READ nem MAP_WRITE, porque o estado de escrita é garantido pela flag. Escreva no ArrayBuffer de getMappedRange (por exemplo, via Float32Array), chame unmap() para efetivar e, só então, submeta passes que leem o buffer. Depois do primeiro unmap, o buffer fica imutável para o CPU; atualizações seguintes exigem queue.writeBuffer ou cópias.

## Exemplo
O carregador de malha monta Float32Array com posições e UVs, cria o vertex buffer com mappedAtCreation, copia o array para o range mapeado e dá unmap antes de criar os bind groups que o referenciam.

## Limites e trade-offs
O preenchimento ocorre no thread principal durante a criação — para dados de MB, isso trava frames se feito em massa. Texturas não têm equivalente direto; dados de imagem passam por copyExternalImageToTexture ou buffers. Se esquecer o unmap, qualquer uso subsequente no encoder é erro de validação.

## Como verificar
Escreva um padrão determinístico, crie o buffer, leia o resultado de volta com o fluxo staging e compare byte a byte. Adicione um uso indevido (MAP_WRITE junto com mappedAtCreation) e confirme a rejeição com mensagem clara. Meça o custo de criação para o maior buffer da sua cena.

## Conexões
- [[webgpu-leitura-gpu-staging-buffer]] — WebGPU: ler dados da GPU exige buffer staging com MAP_READ.
- [[webgpu-textureusage-views-permitidos]] — WebGPU: declarar cada uso de textura no momento certo.

## Fontes
- [MDN — GPUBuffer: mappedAtCreation](https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer/mappedAtCreation) — descreve o estado inicial mapeado e a restrição de flags Consulta: 2026-10-04.
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — define a criação de buffer com criação-mapeada como caminho normativo de dados iniciais Consulta: 2026-10-04.
