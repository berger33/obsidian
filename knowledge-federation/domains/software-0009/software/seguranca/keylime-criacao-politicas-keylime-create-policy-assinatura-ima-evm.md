---
id: software.seguranca.tranche15.001415
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

# Geração de Políticas de Runtime (**`keylime_create_policy`**), Verificação de Assinaturas Digitais **`ima-sig`** e Repositórios de Pacotes Confiáveis no Keylime

## Em uma frase
Como construir e manter a **Runtime Policy JSON** do Keylime para servidores Linux que recebem centenas de pacotes e atualizações legítimas (`dnf update` / `apt upgrade`) sem precisar regerar hashes manualmente a cada pacote atualizado?

## Por que importa
O Keylime oferece o utilitário oficial **`keylime_create_policy`** e suporta dois mecanismos complementares na Runtime Policy: **(1) Hashes `SHA-256` explícitos extraídos de uma Golden Image, de um rootfs/container ou diretamente dos repositórios de pacotes RPM/DEB**; e **(2) Verificação de Assinaturas Digitais IMA (`ima-sig` com chaves públicas X.509 confiáveis em `verification-keys`)**!

## Como funciona
Quando você usa **`ima-sig`** (onde os binários e bibliotecas nos pacotes RPM/DEB vêm assinados no atributo estendido `security.ima` pela chave privada da distribuição ou da sua empresa!), você adiciona a chave pública X.509 na política do Keylime (`--ima-signature-keys`): assim, **qualquer atualização legítima de pacote assinada pela chave oficial passa automaticamente na atestação do Keylime sem precisar atualizar a lista de hashes**!

## Exemplo
```bash
# Gerar uma Runtime Policy JSON para o Keylime combinando medicoes da imagem base, lista de exclusao de logs dinamicos (-e) e chave de assinatura IMA
keylime_create_policy \
  --ima-measurement-list /sys/kernel/security/ima/ascii_runtime_measurements \
  --exclude-list /etc/keylime/ima_exclude.txt \
  --output ./politica_runtime_producao.json
keylime_tenant -c addruntimepolicy --runtime-policy ./politica_runtime_producao.json --runtime-policy-name prod-rhel9-v1
```

## Limites e trade-offs
Por que o arquivo de **`exclude-list` (`--exclude-list`)** deve ser revisado com extremo rigor de segurança antes de ir para produção? Porque caminhos incluídos na lista de exclusão (usados tipicamente para arquivos de log ou caches voláteis em `/var/log/.*`) são ignorados na comparação de hashes pelo Verifier; **JAMAIS inclua na `exclude-list` diretórios onde binários ou scripts possam ser executados (como `/tmp`, `/var/tmp`, `/dev/shm`, `/home` ou `/usr/local/bin`)**!

## Como verificar
Com `keylime_tenant -c addruntimepolicy` (e `updateruntimepolicy`), você armazena as políticas nomeadas diretamente no banco do Verifier e pode atualizá-las dinamicamente para frotas inteiras de agentes.

## Conexões
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Veja também: Monitoramento de Integridade em Tempo de Execução (**Runtime Integrity Monitoring**) no Keylime com **Linux IMA (`Integrity Measurement Architecture` — `PCR 10`)**.
- [[keylime-atestacao-measured-boot-uefi-eventlog-elchecking-politicas]] — Veja também: Atestação de **Measured Boot UEFI (`binary_bios_measurements`)** e Políticas de Firmware/Secure Boot (`--mb_refstate`) no Keylime.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
