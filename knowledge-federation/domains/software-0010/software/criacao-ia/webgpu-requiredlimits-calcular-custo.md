---
id: software.criacao_ia.tranche04.000303
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits", "https://www.w3.org/TR/webgpu/#limits"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: pedir limites maiores e calcular antes do limite suportado

## Em uma frase
Limites são uma negociação: a aplicação declara o que precisa via requiredLimits e deve ler device.limits depois, pois valores variam por hardware.

## Por que importa
Os valores-padrão da especificação (por exemplo, dimensão máxima 8192 em texturas 2D e 64 KiB por binding uniform) são o mínimo que toda implementação deve oferecer. Um motor que assume o teto da própria placa de desenvolvimento quebra em máquinas menores, e o custo de um limite elevado recai sobre toda a cena.

## Como funciona
Compare seu plano de recursos com adapter.limits antes de chamar requestDevice; inclua apenas o que o código realmente exige, pois limites elevados podem ser recusados ou aumentar o custo de alocação. Depois da criação, use device.limits — a interseção do pedido com o suporte — como verdade para a lógica de alocação: tamanho máximo de buffer, número de cores por amostra, trabalho por grupo. Escreva o código de forma que reduza resoluções e lotes quando um limite menor for retornado.

## Exemplo
Um atlas virtual exige buffer maior que 256 MB (padrão de maxBufferSize)? Verifique adapter.limits.maxBufferSize e, se não suportar, divida em sub-buffers com cópias por encadeamento de passes, em vez de pedir um limite gigante e falhar a criação do dispositivo.

## Limites e trade-offs
Pedir limites acima do suportado faz requestDevice rejeitar; não há concessão parcial silenciosa de valores maiores. Limites cobrem capacidade declarada, não orçamento de memória do sistema — alocar até o máximo suportado ainda pode falhar por pressão de memória.

## Como verificar
Leia adapter.limits e device.limits na mesma execução e confirme a interseção. Force um requiredLimits absurdo (por exemplo, maxTextureDimension2D acima do suportado) e observe a rejeição. Rode a aplicação em GPU de entrada e na placa de desenvolvimento, ativando o caminho de redução de lotes quando os limites caírem.

## Conexões
- [[webgpu-devicelost-camada-recuperacao]] — WebGPU: tratar device lost como fronteira de recuperação.
- [[webgpu-features-antes-dependencia]] — WebGPU: features são opcionais e viram dependência de plataforma.

## Fontes
- [MDN — GPUSupportedLimits](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits) — lista os membros de limite e seus valores-padrão Consulta: 2026-10-04.
- [W3C — WebGPU: seção Limits](https://www.w3.org/TR/webgpu/#limits) — define os limites normativos e as regras de requiredLimits Consulta: 2026-10-04.
