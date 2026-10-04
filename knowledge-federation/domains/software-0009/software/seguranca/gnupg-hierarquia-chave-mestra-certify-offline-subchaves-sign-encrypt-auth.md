---
id: software.seguranca.tranche08.000702
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

# GnuPG: Arquitetura de **Chave Mestra `[C]` Offline** e **Subchaves Operacionais (`[S]` Sign, `[E]` Encrypt, `[A]` Authenticate)** em Curvas **Ed25519 / Cv25519**

## Em uma frase
No modelo de segurança do OpenPGP, uma identidade criptográfica não deve ser uma única chave monolítica usada para tudo: a melhor prática arquitetural separa a **Chave Primária / Mestra (`[C]` — *Certify*)**, que serve exclusivamente para assinar e revogar subchaves e identidades (`uid`), das **Subchaves de Uso Diário (`[S]` Assinatura, `[E]` Criptografia e `[A]` Autenticação SSH)**.

## Por que importa
Se o notebook de trabalho de um desenvolvedor ou engenheiro de release for roubado ou comprometido, e a chave mestra `[C]` estiver guardada **offline em cofre físico** (com apenas as subchaves `[S]`, `[E]` e `[A]` presentes no notebook via **`gpg --export-secret-subkeys`**), o engenheiro simplesmente revoga as subchaves comprometidas e emite novas subchaves **sem perder sua identidade OpenPGP principal nem invalidar a confiança acumulada pelos seus pares**!

## Como funciona
O GnuPG 2.4+ utiliza por padrão criptografia de curvas elípticas modernas: **Ed25519** para a chave mestra `[C]` e subchaves `[S]`/`[A]`, e **Curve25519 (`cv25519`)** para a subchave de criptografia `[E]`.

## Exemplo
```bash
# Gerar chave primaria Ed25519 apenas com capacidade Certify e exportar apenas as subchaves secretas (stub sec#)
gpg --batch --passphrase-fd 0 --quick-generate-key "SecOps Release Signing <secops@exemplo.com.br>" ed25519 cert 2y <<< "Passphrase-Forte-Mestra-2026!"
```

## Limites e trade-offs
Quando a chave mestra privada foi removida do computador de uso diário (deixando apenas o *stub* das subchaves exportadas com `gpg --export-secret-subkeys`), a saída de **`gpg -K`** exibe **`sec#`** (com o símbolo sustenido `#` após `sec`), comprovando que a chave primária `[C]` está protegida fora da máquina!

## Como verificar
Inspecione `gpg -K` na estação de trabalho e confirme que a chave primária exibe `sec#` e que cada subchave `ssb` possui data de expiração explícita.

## Conexões
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Veja também: GNU Privacy Guard (**GnuPG 2.x**): Arquitetura Modular (`gpg`, `gpg-agent`, `scdaemon`, `dirmngr` e `keyboxd`) e Padrão **OpenPGP (RFC 4880 / RFC 9580)**.
- [[gnupg-smartcards-yubikey-openpgp-scdaemon-card-edit-keytocard]] — Veja também: GnuPG & **`scdaemon`**: Armazenamento de Subchaves em Hardware (**YubiKey / SmartCard OpenPGP v3.4**), `keytocard` e Proteção de PIN/KDF.
- [[gnupg-certificado-revogacao-ciclo-vida-expiracao-rotacao-subchaves]] — Referência cruzada direta com gnupg-certificado-revogacao-ciclo-vida-expiracao-rotacao-subchaves.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
