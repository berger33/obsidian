---
id: software.seguranca.tranche07.000667
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

# Fail2ban: Correlação Multi-Linha com Tags de Sessão (**`<F-MLFID>`**, **`<F-ID>`**, **`<F-NOFAIL>`**) para Daemons que Logam IP e Falha em Linhas Separadas

## Em uma frase
Muitos daemons corporativos (como Postfix SMTP, Dovecot, OpenVPN ou aplicações Java/Go) **não** imprimem o endereço IP do cliente e o erro de autenticação na mesma linha de log: na Linha 1 o daemon registra `[conn-9812] Conexão recebida de 198.51.100.77` e na Linha 2 registra `[conn-9812] Falha de senha para o usuário admin` (sem repetir o IP!).

## Por que importa
Filtros simples linha a linha falhariam em extrair o IP na Linha 2; para resolver isso, o motor moderno do Fail2ban introduziu as tags de correlação de sessão **`<F-MLFID>...</F-MLFID>`** (*Multi-Line Failure ID*, como o PID ou ID de conexão) combinadas com **`<F-NOFAIL>`**!

## Como funciona
Na `prefregex` ou `failregex`, a primeira expressão com `<F-MLFID>` e `<F-NOFAIL>` captura e memoriza em memória a associação `conn-9812 -> 198.51.100.77` sem contar como falha ainda, e quando a linha de erro real chega com o mesmo `<F-MLFID>`, o Fail2ban recupera automaticamente o `<ADDR>` memorizado e contabiliza a falha!

## Exemplo
```ini
# /etc/fail2ban/filter.d/custom-multiline-vpn.local — Correlacao de ID de sessao entre multiplas linhas
[Definition]
prefregex = ^\s*vpn-gw\[(?P<mlfid>\d+)\]: <F-CONTENT>.+</F-CONTENT>$
cmnfailre = ^CONNECT client_ip="<ADDR>"<F-NOFAIL>$
            ^AUTH_FAILED reason="bad_token"$
failregex = %(cmnfailre)s
```

## Limites e trade-offs
Quando a conexão encerra, você pode usar a tag `<F-MLFFORGET>` na linha de desconexão do log para que o Fail2ban libere imediatamente a memória daquele identificador de sessão `<F-MLFID>`.

## Como verificar
Valide filtros multi-linha com `fail2ban-regex` sobre um trecho de log contendo conexões intercaladas de múltiplos clientes simultâneos.

## Conexões
- [[fail2ban-protecao-proxies-reversos-nginx-http-auth-limit-req-xff]] — Veja também: Fail2ban: Proteção de Proxies Reversos **Nginx / Envoy** (`nginx-http-auth`, `nginx-limit-req`, `nginx-botsearch`) e Cuidados com `X-Forwarded-For`.
- [[fail2ban-acoes-customizadas-webhooks-thehive-abuseipdb-observabilidade]] — Veja também: Fail2ban: Desenvolvimento de **Actions (`action.d/`)** Customizadas, Integração com Webhooks SOC/TheHive e Métricas Prometheus.
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Referência cruzada direta com fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos.
- [[fail2ban-testes-performance-fail2ban-regex-benchmark-logs]] — Referência cruzada direta com fail2ban-testes-performance-fail2ban-regex-benchmark-logs.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
