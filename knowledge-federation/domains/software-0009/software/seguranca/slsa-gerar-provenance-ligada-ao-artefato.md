---
id: software.seguranca.tranche20.001902
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://slsa.dev/spec/v1.0/", "https://slsa.dev/spec/v1.0/levels"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SLSA: Gerar provenance ligada ao artefato

## Em uma frase
**SLSA — Gerar provenance ligada ao artefato:** Build provenance descreve relação entre artefato, processo de build e materiais usados.

## Por que importa
O recorte de **gerar provenance ligada ao artefato** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gerar provenance ligada ao artefato**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Produza provenance para binário de teste no mesmo job que publica seu digest imutável. Teste em staging autorizado.

## Limites e trade-offs
Campo de provenance pode ser declarado incorretamente se o builder não for confiável. Exceções exigem responsável e prazo.

## Como verificar
Confira subject digest, builder, invocation e materiais contra o build real. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-descrever-build-definition]] — Complementa o tópico com slsa: descrever build definition.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
