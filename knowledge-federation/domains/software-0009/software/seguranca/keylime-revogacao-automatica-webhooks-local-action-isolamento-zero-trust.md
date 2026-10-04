---
id: software.seguranca.tranche15.001417
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

# Resposta Automática a Incidentes (**Revocation Framework**) no Keylime: Isolando Nós Comprometidos em Segundos via **Webhooks**, **ZeroMQ** e Scripts **`local_action_*`**

## Em uma frase
O que acontece no exato segundo em que o **`Keylime Verifier`** detecta que um servidor monitorado falhou na atestação (por exemplo: alguém executou um binário não autorizado que alterou o `PCR 10` do IMA, ou o agente parou de responder cotações válidas)?

## Por que importa
O Keylime aciona imediatamente seu **Framework de Revogação Automática (`Revocation Notifier`)**!

## Como funciona
A revogação no Keylime opera em **duas frentes simultâneas**: **(1) Notificação Externa via `Webhook` HTTPS (ou barramento `ZeroMQ`)** — o `Verifier` envia uma mensagem JSON assinada criptograficamente com o evento de falha (`revocation` com `agent_id`, `ip`, `failure_reason`, `context`) para o seu plano de controle de rede/orquestração (por exemplo, um webhook que instrui o **Kubernetes** a fazer `kubectl cordon`/`drain` e revogar os certificados mTLS do nó no **Teleport / Cilium / Istio / Firewall**, impedindo que a máquina comprometida continue acessando o banco de dados!); e **(2) Ações Locais (`local_action_*`) nos demais agentes saudáveis da frota** (ex.: removendo automaticamente o IP ou o certificado da máquina comprometida da tabela `/etc/hosts`, `ipsec` ou `authorized_keys` dos vizinhos)!

## Exemplo
```ini
# Configurar no /etc/keylime/verifier.conf o envio automatico de eventos de revogacao via Webhook HTTPS quando qualquer agente falhar na atestacao
[verifier]
enabled_revocation_notifications = ['agent', 'webhook']
webhook_url = https://soar-interno.exemplo.br/api/v1/keylime/revocation
```

## Limites e trade-offs
Por que você nunca deve depender **apenas** de uma ação executada dentro da própria máquina comprometida para isolá-la quando a atestação falha? Porque se a atestação falhou, significa que o Kernel ou o espaço de usuário daquela máquina já pode estar sob controle de um invasor (que poderia bloquear o script local de desligamento)! Por isso, a arquitetura recomendada do Keylime usa o **`webhook_url` externo do Verifier** (ou os scripts `local_action_*` rodando nos **outros nós saudáveis**) para cortar o acesso da máquina comprometida de fora para dentro!

## Como verificar
Monitore os eventos de falha de atestação com **`keylime_tenant -c cvstatus -u <agent_uuid>`**, que retorna o estado operacional (`Get Quote`, `Tenant Quote Failed`, `Invalid Quote`) de cada agente.

## Conexões
- [[keylime-atestacao-measured-boot-uefi-eventlog-elchecking-politicas]] — Veja também: Atestação de **Measured Boot UEFI (`binary_bios_measurements`)** e Políticas de Firmware/Secure Boot (`--mb_refstate`) no Keylime.
- [[keylime-configuracao-segura-mtls-verifier-registrar-banco-postgresql-ha]] — Veja também: Hardening e Escalabilidade em Produção do Keylime: **mTLS Obrigatório (`trusted_client_ca`)**, Banco **PostgreSQL HA** e Configuração do **`rust-keylime` (`/etc/keylime/agent.conf`)**.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Referência cruzada direta com keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
