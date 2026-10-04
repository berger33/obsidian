---
id: software.seguranca.tranche08.000710
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

# GnuPG: Modelos de Validação de Chaves (**`tofu+pgp`**, *Web of Trust* Clássico, `--tofu-policy` e Assinaturas de Confiança `tsign`)

## Em uma frase
Importar uma chave pública no seu chaveiro (`gpg --import`) **não** a torna confiável (`[ unknown]`): o GnuPG precisa de um **Modelo de Confiança (`--trust-model`)** para decidir se uma chave pública pertence legitimamente ao User ID declarado.

## Por que importa
Além do modelo clássico da *Web of Trust* (`pgp`) e do modo manual (`direct`), o GnuPG 2.1+ introduziu o modelo híbrido **`--trust-model tofu+pgp`** (*Trust On First Use* combinado com OpenPGP): na primeira vez que o `gpg` vê uma chave associada a um endereço de e-mail, ele registra o vínculo no banco SQLite **`~/.gnupg/tofu.db`** e monitora a consistência ao longo do tempo.

## Como funciona
Se meses depois aparecer uma **segunda chave diferente** alegando pertencer ao mesmo endereço de e-mail `fornecedor@parceiro.com`, o motor **TOFU** detecta imediatamente o conflito e bloqueia a operação alertando sobre possível ataque Man-in-the-Middle!

## Exemplo
```bash
# Definir a politica TOFU como 'good' para uma chave verificada out-of-band e consultar estatisticas TOFU
gpg --trust-model tofu+pgp --tofu-policy good "0123456789ABCDEF0123456789ABCDEF01234567"
gpg --trust-model tofu+pgp --list-keys "secops@exemplo.com.br"
```

## Limites e trade-offs
Em equipes de engenharia onde existe uma Autoridade Certificadora OpenPGP interna (uma chave mestra corporativa offline que assina as chaves de cada novo engenheiro contratado), use **`tsign` (*Trust Signature*) restrita ao domínio regex `exemplo\.com\.br`** para que toda a equipe valide automaticamente apenas chaves da própria empresa.

## Como verificar
Verifique o estado de validade das chaves no chaveiro (`[ultimate]`, `[  full  ]`, `[  marginal]`, `[ unknown]`) executando `gpg --list-keys --with-colons`.

## Conexões
- [[gnupg-certificado-revogacao-ciclo-vida-expiracao-rotacao-subchaves]] — Veja também: GnuPG: Ciclo de Vida Criptográfico — Certificados de Revogação (`--gen-revoke`), Renovação de Validade (`--quick-set-expire`) e Resposta a Comprometimento.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.
- [[gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr]] — Referência cruzada direta com gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr.
- [[gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao]] — Referência cruzada direta com gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
