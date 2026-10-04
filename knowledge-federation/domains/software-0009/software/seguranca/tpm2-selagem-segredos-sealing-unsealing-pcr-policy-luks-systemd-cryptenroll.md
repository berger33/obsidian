---
id: software.seguranca.tranche14.001394
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

# Selagem de Segredos (**Sealing / Unsealing** Vinculado a **PCRs**) com `tpm2_createpolicy`, `tpm2_unseal` e Desbloqueio **LUKS2 (`systemd-cryptenroll`)**

## Em uma frase
Como funciona a **Selagem de Segredos (`TPM Sealing`)** no TPM 2.0 — usada para destravar automaticamente a criptografia de disco completo **LUKS2 (`dm-crypt`)** no boot de um servidor Linux sem digitar senha no console, mas garantindo que **se alguém tirar o SSD/NVMe do servidor para ligar em outra máquina ou der boot por um pendrive Live USB, o TPM se recusará a entregar a chave**?

## Por que importa
Você cria uma **Política de PCR (`tpm2_createpolicy --policy-pcr -l sha256:0,7 -L pcr.policy`)** e sela o segredo dentro de um objeto do tipo `keyedhash` preso a essa política (`-L pcr.policy -i segredo.bin`)!

## Como funciona
Quando o servidor inicializa normalmente (mesma UEFI `PCR 0` e mesmo Secure Boot `PCR 7`), os valores atuais dos PCRs dentro do chip TPM batem exatamente com o digest gravado em `pcr.policy` e o comando **`tpm2_unseal -c sealed.ctx -p pcr:sha256:0,7`** libera o segredo! Mas se um atacante tentar dar boot por um pendrive USB, desativar o Secure Boot ou alterar o bootloader, o valor de `PCR 7` / `PCR 4` muda durante o boot e **o hardware do TPM bloqueia matematicamente o `tpm2_unseal`**!

## Exemplo
```bash
# Selar uma chave secreta vinculando-a aos valores atuais dos PCRs 0 e 7 (Firmware UEFI + Secure Boot) e deslacrar (unseal) validando a politica
tpm2_createprimary -C o -c primary.ctx
tpm2_createpolicy --policy-pcr -l sha256:0,7 -L policy_pcr0_7.dat
openssl rand -hex 32 | tpm2_create -C primary.ctx -u sealed.pub -r sealed.priv -L policy_pcr0_7.dat -i-
tpm2_load -C primary.ctx -u sealed.pub -r sealed.priv -c sealed.ctx
tpm2_unseal -c sealed.ctx -p pcr:sha256:0,7
```

## Limites e trade-offs
E para criptografia de disco **LUKS2** em distribuições Linux modernas com `systemd` (RHEL 9+, Fedora, Ubuntu 22.04+, Debian 12+), você pode enrolar um slot LUKS2 diretamente no TPM 2.0 (incluindo suporte a **TPM + PIN** com `--tpm2-with-pin=yes`!) usando um único comando nativo: **`systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=0+7 /dev/nvme0n1p3`**!

## Como verificar
Por que em sistemas que usam **Unified Kernel Images (`UKI`) assinadas pelo Secure Boot** recomenda-se selar no **`PCR 7` + `PCR 11` (ou Políticas Assinadas `tpm2-pcrlock` / `--tpm2-public-key`)** em vez de selar diretamente nos PCRs frágeis `4, 8, 9`? Porque toda atualização normal de pacote do Kernel (`apt upgrade` / `dnf update`) muda o hash do arquivo `vmlinuz`/`initrd` no `PCR 4/9`, enquanto o `PCR 7` (certificado Secure Boot) permanece estável entre atualizações legítimas assinadas!

## Conexões
- [[tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol]] — Veja também: Gerenciamento de Chaves no TPM 2.0: **`tpm2_createprimary`**, **`tpm2_create`**, **`tpm2_load`** e Persistência em NVRAM com **`tpm2_evictcontrol`**.
- [[tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin]] — Veja também: Políticas Avançadas de Autorização (**Enhanced Authorization — EA**) no TPM 2.0: **`tpm2_policyauthorize` (Políticas Assinadas)**, **`tpm2_policyor`** e **`tpm2_policysecret`**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Referência cruzada direta com tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
