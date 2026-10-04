---
id: software.seguranca.tranche20.001907
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

# SLSA: Manter proveniência completa de materiais

## Em uma frase
**SLSA — Manter proveniência completa de materiais:** Lista de materiais conecta build a commit, dependências e outras entradas relevantes.

## Por que importa
O recorte de **manter proveniência completa de materiais** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **manter proveniência completa de materiais**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inclua commit e referências resolvidas de dependências em artefato de release controlado. Teste em staging autorizado.

## Limites e trade-offs
Provenance incompleta pode omitir entrada que influenciou o resultado. Exceções exigem responsável e prazo.

## Como verificar
Reconcilie materiais declarados com lockfiles e etapas efetivas do build. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-interpretar-nivel-sem-declarar-software-seguro]] — Complementa o tópico com slsa: interpretar nível sem declarar software seguro.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
