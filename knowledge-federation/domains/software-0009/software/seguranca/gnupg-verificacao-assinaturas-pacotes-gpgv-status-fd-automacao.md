---
id: software.seguranca.tranche08.000705
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

# GnuPG (`gpgv` & `--status-fd`): Verificação Determinística de Assinaturas de Releases e Pacotes sem Efeitos Colaterais em Scripts e CI/CD

## Em uma frase
Um erro perigoso em scripts de automação e instaladores que verificam assinaturas OpenPGP (`*.asc` / `*.sig`) é invocar `gpg --verify arquivo.tar.gz.asc arquivo.tar.gz` e checar apenas `$? == 0` ou fazer `grep "Good signature"` na saída de texto humano: **a saída de texto humano do `gpg` muda conforme o idioma (`LC_ALL`) e pode ser falsificada por ataques de injeção de User IDs maliciosos, além de validar contra qualquer chave que por acaso esteja no `~/.gnupg/pubring.kbx` do usuário!**

## Por que importa
Para verificação automatizada segura (usada pelo `apt` do Debian/Ubuntu e por pipelines de supply chain), o projeto GnuPG fornece a ferramenta dedicada **`gpgv`** combinada com **`--keyring <chaveiro_isolado.gpg>`** e leitura estruturada via **`--status-fd 1`**!

## Como funciona
O utilitário **`gpgv`** é uma versão enxuta e somente-leitura do `gpg` que **nunca confia no chaveiro global do usuário, nunca baixa chaves da rede e considera válidas exclusivamente as chaves presentes no arquivo `--keyring` explicitamente informado**, emitindo tokens de máquina imutáveis (`[GNUPG:] GOODSIG`, `[GNUPG:] VALIDSIG <fingerprint_completo_da_subchave> <data> ... <fingerprint_da_chave_primaria>`).

## Exemplo
```bash
# Verificar assinatura destacada (.asc) de um release de forma deterministica com gpgv contra um keyring dedicado
gpgv --status-fd 1 \
  --keyring /etc/secops/keyrings/vendor-release-key.gpg \
  /cases/downloads/package-2.8.8.tar.sign \
  /cases/downloads/package-2.8.8.tar
```

## Limites e trade-offs
Em scripts críticos de verificação, além de exigir código de saída `0` do `gpgv`, confira no `--status-fd` que a linha **`[GNUPG:] VALIDSIG`** termina com o **fingerprint completo de 40 caracteres hexadecimais** da chave primária esperada.

## Como verificar
Importe uma chave pública de fornecedor em um chaveiro isolado com `gpg --no-default-keyring --keyring ./trusted-vendor.gpg --import vendor.asc` e valide com `gpgv --keyring ./trusted-vendor.gpg`.

## Conexões
- [[gnupg-operacao-gpg-agent-pinentry-cache-ttl-ssh-agent-socket]] — Veja também: GnuPG (`gpg-agent`): Configuração de Cache (`default-cache-ttl`, `max-cache-ttl`), Emulação **`enable-ssh-support`** e *Agent Forwarding* Remoto.
- [[gnupg-assinatura-commits-tags-git-allowed-signers-verificacao-ci]] — Veja também: GnuPG: Assinatura Criptográfica de **Commits e Tags Git (`commit.gpgsign`, `tag.gpgSign`)** e Gate de Verificação em Pipelines de CI/CD.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
