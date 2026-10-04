---
id: software.seguranca.tranche08.000709
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

# GnuPG: Ciclo de Vida Criptográfico — Certificados de Revogação (`--gen-revoke`), Renovação de Validade (`--quick-set-expire`) e Resposta a Comprometimento

## Em uma frase
No OpenPGP, se você perder a chave privada mestra **e** não tiver gerado previamente um **Certificado de Revogação (`.rev`)**, será matematicamente impossível avisar ao mundo que aquela chave não deve mais ser utilizada; por isso, o GnuPG 2.1+ gera automaticamente um certificado de revogação de emergência em **`~/.gnupg/openpgp-revocs.d/<FINGERPRINT>.rev`** no instante da criação da chave.

## Por que importa
Note que nos arquivos gerados automaticamente em `openpgp-revocs.d/`, o GnuPG insere por segurança um caractere dois-pontos (`:`) antes da linha `-----BEGIN PGP PUBLIC KEY BLOCK-----` para evitar que alguém o importe por acidente sem ler as instruções no cabeçalho.

## Como funciona
Para rotacionar subchaves anualmente ou estender a data de expiração de uma subchave sem trocar seu material criptográfico, o comando não-interativo **`gpg --quick-set-expire <FINGERPRINT_PRIMARIO> <VALIDADE> <FINGERPRINT_SUBCHAVE>`** atualiza a assinatura de auto-vinculação (*self-signature*) da subchave.

## Exemplo
```bash
# Estender a data de expiracao de uma subchave especifica por mais 1 ano (1y) via CLI nao-interativa
gpg --quick-set-expire \
  "0123456789ABCDEF0123456789ABCDEF01234567" \
  1y \
  "FEDCBA9876543210FEDCBA9876543210FEDCBA98"
```

## Limites e trade-offs
Sempre que estender a validade (`--quick-set-expire`), adicionar uma nova subchave (`--quick-add-key`) ou revogar uma subchave comprometida, **você precisa re-exportar e republicar a sua chave pública (`gpg --armor --export`)** no WKD / GitHub / repositórios dos clientes para que eles recebam os novos pacotes de assinatura/revogação!

## Como verificar
Verifique a presença e integridade do certificado de revogação de emergência em `ls -l ~/.gnupg/openpgp-revocs.d/` e guarde uma cópia impressa (Paperkey / QR Code) ou em cofre offline.

## Conexões
- [[gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr]] — Veja também: GnuPG & `dirmngr`: Descoberta Segura de Chaves Públicas via **WKD (*Web Key Directory*)** e **OPENPGPKEY DANE (RFC 7929)** vs Keyservers HKP.
- [[gnupg-modelo-confianca-tofu-trust-on-first-use-wot-tsign]] — Veja também: GnuPG: Modelos de Validação de Chaves (**`tofu+pgp`**, *Web of Trust* Clássico, `--tofu-policy` e Assinaturas de Confiança `tsign`).
- [[gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth]] — Referência cruzada direta com gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth.
- [[certbot-acme-renewal-information-ari-revogacao-comprometimento-chave]] — Referência cruzada direta com certbot-acme-renewal-information-ari-revogacao-comprometimento-chave.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
