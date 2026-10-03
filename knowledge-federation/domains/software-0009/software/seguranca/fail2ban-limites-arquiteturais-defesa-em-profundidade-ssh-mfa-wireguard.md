---
id: software.seguranca.tranche07.000670
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md", "https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5", "https://github.com/fail2ban/fail2ban/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fail2ban: Limites Arquiteturais (*Rate Limiting* vs Autenticação Forte), *IPv6 Subnet Banning* e Defesa em Profundidade

## Em uma frase
Como destaca o próprio `README.md` oficial do Fail2ban (*"Though Fail2Ban is able to reduce the rate of incorrect authentication attempts, it cannot eliminate the risk presented by weak authentication"*), o Fail2ban é uma camada de contenção de taxa e higiene de perímetro, **nunca um substituto para autenticação forte**.

## Por que importa
Contra uma botnet distribuída com 50.000 IPs residenciais onde cada IP testa apenas 2 senhas (abaixo de `maxretry = 5`), ou em redes **IPv6** onde um único atacante possui um bloco `/64` inteiro (`2^64` endereços IPv6 individuais), banir um `/128` IPv6 por vez é insuficiente se o serviço aceitar senhas fracas.

## Como funciona
Para redes IPv6, configure a agregação de prefixos (banindo o bloco `/64` em vez do `/128` individual nas ações de firewall quando aplicável) e combine o Fail2ban com: **(1) `PasswordAuthentication no`** no `sshd_config` (aceitando apenas chaves Ed25519 ou certificados SSH emitidos por CA + FIDO2 `sk-ssh-ed25519@openssh.com`), **(2) MFA obrigatório** em portais web e **(3) Zero-Trust / VPN (`WireGuard` / `OpenZiti`)** ocultando portas de gerência da internet pública.

## Exemplo
```ini
# /etc/ssh/sshd_config.d/10-crypto-auth-only.conf — Hardening do OpenSSH em conjunto com a jail do Fail2ban
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AuthenticationMethods publickey
MaxAuthTries 3
```

## Limites e trade-offs
Após desativar `PasswordAuthentication no` no `sshd`, configure a jail `[sshd]` do Fail2ban com **`mode = aggressive`** para que o Fail2ban bloqueie imediatamente scanners que falham na negociação de chave pública (`Connection closed by authenticating user ... [preauth]`) ou sondam banners SSH sem autenticar.

## Como verificar
Verifique com `sudo sshd -T | grep -E "passwordauthentication|pubkeyauthentication|permitrootlogin"` a aplicação da política de autenticação forte.

## Conexões
- [[fail2ban-operacao-administrativa-ban-unban-manual-dbpurgeage]] — Veja também: Fail2ban: Operação de Resposta a Incidentes via `fail2ban-client` (`set <jail> banip`, `unbanip`, `unban --all` e Auditoria SQLite).
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Referência cruzada direta com fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip.
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Referência cruzada direta com sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
