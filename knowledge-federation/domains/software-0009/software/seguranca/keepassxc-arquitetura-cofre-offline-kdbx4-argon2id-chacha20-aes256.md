---
id: software.seguranca.tranche13.001201
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md", "https://keepassxc.org/docs/KeePassXC_UserGuide"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura Criptográfica do **KeePassXC (`keepassxreboot/keepassxc`)**: Formato **KDBX 4**, Derivação **Argon2id** e Cifras **ChaCha20 / AES-256 / Twofish**

## Em uma frase
Por que engenheiros de segurança, operadores de PKI e equipes de resposta a incidentes escolhem um gerenciador de senhas **offline criptografado localmente (`KeePassXC`)** para proteger credenciais de emergência (*break-glass*), chaves SSH e tokens TOTP de infraestrutura crítica?

## Por que importa
Escrito em C++ (Qt, licenciado sob GPLv2/GPLv3 e certificado com o selo OpenSSF Best Practices), o **KeePassXC** armazena 100% dos segredos, anexos e metadados dentro de um arquivo local no formato aberto **KDBX 4** (compatível com o ecossistema KeePass), garantindo que **nenhum dado sensível jamais saia da máquina ou dependa de servidores de terceiros na nuvem**!

## Como funciona
Na camada criptográfica do formato **KDBX 4**, o KeePassXC aplica: **(1) Key Derivation Function (KDF)** baseada em **Argon2id** ou **Argon2d** (com parâmetros ajustáveis de memória RAM em MiB, iterações temporais e paralelismo de threads para neutralizar ataques de força bruta por GPU/ASIC); **(2) Criptografia de envelope** com escolha entre **ChaCha20 (256-bit)**, **AES-256-CBC** ou **Twofish**; **(3) Autenticação de integridade global e em blocos (`HMAC-SHA256` Block Stream)** contra adulteração de arquivo; e **(4) Ofuscação em memória RAM** dos campos de senha com stream cipher `ChaCha20`/`Salsa20` enquanto o banco está aberto!

## Exemplo
```bash
# Criar um novo cofre KDBX 4 via linha de comando (keepassxc-cli) e inspecionar os parametros criptograficos (Argon2id / ChaCha20) do arquivo
keepassxc-cli --version
keepassxc-cli db-info ./cofre-infraestrutura.kdbx
```

## Limites e trade-offs
Calibre os parâmetros do **Argon2id** nas configurações de segurança do banco (`Ctrl+Shift+,` -> *Security* -> *Benchmark 1.0 sec delay*) para que a derivação da chave mestra leve cerca de **1 segundo** no seu hardware de trabalho — tornando ataques de dicionário offline milhões de vezes mais lentos para um adversário!

## Como verificar
Por padrão no Windows e macOS, o KeePassXC também bloqueia capturas de tela e gravações de janela da aplicação (*Screenshot Security*) para evitar vazamento acidental de senhas durante compartilhamentos de tela em reuniões.

## Conexões
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Veja também: Chave Composta do KeePassXC: Combinando **Senha Mestra + Key File + Hardware Challenge-Response (`YubiKey` / `OnlyKey` HMAC-SHA1)**.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Referência cruzada direta com keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
