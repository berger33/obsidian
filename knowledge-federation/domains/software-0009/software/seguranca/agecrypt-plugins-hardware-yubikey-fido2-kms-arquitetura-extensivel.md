---
id: software.seguranca.tranche02.000157
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

# `age` Sistema de Plugins (`age-plugin-*` e `-j`): chaves em hardware com `age-plugin-yubikey`, Secure Enclave e TPM

## Em uma frase
O `age` possui uma arquitetura oficial de plugins binários (**`age-plugin-<NAME>`** encontrados no `$PATH`) que estende o formato para tokens de hardware (**YubiKey PIV via `age-plugin-yubikey`**), **Apple Secure Enclave (`age-plugin-se`)**, **TPM 2.0 (`age-plugin-tpm`)** e chaves FIDO2, acionados automaticamente pelo prefixo Bech32 da chave (`age1<name>1...` e `AGE-PLUGIN-<NAME>-1...`) ou via flag `-j <PLUGIN>`.

## Por que importa
Armazenar a chave privada de descriptografia em um arquivo no disco do laptop ainda permite que um malware com acesso ao usuário copie o arquivo; em um YubiKey PIV ou TPM, a chave privada nunca pode ser exportada do chip de hardware.

## Como funciona
Quando você passa um destinatário `age1yubikey1...`, o binário `age` invoca automaticamente o executável `age-plugin-yubikey` no `$PATH` usando o protocolo de máquina de estados de plugin da especificação C2SP, exigindo toque físico e PIN no YubiKey durante o `age --decrypt`!

## Exemplo
```bash
# Gerando uma identidade vinculada ao slot PIV do YubiKey e decifrando com hardware token:
age-plugin-yubikey --generate
age --decrypt -i yubikey-identity.txt segredo-critico.age
```

## Limites e trade-offs
Gere sempre pelo menos uma chave de recuperação offline (em um segundo YubiKey de backup guardado em cofre físico) e inclua ambos os destinatários (`-R recipients.txt`) ao cifrar arquivos críticos.

## Como verificar
Verifique os plugins instalados e reconhecidos executando `which age-plugin-yubikey`.

## Conexões
- [[agecrypt-criptografia-simetrica-com-arquivo-identidade-encrypt-i]] — Veja também: `age` Criptografia Simétrica para Arquivo de Identidade (`age --encrypt -i key.txt`): backups sem gerenciar chave pública separada.
- [[agecrypt-suporte-pos-quantico-pq-ml-kem-x25519-especificacao-c2sp]] — Veja também: `age` Criptografia Pós-Quântica Híbrida e Verificação de Binários com `Sigsum`: proteção contra *Harvest Now, Decrypt Later*.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
