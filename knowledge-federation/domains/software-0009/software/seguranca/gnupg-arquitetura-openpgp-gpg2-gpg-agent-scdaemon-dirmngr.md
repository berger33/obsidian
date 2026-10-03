---
id: software.seguranca.tranche08.000701
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

# GNU Privacy Guard (**GnuPG 2.x**): Arquitetura Modular (`gpg`, `gpg-agent`, `scdaemon`, `dirmngr` e `keyboxd`) e Padrão **OpenPGP (RFC 4880 / RFC 9580)**

## Em uma frase
**GnuPG (`gpg` 2.x)** (GPLv3+, mantido pelo projeto GNU / g10 Code) é a implementação completa do padrão **OpenPGP** (RFC 4880 e atualização criptográfica RFC 9580) para assinatura digital, criptografia híbrida de dados e gerenciamento de chaves públicas.

## Por que importa
Ao contrário do `gpg1` monolítico legado, o **GnuPG 2.x** isola completamente o material criptográfico sensível em processos especializados: o binário `gpg` nunca manipula diretamente as chaves privadas no disco; todas as operações de chave privada são delegadas via socket IPC Assuan para o daemon **`gpg-agent`**, que por sua vez delega operações em tokens de hardware/YubiKey para o **`scdaemon`** e operações de rede (HKP/WKD/CRL/OCSP) para o **`dirmngr`**.

## Como funciona
Nas versões modernas do GnuPG (2.1+), o antigo chaveiro duplo (`pubring.gpg` / `secring.gpg`) foi substituído pelo formato indexado rápido **Keybox (`pubring.kbx`, ou banco SQLite via `keyboxd` no GnuPG 2.4+)** e pelo diretório **`private-keys-v1.d/`**, onde cada chave ou subchave privada é armazenada individualmente pelo seu *Keygrip* de 40 caracteres hexadecimais.

## Exemplo
```bash
# Verificar a versao do GnuPG 2.x, os algoritmos suportados (Ed25519, Cv25519, AES256) e os daemons gerenciados pelo gpgconf
gpg --version
gpgconf --list-components
```

## Limites e trade-offs
Sempre defina `export GPG_TTY=$(tty)` no arquivo de inicialização do shell (`~/.bashrc` ou `~/.zshrc`), conforme exige a documentação oficial `Invoking GPG-AGENT`, para que o programa `pinentry` saiba em qual terminal solicitar a passphrase ao usuário.

## Como verificar
Execute `gpg -K --with-keygrip` para listar suas chaves privadas e seus respectivos identificadores *Keygrip* em `~/.gnupg/private-keys-v1.d/`.

## Conexões
- [[gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth]] — Veja também: GnuPG: Arquitetura de **Chave Mestra `[C]` Offline** e **Subchaves Operacionais (`[S]` Sign, `[E]` Encrypt, `[A]` Authenticate)** em Curvas **Ed25519 / Cv25519**.
- [[gnupg-operacao-gpg-agent-pinentry-cache-ttl-ssh-agent-socket]] — Referência cruzada direta com gnupg-operacao-gpg-agent-pinentry-cache-ttl-ssh-agent-socket.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
