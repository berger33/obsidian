---
id: software.seguranca.tranche14.001392
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md", "https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Funcionamento dos **PCRs (*Platform Configuration Registers*)** e **Measured Boot** no TPM 2.0: A Operação Unidirecional **`PCR_Extend`** e os Bancos **`sha256`**

## Em uma frase
Como o chip **TPM 2.0** sabe com certeza matemática se alguém adulterou a BIOS/UEFI, desativou o Secure Boot, trocou o bootloader GRUB, modificou a linha de comando do Kernel Linux (`init=/bin/sh`) ou alterou o `initramfs` antes de o sistema operacional subir?

## Por que importa
Através do **Measured Boot (*Inicialização Medida*)** e dos **24 Registradores de Configuração da Plataforma (`PCR 0` a `PCR 23`, mantidos em bancos de hash como `sha256`)**!

## Como funciona
Qual é o segredo criptográfico que torna um **PCR** impossível de falsificar mesmo se o atacante ganhar acesso `root` depois que o sistema subiu? **Ninguém (nem o `root`, nem o próprio kernel) pode fazer um `WRITE` arbitrário de um valor escolhido dentro de um PCR!** A única operação permitida pelo hardware sobre os PCRs de boot (`0` a `15`) é **`TPM2_PCR_Extend`**: **`PCR_novo = SHA256( PCR_antigo || SHA256(componente_medido) )`**! Como o `SHA-256` é uma função unidirecional resistente a pré-imagem e os PCRs só voltam a `0x00...00` quando o computador sofre um **Reset Físico**, a cadeia de hashes acumulada em cada PCR prova exatamente a sequência e o conteúdo de tudo o que rodou desde o ligar do botão Power!

## Exemplo
```bash
# Ler os valores atuais dos PCRs no banco SHA-256 (0 a 9) e inspecionar o log de eventos do Measured Boot UEFI/TCG
tpm2_pcrread sha256:0,1,2,3,4,5,6,7,8,9
tpm2_eventlog /sys/kernel/security/tpm0/binary_bios_measurements | head -n 40
```

## Limites e trade-offs
Entenda o significado dos principais **PCRs padronizados em sistemas Linux UEFI**: **`PCR 0`** (código do Firmware UEFI/BIOS), **`PCR 1`** (configuração do Firmware/Hardware), **`PCR 2` e `3`** (Option ROMs de placas PCI/NVMe), **`PCR 4`** (Bootloader: shim + GRUB2 + imagem do Kernel UEFI Stub), **`PCR 7`** (**Estado do UEFI Secure Boot e chaves PK/KEK/db/dbx — o PCR mais importante para selagem de disco!**), **`PCR 8` e `9`** (comandos, linha de comando do Kernel e `initramfs` medidos pelo GRUB2) e **`PCR 11`** (medições de *Unified Kernel Images — UKI* pelo `systemd-stub` / `systemd-pcrphase`)!

## Como verificar
O comando **`tpm2_eventlog /sys/kernel/security/tpm0/binary_bios_measurements`** decodifica o log binário deixado pela UEFI na tabela ACPI `TCPA`/`TPM2`, mostrando passo a passo cada binário e variável UEFI que foi estendido em cada PCR durante o boot!

## Conexões
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Veja também: Arquitetura do **TPM 2.0 (`tpm2-tss` & `tpm2-tools`)**: Raiz de Confiança em Hardware, Camadas da Stack TCG (`FAPI`, `ESYS`, `TCTI`) e **As 4 Hierarquias (`Owner`, `Endorsement`, `Platform`, `Null`)**.
- [[tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol]] — Veja também: Gerenciamento de Chaves no TPM 2.0: **`tpm2_createprimary`**, **`tpm2_create`**, **`tpm2_load`** e Persistência em NVRAM com **`tpm2_evictcontrol`**.
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Referência cruzada direta com tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll.
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Referência cruzada direta com tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
