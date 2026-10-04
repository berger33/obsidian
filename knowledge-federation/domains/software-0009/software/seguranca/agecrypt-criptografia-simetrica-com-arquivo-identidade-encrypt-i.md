---
id: software.seguranca.tranche02.000156
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/FiloSottile/age/main/README.md", "https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html", "https://github.com/FiloSottile/age"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `age` Criptografia Simétrica para Arquivo de Identidade (`age --encrypt -i key.txt`): backups sem gerenciar chave pública separada

## Em uma frase
Conforme documentado na seção *Usage* do README e em `age(1)`, quando a flag **`-e` / `--encrypt` é especificada explicitamente**, a flag **`-i` / `--identity`** também pode ser usada para cifrar o arquivo para os destinatários correspondentes às identidades contidas em `PATH` (equivalente a converter `key.txt` com `age-keygen -y` e passar como destinatário)!

## Por que importa
Em scripts automatizados de backup onde o servidor já possui o arquivo de identidade ou onde você usa uma identidade cifrada por passphrase, não precisar manter dois arquivos sincronizados (`key.txt` e `pubkey.txt`) simplifica a operação.

## Como funciona
Por segurança de interface na CLI, o `age` exige que você escreva **`--encrypt` (ou `-e`) explicitamente** quando usar `-i` para cifrar, evitando que um usuário que esqueceu de digitar `-d` ao tentar decifrar (`age -i key.txt file.age`) sobrescreva ou cifre duas vezes o arquivo por engano!

## Exemplo
```bash
# Cifrando um arquivo diretamente para os destinatários correspondentes ao arquivo de identidade key.txt:
age --encrypt -i key.txt -o backup.sql.age backup.sql

# Decifrando com o mesmo arquivo de identidade:
age --decrypt -i key.txt -o backup.sql backup.sql.age
```

## Limites e trade-offs
Melhor ainda: em um servidor de produção que só precisa **gerar** backups cifrados (e nunca decifrá-los localmente), mantenha no servidor **apenas a chave pública (`-r age1...`)** e guarde a chave privada (`key.txt`) offline em cofre seguro!

## Como verificar
Teste executar `age -e -i key.txt` e confirme que omitir `-e` ao passar `-i` retorna erro informativo pedindo `-e` ou `-d` explícito.

## Conexões
- [[agecrypt-ascii-armor-pem-strict-base64-protecao-tty]] — Veja também: `age` ASCII Armor (`-a` / `--armor`): codificação PEM canônica estrita (`AGE ENCRYPTED FILE`) e proteção de TTY.
- [[agecrypt-plugins-hardware-yubikey-fido2-kms-arquitetura-extensivel]] — Veja também: `age` Sistema de Plugins (`age-plugin-*` e `-j`): chaves em hardware com `age-plugin-yubikey`, Secure Enclave e TPM.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
