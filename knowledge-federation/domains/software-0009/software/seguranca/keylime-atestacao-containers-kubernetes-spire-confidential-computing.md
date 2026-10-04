---
id: software.seguranca.tranche15.001420
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/keylime/keylime/master/README.md", "https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração do Keylime com **Kubernetes, SPIFFE/SPIRE (`node-attestor`) e Confidential Computing (AMD SEV-SNP / Intel TDX vTPM)**: Zero-Trust Ancorado no Silício

## Em uma frase
Como unir a **Atestação de Hardware e Runtime do Keylime** ao ecossistema Cloud-Native moderno (**Kubernetes, Service Mesh Istio/Cilium com SPIFFE/SPIRE e Máquinas Virtuais Confidenciais `Confidential VMs`**)?

## Por que importa
O Keylime atua como o **Provedor de Confiança de Hardware (*Hardware Root-of-Trust Attestor*)** para toda a pilha Cloud-Native em três padrões de arquitetura: **(1) Integração `SPIFFE / SPIRE` + Keylime** — o `SPIRE Server` só emite e renova o certificado de identidade `SVID` de um nó do Kubernetes (`spire-agent`) enquanto o `Keylime Verifier` confirmar que o `TPM 2.0` e o `IMA (PCR 10)` daquele nó estão íntegros; se o Keylime detectar execução de binário não autorizado no host K8s, o SPIRE revoga a identidade do nó e o Service Mesh corta o mTLS instantaneamente!.

## Como funciona
**(2)Monitoramento de Imagens de Containers via IMA Namespaces / `fs-verity`**; e **(3) Confidential Computing (AMD SEV-SNP / Intel TDX com `vTPM` protegido em memória cifrada)**!

## Exemplo
```bash
# Consultar via API/CLI do Keylime o status consolidado de atestacao de todos os nos do cluster Kubernetes registrados no Verifier
keylime_tenant -c cvlist
keylime_tenant -c cvstatus -u d432fbb3-d2f1-4a97-9ef7-75bd81c00000
```

## Limites e trade-offs
Por que essa integração **Keylime + SPIFFE/SPIRE (ou Teleport)** fecha a maior lacuna das arquiteturas Zero-Trust tradicionais baseadas apenas em mTLS de software? Porque o mTLS comum prova apenas que a máquina possui uma chave privada na memória, mas **não prova se a máquina que possui aquela chave foi infectada por um rootkit ou binário trojanizado**; com o **Keylime + TPM 2.0 + IMA**, a identidade na rede está condicionada continuamente à **integridade verificada do software em execução**!

## Como verificar
Sempre teste todo o fluxo de registro, provisionamento, falha de atestação (`cp /bin/ls /tmp/ls_nao_autorizado && /tmp/ls_nao_autorizado`) e revogação automática em ambiente de homologação com `swtpm` antes do rollout em produção.

## Conexões
- [[keylime-modelo-push-attestation-edge-nat-firewalls-escalabilidade]] — Veja também: Atestação em Bordas Restritas e Atrás de NAT/Firewalls: **Push Mode Attestation (`keylime-push-model-agent`)** vs. Modelo Pull Clássico no Keylime.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust]] — Referência cruzada direta com keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust.
- [[tpm2-simulacao-testes-ci-cd-swtpm-tcti-qemu-vtpm-containers]] — Referência cruzada direta com tpm2-simulacao-testes-ci-cd-swtpm-tcti-qemu-vtpm-containers.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
