---
id: software.seguranca.tranche07.000663
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

# Fail2ban: Escrita Segura de Filtros (`failregex`, `ignoreregex`, `<HOST>` vs `<ADDR>`) e Prevenção de **ReDoS** e *Log Injection*

## Em uma frase
Os arquivos em `/etc/fail2ban/filter.d/` usam expressões regulares Python (`failregex` e `ignoreregex`) com tags pré-definidas como **`<HOST>`** (casa IPv4, IPv6 ou hostname se `usedns` permitir) e **`<ADDR>`** (casa estritamente endereços IPv4 ou IPv6 numéricos) para extrair o endereço do atacante de cada linha de log.

## Por que importa
Como o conteúdo das linhas de log frequentemente inclui strings enviadas pela rede pelo próprio atacante (ex.: a URL requisitada no Nginx, o `User-Agent` ou o nome de usuário inválido no SSH), **escrever um `failregex` frouxo com `.*` guloso permite dois ataques graves contra o próprio Fail2ban: ReDoS (*Regular Expression Denial of Service* por backtracking catastrófico) e *Arbitrary IP Banning via Log Injection***!

## Como funciona
Se uma regra de servidor web for escrita como `^<HOST> .* "GET .* HTTP/1\.[01]" 401$` ou `Failed login for .* from <HOST>`, um atacante pode enviar como nome de usuário a string `"admin from 8.8.8.8"`, fazendo o `.*` engolir o texto e casar o IP forjado `8.8.8.8` no lugar do IP real! Por isso, **sempre ancore a regex no início (`^`) e no fim (`$`)**, use classes restritas sem espaços (`\S+` ou `[^"]+`) em vez de `.*`, prefira **`<ADDR>`** e mantenha **`usedns = no`** na jail.

## Exemplo
```ini
# /etc/fail2ban/filter.d/corp-api-auth.local — Filtro ancorado e resistente a ReDoS/Log Injection
[Definition]
prefiret = ^<F-MLFID>\s*corp-api\[\d+\]:</F-MLFID>\s+
failregex = ^AUTH_FAILURE client_ip="<ADDR>" user="[^"]{1,64}" reason="invalid_credentials"$
ignoreregex =
```

## Limites e trade-offs
Para estender o `failregex` de um filtro padrão sem sobrescrever as regras originais da distribuição, utilize a interpolação documentada em `jail.conf(5)`: **`failregex = %(known/failregex)s`** seguida da sua nova linha indentada.

## Como verificar
Nunca habilite `usedns = yes` em produção: fazer resolução DNS reversa/direta sobre hostnames em logs permite que um atacante controle um registro DNS apontando para o IP de um parceiro ou gateway e force o Fail2ban a banir a vítima.

## Conexões
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Veja também: Fail2ban: Anatomia de uma **Jail** (`findtime`, `maxretry`, `bantime`, `ignoreip`, `ignoreself` e `backend = systemd`).
- [[fail2ban-testes-performance-fail2ban-regex-benchmark-logs]] — Veja também: Fail2ban: Validação e Benchmark de Expressões Regulares com **`fail2ban-regex`** antes do Deploy em Produção.
- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Referência cruzada direta com fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client.
- [[fail2ban-protecao-proxies-reversos-nginx-http-auth-limit-req-xff]] — Referência cruzada direta com fail2ban-protecao-proxies-reversos-nginx-http-auth-limit-req-xff.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
