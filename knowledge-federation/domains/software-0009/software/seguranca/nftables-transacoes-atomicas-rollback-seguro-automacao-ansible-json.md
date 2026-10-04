---
id: software.seguranca.tranche12.001190
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes", "https://wiki.nftables.org/wiki-nftables/index.php/Sets"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operação Segura sem Lockout: **Transações Atômicas (`nft -f`)**, Saída JSON (`nft -j`), Migração `iptables-translate` e Rollback Automático

## Em uma frase
Qual é o maior pesadelo de qualquer administrador de sistemas ou engenheiro de segurança ao atualizar regras de firewall remotamente via SSH em um servidor em nuvem? **Cometer um erro na regra e cortar a própria conexão SSH (*Remote Firewall Lockout*)**!

## Por que importa
No `nftables`, dois recursos fundamentais tornam a automação de firewall muito mais segura e previsível: **(1) Atomicidade Transacional (`nft -f /etc/nftables.conf`)** — todo o arquivo começando com `flush ruleset` é compilado e aplicado em uma **única transação atômica do kernel** (ou 100% do novo ruleset entra em vigor instantaneamente sem nenhuma janela de milissegundos com o firewall aberto, ou, se houver qualquer erro em qualquer linha, a transação inteira aborta e o ruleset antigo permanece intacto!); e **(2) API JSON nativa (`nft -j list ruleset`)** para auditoria automatizada!

## Como funciona
Para eliminar o risco de *lockout* humano ao testar uma mudança remota via SSH, utilize sempre o padrão de **Aplicação com Rollback Automático (`at` ou `systemd-run --on-active=60s`)** que restaura `/etc/nftables.backup.conf` após 60 segundos caso você perca a conexão e não cancele o timer!

## Exemplo
```bash
# Aplicar um novo ruleset do nftables remotamente com rollback automatico garantido em 60 segundos caso a sessao SSH caia
sudo nft list ruleset > /etc/nftables.backup.conf
sudo systemd-run --unit=nft-rollback --on-active=60s /usr/sbin/nft -f /etc/nftables.backup.conf
sudo nft -c -f /etc/nftables.conf && sudo nft -f /etc/nftables.conf
# Se a conexao SSH continuar funcionando, cancele o timer de rollback imediatamente:
sudo systemctl stop nft-rollback.timer
```

## Limites e trade-offs
Se você ainda possui scripts legados em `iptables` que precisam ser migrados para `nftables`, utilize os utilitários oficiais **`iptables-translate`** e **`iptables-restore-translate`**, que convertem comandos `iptables` automaticamente para a sintaxe equivalente do `nftables`!

## Como verificar
Habilite o serviço `systemd` (`sudo systemctl enable nftables.service`) para garantir que o `/etc/nftables.conf` seja carregado automaticamente no boot antes da subida das interfaces de rede.

## Conexões
- [[nftables-logging-estruturado-ulogd2-nflog-rastreamento-nftrace-debug]] — Veja também: Depuração em Tempo Real (**`meta nftrace set 1` / `nft monitor trace`**) e Logging Estruturado JSON (**`nflog` + `ulogd2`**) no `nftables`.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
