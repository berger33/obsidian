---
id: software.seguranca.tranche15.001416
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

# Atestação de **Measured Boot UEFI (`binary_bios_measurements`)** e Políticas de Firmware/Secure Boot (`--mb_refstate`) no Keylime

## Em uma frase
Enquanto o **Linux IMA (`PCR 10`)** vigia os arquivos abertos depois que o Kernel Linux assumiu o controle, como o **Keylime** audita tudo o que aconteceu **antes do Kernel subir** — como a versão exata da BIOS/UEFI, a ordem de boot, os certificados do **UEFI Secure Boot (`PK`, `KEK`, `db`, `dbx` no `PCR 7`)**, o `shim.efi`, o `grubx64.efi` e a linha de comando do Kernel (`boot_aggregate`)?

## Por que importa
Através do motor de **Measured Boot Attestation (`--mb_refstate` / `measured_boot_policy_name`)** do Keylime!

## Como funciona
Em vez de olhar apenas para os valores finais opacos dos PCRs `0` a `9` (que mudam por motivos difíceis de diagnosticar quando um periférico muda), o `keylime_agent` envia ao `Verifier` o log completo de eventos UEFI da ACPI (**`/sys/kernel/security/tpm0/binary_bios_measurements`**) junto com a cotação assinada dos PCRs `0–9`! O `Verifier` primeiro **recalcula todos os `PCR_Extend` do log UEFI para provar matematicamente contra o `TPM2_Quote` que o log UEFI é 100% verdadeiro**, e depois aplica a política de *Measured Boot* (`accept-all`, `reject-all` ou política customizada de *Reference State*) validando se o **Secure Boot está `Enabled`**, quais chaves `db`/`dbx` estão ativas e se o digest do `shim` + `grub` + `vmlinuz` é autorizado!

## Exemplo
```bash
# Provisionar um agente Keylime exigindo simultaneamente Runtime Policy (IMA PCR 10) e Measured Boot Reference State (UEFI PCRs 0-9)
keylime_tenant -c add \
  -t 10.20.30.15 \
  -u d432fbb3-d2f1-4a97-9ef7-75bd81c00000 \
  --runtime-policy-name prod-rhel9-v1 \
  --mb_refstate ./measured_boot_refstate.json
```

## Limites e trade-offs
Olhe como o **`boot_aggregate`** (a primeira entrada da lista do Linux IMA no `PCR 10`) fecha o elo criptográfico entre o **Measured Boot (`PCRs 0–9`)** e o **Runtime IMA (`PCR 10`)**: ao iniciar o subsistema IMA durante o boot, o Kernel Linux lê os valores acumulados dos `PCRs 0 a 9` dentro do chip TPM, calcula um hash agregado deles e registra esse valor como a entrada #1 (`boot_aggregate`) no `PCR 10`!

## Como verificar
Assim, com **Measured Boot + IMA (`PCR 0–10`)** auditados juntos pelo Keylime, existe uma cadeia criptográfica ininterrupta desde o primeiro ciclo de clock do reset da placa-mãe até o último processo em execução hoje!

## Conexões
- [[keylime-criacao-politicas-keylime-create-policy-assinatura-ima-evm]] — Veja também: Geração de Políticas de Runtime (**`keylime_create_policy`**), Verificação de Assinaturas Digitais **`ima-sig`** e Repositórios de Pacotes Confiáveis no Keylime.
- [[keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust]] — Veja também: Resposta Automática a Incidentes (**Revocation Framework**) no Keylime: Isolando Nós Comprometidos em Segundos via **Webhooks**, **ZeroMQ** e Scripts **`local_action_*`**.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Referência cruzada direta com keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices.
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Referência cruzada direta com tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
