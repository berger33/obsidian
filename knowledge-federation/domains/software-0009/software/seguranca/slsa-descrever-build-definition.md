---
id: software.seguranca.tranche20.001903
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

# SLSA: Descrever build definition

## Em uma frase
**SLSA — Descrever build definition:** Build definition identifica parâmetros e dependências que influenciaram a produção do artefato.

## Por que importa
O recorte de **descrever build definition** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **descrever build definition**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Registre source revision e parâmetros não secretos de compilação em provenance de laboratório. Teste em staging autorizado.

## Limites e trade-offs
Parâmetros omitidos tornam difícil reproduzir ou comparar dois builds. Exceções exigem responsável e prazo.

## Como verificar
Compare definição declarada com comando e contexto executados pela pipeline. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-validar-origem-e-identidade-do-builder]] — Complementa o tópico com slsa: validar origem e identidade do builder.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
