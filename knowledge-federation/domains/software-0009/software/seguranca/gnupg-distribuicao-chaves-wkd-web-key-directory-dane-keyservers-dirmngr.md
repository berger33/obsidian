---
id: software.seguranca.tranche08.000708
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

# GnuPG & `dirmngr`: Descoberta Segura de Chaves Públicas via **WKD (*Web Key Directory*)** e **OPENPGPKEY DANE (RFC 7929)** vs Keyservers HKP

## Em uma frase
Historicamente, servidores de chaves públicos baseados no protocolo SKS/HKP sofriam de dois problemas graves: qualquer pessoa podia fazer upload de chaves falsas com o e-mail de terceiros (*Key Spoofing*) ou anexar dezenas de milhares de assinaturas de terceiros a uma chave pública para corromper o cliente de quem a importasse (*Certificate Flooding / Poisoning*).

## Por que importa
Para resolver a distribuição autenticada de chaves públicas corporativas, o projeto GnuPG e o IETF padronizaram dois mecanismos superiores suportados nativamente pelo **`dirmngr`** (`gpg --locate-keys usuario@exemplo.com.br`): **(1) WKD (*Web Key Directory*)** e **(2) DNS DANE `OPENPGPKEY` (RFC 7929)**.

## Como funciona
No **WKD**, o próprio domínio `exemplo.com.br` serve a chave pública binária sob HTTPS em `https://openpgpkey.exemplo.com.br/.well-known/openpgpkey/exemplo.com.br/hu/<zbase32(sha1(localpart))>` (gerado com `gpg-wks-client` / `gpg --with-wkd-hash`), garantindo que apenas o dono do domínio HTTPS possa publicar a chave de `secops@exemplo.com.br`!

## Exemplo
```bash
# Calcular o hash z-base-32 oficial do Web Key Directory (WKD) para publicar uma chave publica no dominio HTTPS
gpg --with-wkd-hash --fingerprint secops@exemplo.com.br
gpg --auto-key-locate clear,nodefault,wkd,dane --locate-keys secops@exemplo.com.br
```

## Limites e trade-offs
Se precisar buscar uma chave no servidor público moderno **`keys.openpgp.org`** (que exige verificação de posse do e-mail antes de publicar o User ID e aplica `import-clean`), adicione `import-options import-clean` e `export-options export-clean` no `gpg.conf` para descartar assinaturas de terceiros desnecessárias.

## Como verificar
Verifique com `gpg --with-wkd-hash -k` o caminho exato `.well-known/openpgpkey/hu/...` onde o arquivo binário exportado (`gpg --export`) deve ser hospedado.

## Conexões
- [[gnupg-criptografia-simetrica-hibrida-aead-aes256-s2k-argon2-iteracoes]] — Veja também: GnuPG: Criptografia Simétrica (`-c`) e Híbrida Assimétrica (`-e -r`), **S2K (`s2k-count` / Argon2)** e Preferências de Cifra (`AES256`, `SHA512`).
- [[gnupg-certificado-revogacao-ciclo-vida-expiracao-rotacao-subchaves]] — Veja também: GnuPG: Ciclo de Vida Criptográfico — Certificados de Revogação (`--gen-revoke`), Renovação de Validade (`--quick-set-expire`) e Resposta a Comprometimento.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.
- [[gnupg-modelo-confianca-tofu-trust-on-first-use-wot-tsign]] — Referência cruzada direta com gnupg-modelo-confianca-tofu-trust-on-first-use-wot-tsign.
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Referência cruzada direta com certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
