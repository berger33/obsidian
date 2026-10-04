---
id: software.seguranca.tranche07.000664
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

# Fail2ban: Validação e Benchmark de Expressões Regulares com **`fail2ban-regex`** antes do Deploy em Produção

## Em uma frase
O utilitário de linha de comando **`fail2ban-regex`** testa qualquer arquivo de filtro (ou expressão regular direta) contra um arquivo de log real ou contra o `systemd-journal`, reportando quantas linhas casaram, quais IPs foram extraídos, quantas linhas falharam e **quanto tempo em milissegundos cada regex levou para executar**.

## Por que importa
Subir um filtro customizado para produção sem testá-lo primeiro com `fail2ban-regex` pode resultar em uma jail cega (`0 matched` por causa de uma diferença no formato de data `datepattern`) ou em alto consumo de CPU no daemon Python.

## Como funciona
Passar **`--print-all-matched`** (ou `--print-all-missed`) permite auditar linha por linha se a regex casa exclusivamente com os eventos de falha de autenticação e ignora linhas de login bem-sucedido.

## Exemplo
```bash
# Testar e medir o tempo de execucao do filtro customizado contra um arquivo de log real antes de ativar a jail
fail2ban-regex --print-all-matched \
  /var/log/corp-api/auth.log \
  /etc/fail2ban/filter.d/corp-api-auth.local
```

## Limites e trade-offs
Se o `fail2ban-regex` reportar `0 matched` mas a regex do corpo estiver correta, verifique a linha `Date template hits`: o Fail2ban exige reconhecer o carimbo de tempo no início da linha antes de aplicar o `failregex` ao restante da mensagem.

## Como verificar
Adicione a execução do `fail2ban-regex` contra amostras de logs de ataque e logs benignos no pipeline de CI do repositório de infraestrutura (Ansible/Puppet) da empresa.

## Conexões
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Veja também: Fail2ban: Escrita Segura de Filtros (`failregex`, `ignoreregex`, `<HOST>` vs `<ADDR>`) e Prevenção de **ReDoS** e *Log Injection*.
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Veja também: Fail2ban: Escalabilidade de Firewall com Sets **`nftables` / `ipset`**, *Exponential Backoff* (`bantime.increment`) e Jail **`recidive`**.
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Referência cruzada direta com fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
