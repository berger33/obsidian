---
id: software.seguranca.tranche15.001419
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

# Atestação em Bordas Restritas e Atrás de NAT/Firewalls: **Push Mode Attestation (`keylime-push-model-agent`)** vs. Modelo Pull Clássico no Keylime

## Em uma frase
No modelo clássico (*Pull Model*) do Keylime, o `Keylime Verifier` central abre conexões HTTPS mTLS de entrada para a porta `:9002` de cada `keylime_agent` a cada 2 segundos para pedir a cotação `TPM2_Quote`. Mas e quando os seus dispositivos de **Edge Computing, Caixas Eletrônicos, Veículos Conectados ou Gateways Industriais** estão atrás de **NAT, CGNAT 4G/5G ou Firewalls estritos que bloqueiam 100% das conexões de entrada**?

## Por que importa
O projeto **`rust-keylime`** desenvolveu o **`keylime-push-model-agent` (*Push Attestation Model*)**!

## Como funciona
No **Push Model**: o agente em Rust na ponta **não precisa abrir nenhuma porta TCP de escuta (`Zero Inbound Ports`)**! Em vez de esperar o Verifier conectá-lo, o próprio agente abre periodicamente uma conexão HTTPS mTLS de saída para o `Verifier`, obtém os parâmetros de desafio/frescor e **empurra (*pushes*) a cotação assinada pelo TPM 2.0 (`TPM2_Quote`), o log UEFI e as novas medições do Linux IMA para o Verifier**!

## Exemplo
```bash
# Verificar no repositorio/pacote rust-keylime o binario de atestacao ativa de saida (keylime_push_model_agent) para dispositivos Edge atras de NAT
keylime_push_model_agent --help || keylime_agent --version
```

## Limites e trade-offs
Se um dispositivo em **Push Mode** for comprometido e o invasor bloquear o envio das mensagens de saída do agente (tentando esconder uma medição maliciosa no `PCR 10`), como o `Verifier` descobre? Pelo **Heartbeat Timeout de Atestação**: se o `Verifier` não receber uma cotação válida e fresca assinada pela `AK` do TPM daquele agente dentro da janela máxima esperada, o `Verifier` marca o agente como **`Failed / Unreachable`** e aciona imediatamente o webhook de revogação!

## Como verificar
Além de atravessar NAT e firewalls sem abrir portas de entrada, o **Push Model** melhora drasticamente a escalabilidade de um cluster `Verifier` atrás de Load Balancers HTTP/gRPC stateless!

## Conexões
- [[keylime-configuracao-segura-mtls-verifier-registrar-banco-postgresql-ha]] — Veja também: Hardening e Escalabilidade em Produção do Keylime: **mTLS Obrigatório (`trusted_client_ca`)**, Banco **PostgreSQL HA** e Configuração do **`rust-keylime` (`/etc/keylime/agent.conf`)**.
- [[keylime-atestacao-containers-kubernetes-spire-confidential-computing]] — Veja também: Integração do Keylime com **Kubernetes, SPIFFE/SPIRE (`node-attestor`) e Confidential Computing (AMD SEV-SNP / Intel TDX vTPM)**: Zero-Trust Ancorado no Silício.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust]] — Referência cruzada direta com keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust.
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Referência cruzada direta com teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
