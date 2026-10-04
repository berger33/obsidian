---
id: software.seguranca.tranche20.001906
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

# SLSA: Endurecer plataforma de build

## Em uma frase
**SLSA — Endurecer plataforma de build:** Níveis mais altos impõem garantias adicionais ao controle e isolamento do ambiente de build.

## Por que importa
O recorte de **endurecer plataforma de build** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **endurecer plataforma de build**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use executor isolado por job e limite credenciais acessíveis durante compilação de teste. Teste em staging autorizado.

## Limites e trade-offs
Runner compartilhado ou token amplo pode permitir alteração de artefatos ou provenance. Exceções exigem responsável e prazo.

## Como verificar
Inspecione privilégio, persistência do workspace e acesso a credenciais no executor. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-manter-proveniencia-completa-de-materiais]] — Complementa o tópico com slsa: manter proveniência completa de materiais.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
