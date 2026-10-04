---
id: software.seguranca.tranche20.001901
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

# SLSA: Entender níveis de garantia de build

## Em uma frase
**SLSA — Entender níveis de garantia de build:** Níveis SLSA organizam requisitos crescentes sobre geração e proteção da proveniência de build.

## Por que importa
O recorte de **entender níveis de garantia de build** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **entender níveis de garantia de build**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Classifique pipeline atual por evidências observáveis antes de prometer um nível de garantia. Teste em staging autorizado.

## Limites e trade-offs
Nível não é pontuação de qualidade e não mede todas as ameaças do produto. Exceções exigem responsável e prazo.

## Como verificar
Associe cada requisito do nível a configuração, log ou atestação verificável. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-gerar-provenance-ligada-ao-artefato]] — Complementa o tópico com slsa: gerar provenance ligada ao artefato.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
