---
id: software.seguranca.tranche20.001947
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

# GitHub Artifact Attestations: Separar verificação de artifact e identidade

## Em uma frase
**GitHub Artifact Attestations — Separar verificação de artifact e identidade:** Validação precisa ligar bytes do subject à attestation e validar identidade esperada do produtor.

## Por que importa
O recorte de **separar verificação de artifact e identidade** ajuda a ligar artefato publicado a workflow, repositório e identidade verificáveis antes de distribuição. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar verificação de artifact e identidade**, workflow autorizado cria attestation com subject digest e provenance; consumidores consultam e validam claims pelo CLI. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use fixture alterada e attestation de outra origem para testar ambos os checks. Teste em staging autorizado.

## Limites e trade-offs
Assinatura válida sem vínculo ao digest ou identidade pode ser inadequada. Exceções exigem responsável e prazo.

## Como verificar
Confirme que mudar digest e signer, separadamente, falha na verificação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[github-artifact-attestations-acompanhar-acesso-publico-e-retencao]] — Complementa o tópico com github artifact attestations: acompanhar acesso público e retenção.

## Fontes
- [GitHub Docs — Artifact attestations for builds](https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds) — guia oficial de geração de provenance para builds e containers; consultado em 2026-10-04.
- [GitHub CLI — gh attestation verify](https://cli.github.com/manual/gh_attestation_verify) — referência oficial de verificação de attestations e opções de identidade e source; consultado em 2026-10-04.
