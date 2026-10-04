---
id: software.seguranca.tranche20.001909
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

# SLSA: Verificar provenance na implantação

## Em uma frase
**SLSA — Verificar provenance na implantação:** Política de consumo pode validar que artefato foi produzido por builder e source revision aceitos.

## Por que importa
O recorte de **verificar provenance na implantação** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificar provenance na implantação**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em staging, bloqueie imagem se repository, workflow ou digest não corresponderem à allowlist. Teste em staging autorizado.

## Limites e trade-offs
Verificação só no CI pode ser contornada por canal alternativo de implantação. Exceções exigem responsável e prazo.

## Como verificar
Demonstre bloqueio no último ponto de entrada antes de executar o artefato. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-tratar-mudanca-de-pipeline-como-mudanca-de-confianca]] — Complementa o tópico com slsa: tratar mudança de pipeline como mudança de confiança.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
