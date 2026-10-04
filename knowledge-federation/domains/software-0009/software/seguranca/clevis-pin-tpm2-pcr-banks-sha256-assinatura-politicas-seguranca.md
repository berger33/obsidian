---
id: software.seguranca.tranche08.000737
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/latchset/clevis/master/README.md", "https://raw.githubusercontent.com/latchset/tang/master/README.md", "https://github.com/latchset/jose"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clevis Pin **`tpm2`**: Seleção Segura de Bancos e Registradores **PCR (`pcr_bank`, `pcr_ids`)** para Integridade de Boot

## Em uma frase
Quando o Pin **`tpm2`** do Clevis é usado com configuração vazia (`'{}'`), ele sela a chave dentro do chip TPM 2.0 usando a *Storage Root Key (SRK)* sem vincular a nenhum registrador de configuração de plataforma (**PCR — *Platform Configuration Register***): isso protege contra alguém que retire apenas os discos SSD/NVMe do servidor (pois os discos sem a placa-mãe não abrem), mas se o atacante levar o servidor inteiro e der boot por um pendrive Linux Live malicioso, o TPM2 ainda liberará a chave!

## Por que importa
Para impedir que um boot modificado (pendrive Live, edição da linha de comando do kernel no GRUB `init=/bin/sh` ou desativação do Secure Boot) consiga fazer o TPM 2.0 liberar a chave, é obrigatório especificar **`"pcr_bank": "sha256"`** e **`"pcr_ids"`** na configuração do Pin `tpm2`.

## Como funciona
Na especificação TCG PC Client Platform Firmware Profile: **PCR 0** mede o código do firmware BIOS/UEFI; **PCR 1** mede a configuração da BIOS; **PCR 4** mede o bootloader EFI; **PCR 7** mede o estado do **UEFI Secure Boot** e as chaves PK/KEK/db/dbx autorizadas; e **PCR 9 / 11 / 14** medem o kernel/initrd/MOK.

## Exemplo
```bash
# Inspecionar os valores atuais do banco SHA-256 dos registradores PCR 0, 1, 4, 7 no chip TPM 2.0 local via tpm2_pcrread
tpm2_pcrread sha256:0,1,4,7
```

## Limites e trade-offs
Vincular inicialmente apenas ao **`PCR 7` (`"pcr_ids": "0,7"`)** com o **UEFI Secure Boot ativo** e senha na BIOS/UEFI garante que o TPM 2.0 recuse o desbloqueio se o Secure Boot for desligado ou se qualquer bootloader não assinado pela sua cadeia confiável tentar iniciar, sem quebrar a cada atualização normal de kernel assinado pela distribuição.

## Como verificar
Confirme com `tpm2_pcrread sha256:7` que o chip TPM 2.0 está ativo com o banco `sha256` populado antes de executar `clevis luks bind`.

## Conexões
- [[clevis-auditoria-regeneracao-clevis-luks-list-regen-unbind-edit]] — Veja também: Clevis: Ciclo de Vida de Vínculos LUKS (`clevis luks list`, `unlock`, `regen`, `edit` e `unbind`) após Rotação de Chaves Tang ou Mudança de PCRs.
- [[clevis-pin-pkcs11-smartcards-yubikey-desbloqueio-discos-luks]] — Veja também: Clevis Pin **`pkcs11`**: Desbloqueio de Volumes LUKS2 com SmartCards e Tokens de Hardware **PKCS#11** via URI RFC 7512.
- [[clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato]] — Referência cruzada direta com clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato.
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Referência cruzada direta com clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2.
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Referência cruzada direta com cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
