---
id: software.seguranca.tranche09.000828
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod", "https://docs.projectdiscovery.io/tools/dnsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `dnsx`: Configuração de **Resolvedores DNS-over-HTTPS (`DoH`) e DNS-over-TLS (`DoT`)**, Controle de Taxa (`-rl`), `-retry` e `-timeout`

## Em uma frase
Diferente de ferramentas legadas que só aceitam endereços IPv4 na porta `53/UDP`, a flag **`-r` / `-resolver`** do `dnsx` (alimentada pela biblioteca `retryabledns`) aceita quatro protocolos de transporte DNS na mesma lista: **`udp:IP:53`**, **`tcp:IP:53`**, **`dot:IP:853` (DNS-over-TLS)** e **`doh:https://host/dns-query:443` (DNS-over-HTTPS)**!

## Por que importa
Usar resolvedores **DoH / DoT** durante auditorias em redes restritivas impede que firewalls locais ou provedores de internet interceptem, alterem ou apliquem *DNS hijacking* nas consultas em texto claro na porta `53/UDP`.

## Como funciona
Para garantir zero perda de respostas por congestionamento UDP quando utilizando resolvedores tradicionais em alta concorrência (`-t 100`), ajuste **`-rl <queries_por_segundo>`**, **`-retry 3`** (padrão `2` tentativas) e **`-timeout 3s`**.

## Exemplo
```bash
# Executar resolucao DNS usando transporte criptografado DNS-over-HTTPS (DoH) e DNS-over-TLS (DoT)
dnsx -l /cases/easm/raw_subdomains.txt \
  -a -resp \
  -r "doh:https://cloudflare-dns.com/dns-query:443,dot:dns.quad9.net:853" \
  -retry 3 -timeout 5s \
  -o /cases/easm/encrypted_dns_results.txt
```

## Limites e trade-offs
Execute **`dnsx -hc` (`-health-check`)** se notar timeouts anômalos: o diagnóstico verifica a resolução UDP/TCP/DoH/DoT e os limites de sockets do sistema operacional.

## Como verificar
Em varreduras massivas (`> 100.000` subdomínios), prefira resolvedores UDP dedicados com `-rl 1000` e `-retry 3`, reservando DoH/DoT para validação ou redes onde a porta `53/UDP` sofre interferência.

## Conexões
- [[dnsx-auditoria-transferencia-zona-axfr-trace-delegacao-dns]] — Veja também: `dnsx`: Teste em Massa de **Transferência de Zona DNS (`-axfr`)** e Rastreamento da Cadeia de Delegação Autoritativa (**`-trace`**).
- [[dnsx-templates-saida-customizados-ot-json-omit-raw-stream]] — Veja também: `dnsx`: Formatação Avançada com **Output Templates (`-ot '{{host}} {{a}}'`)**, JSONL Enxuto (`-json -omit-raw`) e Modo **`-stream`**.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning]] — Referência cruzada direta com amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
