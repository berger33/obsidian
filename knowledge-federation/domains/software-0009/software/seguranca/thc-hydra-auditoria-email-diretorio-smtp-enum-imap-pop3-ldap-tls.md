---
id: software.seguranca.tranche16.001578
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditando Serviços de E-mail e Diretório no THC-Hydra: Enumeração de Contas **`smtp-enum` (`VRFY`/`EXPN`/`RCPT TO`)**, **`smtp`**, **`imap`/`pop3`** e **`ldap3` (`-S` LDAPS)**

## Em uma frase
Como usar o **THC-Hydra** para testar se um servidor de e-mail SMTP permite **Enumeração de Usuários Válidos (`smtp-enum`)** ou Relay Autenticado Fraco (`smtp`), e como auditar binds simples e CRAM/DIGEST-MD5 em servidores **LDAP v3 (`ldap3` / `ldaps`)**?

## Por que importa
Primeiro: o módulo **`smtp-enum`** do Hydra testa automaticamente os três comandos clássicos do protocolo SMTP (`RFC 5321`) que podem revelar se uma caixa de correio ou conta de usuário existe no servidor: **`VRFY`** (padrão), **`EXPN`** e **`RCPT TO`** (configuráveis via opção `-m`)!

## Como funciona
Segundo: para servidores de diretório corporativo, o Hydra inclui os módulos **`ldap2`**, **`ldap3`**, **`ldap3-crammd5`** e **`ldap3-digestmd5`** (suportando LDAPS na porta `636` com a flag `-S`), onde você informa o **Base DN / Bind DN template** usando o placeholder `^USER^` na opção de módulo!

## Exemplo
```bash
# Verificar opcoes dos modulos smtp-enum e ldap3 e testar enumeracao de usuarios SMTP (VRFY) em um servidor de laboratorio
hydra -U smtp-enum
hydra -U ldap3
hydra -L ./usuarios_candidatos.txt -f -t 4 192.0.2.25 smtp-enum VRFY
```

## Limites e trade-offs
Como proteger o seu servidor SMTP (**Postfix / Exim / Exchange**) contra enumeração de contas pelo módulo `smtp-enum`? No Postfix (`/etc/postfix/main.cf`), configure **`disable_vrfy_command = yes`** e garanta que respostas a `RCPT TO` não-autenticados passem por *rate limiting* (`smtpd_client_event_limit_exceptions` / `anvil`) e listas de controle de acesso estritas!

## Como verificar
E em servidores **LDAP (`389-ds` / FreeIPA / OpenLDAP / Active Directory)**, desative *Anonymous Binds* desnecessários, exija sempre **TLS 1.3 (`ldaps://` ou `StartTLS` obrigatório com `sssd`/`kanidm`)** e aplique políticas de bloqueio temporário de conta após falhas consecutivas de bind!

## Conexões
- [[thc-hydra-geracao-bruteforce-x-charset-pw-inspector-filtragem-wordlists]] — Veja também: Geração On-the-Fly (**`-x min:max:charset`**) e Filtragem de Wordlists por Política de Senha com o Utilitário **`pw-inspector`** do THC-Hydra.
- [[thc-hydra-validacao-controles-defensivos-fail2ban-crowdsec-waf-pam]] — Veja também: Usando o THC-Hydra em **Purple Team e Engenharia de Confiabilidade de Segurança** para Validar Regras do **Fail2ban, CrowdSec, WAF (Coraza/ModSecurity) e `pam_faillock`**.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
