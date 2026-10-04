---
id: software.seguranca.tranche08.000703
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

# GnuPG & **`scdaemon`**: Armazenamento de Subchaves em Hardware (**YubiKey / SmartCard OpenPGP v3.4**), `keytocard` e Proteção de PIN/KDF

## Em uma frase
O daemon **`scdaemon`** do GnuPG implementa o protocolo **OpenPGP SmartCard (ISO/IEC 7816-4/8)**, permitindo transferir as subchaves privadas (`[S]`, `[E]`, `[A]`) para dentro do elemento seguro de um token criptográfico de hardware (como **YubiKey Série 5** ou **Nitrokey**).

## Por que importa
Uma vez movidas para o YubiKey via comando **`keytocard`** dentro do menu `gpg --edit-key`, as chaves privadas **nunca mais podem ser extraídas do chip de hardware**: quando o `gpg` precisa assinar um pacote ou decifrar um segredo, o `gpg-agent` envia o hash/desafio via USB/NFC para o YubiKey, que realiza a operação matemática `Ed25519`/`Cv25519` internamente após o toque físico do usuário (*Touch Policy = On/Fixed*)!

## Como funciona
Além de configurar o **User PIN** (mínimo 6 dígitos/caracteres, usado no dia a dia) e o **Admin PIN** (mínimo 8 caracteres, exigido para alterar configurações do cartão), habilite no cartão OpenPGP v3.3+ a função **KDF (`kdf-setup`)**, que faz o `gpg` enviar um hash salgado do PIN pelo cabo USB em vez do PIN em texto claro.

## Exemplo
```bash
# Verificar o status do token YubiKey/SmartCard OpenPGP, contadores de tentativas de PIN e stubs ssb>
gpg --card-status
```

## Limites e trade-offs
Antes de executar `keytocard` e salvar (`save`) no `gpg --edit-key` (operação que **move** a subchave para o YubiKey e substitui o arquivo local em `private-keys-v1.d/` por um ponteiro de hardware **`ssb>`**), faça **sempre** um backup cifrado offline da pasta `~/.gnupg` completa, pois o `keytocard` é destrutivo sobre a cópia em disco.

## Como verificar
Verifique na saída de `gpg -K` que as três subchaves exibem o indicador **`ssb>`** (sinal maior-que `>`), provando que residem no hardware token.

## Conexões
- [[gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth]] — Veja também: GnuPG: Arquitetura de **Chave Mestra `[C]` Offline** e **Subchaves Operacionais (`[S]` Sign, `[E]` Encrypt, `[A]` Authenticate)** em Curvas **Ed25519 / Cv25519**.
- [[gnupg-operacao-gpg-agent-pinentry-cache-ttl-ssh-agent-socket]] — Veja também: GnuPG (`gpg-agent`): Configuração de Cache (`default-cache-ttl`, `max-cache-ttl`), Emulação **`enable-ssh-support`** e *Agent Forwarding* Remoto.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
