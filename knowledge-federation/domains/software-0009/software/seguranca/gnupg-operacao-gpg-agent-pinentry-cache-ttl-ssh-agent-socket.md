---
id: software.seguranca.tranche08.000704
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
fontes: ["https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html", "https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html", "https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# GnuPG (`gpg-agent`): Configuração de Cache (`default-cache-ttl`, `max-cache-ttl`), Emulação **`enable-ssh-support`** e *Agent Forwarding* Remoto

## Em uma frase
O daemon **`gpg-agent`** gerencia em memória não-paginável (`mlock`) o cache temporário de passphrases e PINs, além de implementar nativamente o protocolo do **`ssh-agent` (`enable-ssh-support`)**, permitindo usar a subchave de autenticação OpenPGP **`[A]`** (inclusive armazenada em um YubiKey) diretamente como chave SSH!

## Por que importa
Se os tempos de cache padrão do `~/.gnupg/gpg-agent.conf` forem longos demais em um notebook corporativo, uma chave desbloqueada pela manhã permanece aberta na sessão pelo resto do dia; ajustando **`default-cache-ttl 300`** (5 minutos de inatividade) e **`max-cache-ttl 1800`** (30 minutos absolutos), o `gpg-agent` limpa a passphrase automaticamente.

## Como funciona
E ao adicionar `enable-ssh-support` no `gpg-agent.conf` e apontar `SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)`, o comando **`gpg --export-ssh-key <ID>`** exporta a linha `ssh-ed25519 AAAA...` pronta para ser colada no `~/.ssh/authorized_keys` dos servidores.

## Exemplo
```ini
# ~/.gnupg/gpg-agent.conf — Hardening de tempos de cache de credenciais e suporte nativo a SSH Agent
default-cache-ttl 300
max-cache-ttl 1800
default-cache-ttl-ssh 300
max-cache-ttl-ssh 1800
enable-ssh-support
no-allow-external-cache
no-allow-mark-trusted
```

## Limites e trade-offs
Caso precise usar o seu YubiKey local para assinar commits ou decifrar arquivos em uma estação de build remota via SSH, jamais copie chaves privadas para o servidor remoto: encaminhe apenas o socket restrito **`agent-extra-socket`** (`gpgconf --list-dirs agent-extra-socket`) via `RemoteForward` do OpenSSH, que proíbe exportação ou exclusão de chaves a partir do host remoto.

## Como verificar
Recarregue o `gpg-agent` após alterações executando **`gpg-connect-agent reloadagent /bye`** e verifique a chave SSH exposta com `ssh-add -L`.

## Conexões
- [[gnupg-smartcards-yubikey-openpgp-scdaemon-card-edit-keytocard]] — Veja também: GnuPG & **`scdaemon`**: Armazenamento de Subchaves em Hardware (**YubiKey / SmartCard OpenPGP v3.4**), `keytocard` e Proteção de PIN/KDF.
- [[gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao]] — Veja também: GnuPG (`gpgv` & `--status-fd`): Verificação Determinística de Assinaturas de Releases e Pacotes sem Efeitos Colaterais em Scripts e CI/CD.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.
- [[gnupg-assinatura-commits-tags-git-allowed-signers-verificacao-ci]] — Referência cruzada direta com gnupg-assinatura-commits-tags-git-allowed-signers-verificacao-ci.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
