---
id: software.seguranca.tranche15.001418
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

# Hardening e Escalabilidade em Produção do Keylime: **mTLS Obrigatório (`trusted_client_ca`)**, Banco **PostgreSQL HA** e Configuração do **`rust-keylime` (`/etc/keylime/agent.conf`)**

## Em uma frase
Como implantar o **`Keylime Verifier`** e o **`Keylime Registrar`** em produção para monitorar milhares de servidores sem usar o banco SQLite local de demonstração e garantindo que todas as chamadas de API de controle (`keylime_tenant` <-> `Verifier` <-> `Agent`) sejam protegidas por **Autenticação Mútua mTLS**?

## Por que importa
Nos arquivos `/etc/keylime/verifier.conf` e `/etc/keylime/registrar.conf`: **(1) Substitua o `database_url = sqlite` padrão por um cluster `PostgreSQL` de alta disponibilidade** (`database_url = postgresql://keylime_user:SenhaForte@pg-ha.exemplo.br:5432/keylime_db`); **(2) Configure certificados X.509 mTLS dedicados** assinados pela PKI interna da sua empresa (`tls_dir`, `server_key`, `server_cert`, `trusted_client_ca`) com **`enable_agent_mtls = True`**; e **(3) Ajuste `quote_interval`** (ex.: `2` a `10` segundos) e o número de `max_workers` do Tornado/Verifier!

## Como funciona
No lado do agente em Rust (**`/etc/keylime/agent.conf`**), configure o `uuid` determinístico (ou `hash_ek`), restrinja o `ip` e a `port` (`9002`) para aceitar conexões mTLS exclusivamente do `Verifier` e configure `run_as = "keylime:tss"` para que o agente rode com privilégios reduzidos acessando `/dev/tpmrm0` pelo grupo `tss`!

## Exemplo
```toml
# Trecho essencial do /etc/keylime/agent.conf (rust-keylime) com mTLS habilitado e execucao com privilegio reduzido (keylime:tss)
[agent]
uuid = "d432fbb3-d2f1-4a97-9ef7-75bd81c00000"
ip = "10.20.30.15"
port = 9002
registrar_ip = "10.20.30.10"
registrar_port = 8890
enable_agent_mtls = true
run_as = "keylime:tss"
tpm_Hash_alg = "sha256"
tpm_encryption_alg = "ecc"
tpm_signing_alg = "rsassa"
```

## Limites e trade-offs
Veja na configuração do `agent.conf` acima a diretiva **`run_as = "keylime:tss"`**: graças ao gerenciador de recursos em kernel `/dev/tpmrm0` (que pertence ao grupo `tss`), o agente oficial `rust-keylime` pode abandonar privilégios de `root` após montar o diretório seguro e continuar realizando todas as operações de `TPM2_Quote` no chip TPM como usuário `keylime`!

## Como verificar
Ao atualizar arquivos `/etc/keylime/*.conf` entre versões do Keylime, utilize o utilitário **`keylime_upgrade_config`** para migrar seus parâmetros customizados para os novos templates de schema.

## Conexões
- [[keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust]] — Veja também: Resposta Automática a Incidentes (**Revocation Framework**) no Keylime: Isolando Nós Comprometidos em Segundos via **Webhooks**, **ZeroMQ** e Scripts **`local_action_*`**.
- [[keylime-modelo-push-attestation-edge-nat-firewalls-escalabilidade]] — Veja também: Atestação em Bordas Restritas e Atrás de NAT/Firewalls: **Push Mode Attestation (`keylime-push-model-agent`)** vs. Modelo Pull Clássico no Keylime.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust]] — Referência cruzada direta com rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
