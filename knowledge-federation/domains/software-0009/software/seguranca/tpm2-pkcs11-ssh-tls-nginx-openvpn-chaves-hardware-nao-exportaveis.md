---
id: software.seguranca.tranche14.001397
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

# Uso de Chaves TPM 2.0 Não-Exportáveis em **OpenSSH, Nginx, OpenVPN, StrongSwan e Rust/Go** com **`tpm2-pkcs11`** e **`tpm2-openssl` Provider**

## Em uma frase
Como fazer com que a **chave privada SSH de um administrador (`ssh -I`)**, a **chave privada do certificado TLS de um servidor Nginx/Apache** ou a **chave mTLS de um agente VPN (`strongSwan` / `OpenVPN`)** seja gerada dentro do chip **TPM 2.0** da máquina e usada para assinar conexões TLS/SSH **sem que a chave privada jamais exista em texto claro na memória RAM ou no disco**?

## Por que importa
A organização `tpm2-software` mantém duas pontes padrão da indústria que conectam qualquer aplicação existente ao TPM 2.0: **(1) `tpm2-pkcs11` (`libtpm2_pkcs11.so`)** — expõe o TPM 2.0 como um token criptográfico padrão **PKCS#11 (`Cryptoki`)** compatível nativamente com OpenSSH (`ssh -I` / `ssh-add -s`), Firefox/Chrome, GnuTLS, strongSwan, OpenVPN e Java!; e **(2) `tpm2-openssl` (`provider = tpm2` no OpenSSL 3.x)** — integra o TPM 2.0 diretamente à arquitetura de Providers do OpenSSL 3!

## Como funciona
Quando o Nginx ou o `ssh` precisa assinar o desafio do handshake TLS 1.3 ou SSH, a biblioteca PKCS#11 envia apenas o digest (`32 bytes`) para `/dev/tpmrm0`, o chip TPM assina lá dentro do silício e devolve a assinatura pronta!

## Exemplo
```bash
# Inicializar um token PKCS#11 no TPM 2.0 com tpm2_ptool, gerar uma chave ECC P-256 no hardware e autenticar via OpenSSH usando a chave presa ao TPM
tpm2_ptool init --path=/etc/tpm2_pkcs11
tpm2_ptool addtoken --pid=1 --label=token-ssh-servidor --sopin=SoPinSecreto123 --userpin=UserPinSecreto123 --path=/etc/tpm2_pkcs11
tpm2_ptool addkey --label=token-ssh-servidor --userpin=UserPinSecreto123 --algorithm=ecc256 --path=/etc/tpm2_pkcs11
ssh-keygen -D /usr/lib/x86_64-linux-gnu/pkcs11/libtpm2_pkcs11.so
```

## Limites e trade-offs
Pense no impacto de segurança de usar **`libtpm2_pkcs11.so`** (ou `tpm2-openssl`) para a chave privada mTLS/SSH de uma máquina: se um invasor explorar uma vulnerabilidade na aplicação e copiar toda a pasta `/etc/ssl/` e `/etc/tpm2_pkcs11/` para o servidor dele, **ele não conseguirá usar a chave privada roubada**, porque os arquivos copiados são apenas blobs cifrados pela `Storage Root Key (SRK)` daquele chip TPM físico!

## Como verificar
No OpenSSH, você pode inclusive carregar o token do TPM no `ssh-agent` da sessão com **`ssh-add -s /usr/lib/x86_64-linux-gnu/pkcs11/libtpm2_pkcs11.so`** para autenticar transparentemente em todos os seus hosts.

## Conexões
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Veja também: Atestação Remota de Hardware e Boot (**Remote Attestation**) no TPM 2.0: **Endorsement Key (`EK`)**, **Attestation Key (`AK`)**, **`tpm2_quote`** e **`tpm2_checkquote`**.
- [[tpm2-nvram-armazenamento-seguro-contadores-monotonicos-anti-rollback]] — Veja também: Memória Não-Volátil (**NVRAM**: `tpm2_nvdefine`, `tpm2_nvwrite`, `tpm2_nvread`) e **Contadores Monotônicos Anti-Rollback (`tpm2_nvincrement`)** no TPM 2.0.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol]] — Referência cruzada direta com tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
