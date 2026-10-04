---
id: software.seguranca.tranche15.001414
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

# Monitoramento de Integridade em Tempo de Execução (**Runtime Integrity Monitoring**) no Keylime com **Linux IMA (`Integrity Measurement Architecture` — `PCR 10`)**

## Em uma frase
O **Measured Boot** tradicional (`PCR 0` a `PCR 9`) mede a UEFI, o bootloader GRUB e a imagem do Kernel no momento em que o servidor liga. Mas e se o servidor ligar limpo às 08h00 da manhã e, às 14h30 da tarde, um invasor explorar uma vulnerabilidade web, baixar um binário malicioso `/tmp/exploit` (ou modificar `/usr/bin/sshd`) e executá-lo em memória? Os PCRs `0–9` de boot não mudam depois do boot!

## Por que importa
Como o **Keylime** detecta em menos de 2 segundos qualquer binário, script ou biblioteca compartilhada executada ou modificada **durante o tempo de execução (Runtime)**?

## Como funciona
Integrando o chip **TPM 2.0 (`PCR 10`)** ao subsistema nativo do Kernel Linux chamado **IMA (*Integrity Measurement Architecture*)**! Quando o Kernel Linux está com `ima_policy=tcb` (ou política customizada), **antes** de executar qualquer binário (`BPRM_CHECK`), mapear qualquer biblioteca `.so` (`MMAP_CHECK`) ou ler arquivos críticos, o próprio Kernel calcula o hash **`SHA-256` do arquivo**, grava uma linha na lista `/sys/kernel/security/ima/ascii_runtime_measurements` e **executa `TPM2_PCR_Extend` no `PCR 10` do chip TPM**! Como o `PCR 10` está dentro do hardware do TPM, nem mesmo um rootkit em nível de `root` consegue apagar uma medição depois que o arquivo foi executado!

## Exemplo
```bash
# Inspecionar a lista de medicoes em tempo de execucao do Linux IMA (estendida no PCR 10 do TPM) e criar uma Runtime Policy para o Keylime
head -n 15 /sys/kernel/security/ima/ascii_runtime_measurements
keylime_create_policy -m /sys/kernel/security/ima/ascii_runtime_measurements -o ./runtime_policy_ima.json
```

## Limites e trade-offs
Como o **`Keylime Verifier`** valida que o servidor não está mentindo sobre a lista do IMA? A cada ciclo (ex.: a cada 2 segundos), o `Verifier` pede ao `Agent` as novas linhas do log do IMA e uma cotação assinada pelo TPM (**`TPM2_Quote` incluindo o `PCR 10`**): o `Verifier` recalcula a cadeia de `SHA-256` de todas as linhas do log IMA desde o boot e confere se o resultado bate bit a bit com o valor do **`PCR 10` assinado pelo hardware do TPM**, e em seguida compara cada hash `SHA-256` contra a **Runtime Policy (Allowlist + Excludelist)**!

## Como verificar
Se qualquer binário fora da Allowlist for executado no servidor, a verificação falha no ciclo seguinte e o Keylime dispara a **Revogação Automática** em segundos!

## Conexões
- [[keylime-provisionamento-payload-criptografado-bootstrap-chaves-mtls]] — Veja também: Entrega Segura de Segredos (**Encrypted Payload Provisioning**) no Keylime: Derivação Tripartida da Chave **`U` + `V` = `K`** só Após Aprovação na Atestação!.
- [[keylime-criacao-politicas-keylime-create-policy-assinatura-ima-evm]] — Veja também: Geração de Políticas de Runtime (**`keylime_create_policy`**), Verificação de Assinaturas Digitais **`ima-sig`** e Repositórios de Pacotes Confiáveis no Keylime.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
