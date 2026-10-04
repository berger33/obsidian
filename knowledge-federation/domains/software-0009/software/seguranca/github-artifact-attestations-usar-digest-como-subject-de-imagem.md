---
id: software.seguranca.tranche20.001942
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

# GitHub Artifact Attestations: Usar digest como subject de imagem

## Em uma frase
**GitHub Artifact Attestations — Usar digest como subject de imagem:** Attestation de container precisa apontar para digest imutável em vez de depender de tag móvel.

## Por que importa
O recorte de **usar digest como subject de imagem** ajuda a ligar artefato publicado a workflow, repositório e identidade verificáveis antes de distribuição. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar digest como subject de imagem**, workflow autorizado cria attestation com subject digest e provenance; consumidores consultam e validam claims pelo CLI. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Publique imagem por digest e gere provenance para a referência exata. Teste em staging autorizado.

## Limites e trade-offs
Tag reatribuída pode apontar a bytes diferentes daqueles cobertos pela attestation. Exceções exigem responsável e prazo.

## Como verificar
Verifique digest do registry e subject reportado pelo `gh attestation verify`. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[github-artifact-attestations-limitar-permissoes-do-workflow-produtor]] — Complementa o tópico com github artifact attestations: limitar permissões do workflow produtor.

## Fontes
- [GitHub Docs — Artifact attestations for builds](https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds) — guia oficial de geração de provenance para builds e containers; consultado em 2026-10-04.
- [GitHub CLI — gh attestation verify](https://cli.github.com/manual/gh_attestation_verify) — referência oficial de verificação de attestations e opções de identidade e source; consultado em 2026-10-04.
