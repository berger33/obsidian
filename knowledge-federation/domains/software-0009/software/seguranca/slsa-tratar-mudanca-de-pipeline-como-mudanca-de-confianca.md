---
id: software.seguranca.tranche20.001910
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

# SLSA: Tratar mudança de pipeline como mudança de confiança

## Em uma frase
**SLSA — Tratar mudança de pipeline como mudança de confiança:** Alterações em workflow, builder ou definição de materiais mudam as garantias associadas ao artefato.

## Por que importa
O recorte de **tratar mudança de pipeline como mudança de confiança** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar mudança de pipeline como mudança de confiança**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exija revisão de segurança para mudanças no workflow que assina ou gera provenance de release. Teste em staging autorizado.

## Limites e trade-offs
Branch protection insuficiente permite que código altere sua própria identidade de produtor. Exceções exigem responsável e prazo.

## Como verificar
Compare revision do workflow com política de release e guarde proveniência de cada publicação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-separar-papeis-root-targets-snapshot-e-timestamp]] — Complementa o tópico com the update framework (tuf): separar papéis root, targets, snapshot e timestamp.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
