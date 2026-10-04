---
id: software.seguranca.tranche08.000738
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

# Clevis Pin **`pkcs11`**: Desbloqueio de Volumes LUKS2 com SmartCards e Tokens de Hardware **PKCS#11** via URI RFC 7512

## Em uma frase
A partir das versões recentes do Clevis, o Pin **`pkcs11`** permite vincular o desbloqueio de volumes LUKS2 e objetos JWE a módulos criptográficos de hardware compatíveis com o padrão **PKCS#11 (Cryptoki)** identificáveis por uma **PKCS#11 URI (IETF RFC 7512)**.

## Por que importa
Em estações de trabalho ou servidores de custódia onde o módulo TPM não está disponível ou onde a política exige que um operador insira um cartão inteligente / YubiKey PIV físico no momento do boot, o Pin `pkcs11` utiliza o par de chaves RSA/ECC armazenado no slot PIV do token.

## Como funciona
A configuração JSON do Pin `pkcs11` recebe a `"uri"` RFC 7512 (`pkcs11:model=...;manufacturer=...;token=...;id=...`) e opcionalmente o caminho do módulo PKCS#11 (`module-path`, ex.: `/usr/lib64/opensc-pkcs11.so`).

## Exemplo
```bash
# Listar os tokens e objetos PKCS#11 disponiveis no sistema no formato URI RFC 7512 usando p11tool
p11tool --list-token-urls
```

## Limites e trade-offs
Ao usar tokens USB (PKCS#11 ou FIDO2) para desbloqueio no boot, certifique-se de que os módulos de kernel do controlador USB (`xhci_hcd`, `uhci_hcd`, `usbhid`, `ccid`) e o daemon `pcscd` estejam incluídos na imagem do `initramfs` (`dracut` / `initramfs-tools`), e que o **USBGuard** autorize o ID específico daquele token.

## Como verificar
Verifique com `p11tool --list-all "<URI_DO_TOKEN>"` a presença do certificado e da chave privada com capacidade de decriptação/derivação.

## Conexões
- [[clevis-pin-tpm2-pcr-banks-sha256-assinatura-politicas-seguranca]] — Veja também: Clevis Pin **`tpm2`**: Seleção Segura de Bancos e Registradores **PCR (`pcr_bank`, `pcr_ids`)** para Integridade de Boot.
- [[clevis-seguranca-rede-tang-segmentacao-vlan-ipsec-wireguard-mtls]] — Veja também: Arquitetura de Segurança de Rede para **Tang (NBDE)**: Segmentação de VLAN de Boot, *802.1X MACsec* e Riscos de Exposição do Endpoint `/rec`.
- [[clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato]] — Referência cruzada direta com clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato.
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Referência cruzada direta com cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
