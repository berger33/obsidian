---
id: software.seguranca.tranche20.001944
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
fontes: ["https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds", "https://cli.github.com/manual/gh_attestation_verify"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# GitHub Artifact Attestations: Verificar repository e workflow de origem

## Em uma frase
**GitHub Artifact Attestations — Verificar repository e workflow de origem:** Consumidor pode restringir qual repository e workflow assinaram a attestation.

## Por que importa
O recorte de **verificar repository e workflow de origem** ajuda a ligar artefato publicado a workflow, repositório e identidade verificáveis antes de distribuição. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificar repository e workflow de origem**, workflow autorizado cria attestation com subject digest e provenance; consumidores consultam e validam claims pelo CLI. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Verifique artefato de staging exigindo owner e source workflow definidos. Teste em staging autorizado.

## Limites e trade-offs
Confiar em qualquer identidade GitHub Actions aceita origem controlada por terceiro. Exceções exigem responsável e prazo.

## Como verificar
Teste attestation válida de repo diferente e confirme rejeição. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[github-artifact-attestations-inspecionar-tipo-de-predicate]] — Complementa o tópico com github artifact attestations: inspecionar tipo de predicate.

## Fontes
- [GitHub Docs — Artifact attestations for builds](https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds) — guia oficial de geração de provenance para builds e containers; consultado em 2026-10-04.
- [GitHub CLI — gh attestation verify](https://cli.github.com/manual/gh_attestation_verify) — referência oficial de verificação de attestations e opções de identidade e source; consultado em 2026-10-04.
