---
id: software.seguranca.tranche02.000158
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

# `age` Criptografia Pós-Quântica Híbrida e Verificação de Binários com `Sigsum`: proteção contra *Harvest Now, Decrypt Later*

## Em uma frase
Conforme destacado no README oficial do `age` (*"It features small explicit keys, post-quantum support, no config options, and UNIX-style composability"* e `./SIGSUM.md`), o ecossistema `age` incorpora suporte a destinatários híbridos pós-quânticos (`ML-KEM-768` / Kyber combinado com `X25519`) e transparência criptográfica de binários via **Sigsum**.

## Por que importa
Ataques do tipo *Harvest Now, Decrypt Later (HNDL)* capturam backups cifrados hoje em trânsito ou em buckets de armazenamento para decifrá-los no futuro quando computadores quânticos capazes de quebrar ECDH (`X25519`) puro estiverem disponíveis.

## Como funciona
Combinar um acordo de chaves pós-quântico baseado em reticulados (`ML-KEM`) de forma híbrida com `X25519` garante que a segurança nunca seja inferior ao `X25519` clássico hoje, enquanto resiste a adversários quânticos futuros.

## Exemplo
```bash
# Verificando a versão instalada do age e consultando a documentação local da man page:
age --version
man age
```

## Limites e trade-offs
Ao baixar binários pré-compilados oficiais em `https://dl.filippo.io/age/latest`, verifique sempre as provas de transparência de log público conforme documentado em `SIGSUM.md`.

## Como verificar
Inspecione o cabeçalho de um arquivo `.age` (primeiras linhas em texto ASCII antes do `---`) para ver os tipos de `stanza` de destinatário gravados.

## Conexões
- [[agecrypt-plugins-hardware-yubikey-fido2-kms-arquitetura-extensivel]] — Veja também: `age` Sistema de Plugins (`age-plugin-*` e `-j`): chaves em hardware com `age-plugin-yubikey`, Secure Enclave e TPM.
- [[agecrypt-biblioteca-go-filippo-io-age-encrypt-decrypt-streams]] — Veja também: `age` como Biblioteca Nativa em Go (`filippo.io/age`): `age.Encrypt`, `age.Decrypt` e `armor` em aplicações sem processos externos.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
