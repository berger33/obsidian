---
id: software.seguranca.tranche12.001189
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

# Depuração em Tempo Real (**`meta nftrace set 1` / `nft monitor trace`**) e Logging Estruturado JSON (**`nflog` + `ulogd2`**) no `nftables`

## Em uma frase
Quando um pacote legítimo está sendo bloqueado por um ruleset complexo do `nftables` (com dezenas de chains, sets, vmaps e NAT) e você não sabe qual linha exata está descartando o pacote, como rastrear o caminho completo do pacote dentro do kernel sem adivinhar?

## Por que importa
O `nftables` possui uma ferramenta de diagnóstico incomparável chamada **`nftrace`**: basta criar uma regra temporária no `prerouting` marcando apenas o tráfego que você quer investigar (por exemplo, **`ip saddr 10.20.30.40 tcp dport 443 meta nftrace set 1`**) e abrir em outro terminal **`sudo nft monitor trace`**! O kernel imprimirá em tempo real cada hook, cada tabela, cada chain, **o número exato da linha/regra que casou** e o veredito final (`verdict drop` ou `verdict accept`)!

## Como funciona
E para o logging contínuo de produção no SIEM, em vez de poluir o `dmesg` do kernel com `log prefix ...` comum (quesem `limit rate` pode travar o console serial!), utilize **`log group <N>` (subsistema `nflog` via Netlink)** integrado ao daemon **`ulogd2`**, que grava logs de firewall diretamente em formato **JSON estruturado** em disco!

## Exemplo
```bash
# Ativar rastreamento nftrace apenas para pacotes vindos de 10.20.30.40 na porta 8443 e assistir a avaliacao regra por regra ao vivo
sudo nft insert rule inet filter input ip saddr 10.20.30.40 tcp dport 8443 meta nftrace set 1
sudo nft monitor trace
```

## Limites e trade-offs
Sempre que usar a instrução `log` tradicional no `nftables`, proteja-a obrigatoriamente com um limitador de taxa (ex.: **`limit rate 10/minute burst 5 packets log prefix "NFT-DROP: " drop`**) para que um scan de portas não gere milhões de linhas por minuto no `journald`/`rsyslog`.

## Como verificar
Lembre-se de remover a regra temporária de `meta nftrace set 1` (usando `sudo nft -a list chain ...` e `sudo nft delete rule ... handle <N>`) assim que concluir o troubleshooting.

## Conexões
- [[nftables-aceleracao-hardware-software-flowtables-fastpath-roteadores]] — Veja também: Aceleração de Fluxos de Rede com **`flowtables` (Fastpath Software e Hardware Offload)** no `nftables` para Gateways de Alta Vazão (10GbE / 40GbE).
- [[nftables-transacoes-atomicas-rollback-seguro-automacao-ansible-json]] — Veja também: Operação Segura sem Lockout: **Transações Atômicas (`nft -f`)**, Saída JSON (`nft -j`), Migração `iptables-translate` e Rollback Automático.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Referência cruzada direta com cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
