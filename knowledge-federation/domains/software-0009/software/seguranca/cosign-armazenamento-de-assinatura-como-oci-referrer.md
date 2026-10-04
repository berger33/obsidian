---
id: software.seguranca.tranche17.001635
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://docs.sigstore.dev/cosign/overview/", "https://docs.sigstore.dev/cosign/verifying/verify/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Cosign: Armazenamento de assinatura como OCI referrer

## Em uma frase
**Sigstore Cosign — Armazenamento de assinatura como OCI referrer:** Assinaturas associadas ao registry precisam permanecer ligadas à referência correta e recuperáveis para verificação.

## Por que importa
O recorte de **armazenamento de assinatura como oci referrer** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **armazenamento de assinatura como oci referrer**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inspecione a árvore de referrers do digest de release e confirme a presença de assinatura em um registry de teste. Teste em staging autorizado.

## Limites e trade-offs
Comportamento de exclusão, retenção e replicação depende do registry; uma assinatura pode não acompanhar cópias incompletas. Exceções exigem responsável e prazo.

## Como verificar
Teste mirror e garbage collection com um artefato descartável antes de confiar na distribuição. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-atestacao-de-metadados-de-build]] — Complementa o tópico com sigstore cosign: atestação de metadados de build.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
