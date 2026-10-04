---
id: software.seguranca.tranche09.000829
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

# `dnsx`: Formatação Avançada com **Output Templates (`-ot '{{host}} {{a}}'`)**, JSONL Enxuto (`-json -omit-raw`) e Modo **`-stream`**

## Em uma frase
Quando você integra o `dnsx` em scripts de automação ou bancos de dados de inventário, muitas vezes você quer um formato de linha específico (por exemplo, CSV `hostname,ip` ou `hostname -> cname`) sem precisar rodar `jq` pesado em milhões de linhas.

## Por que importa
O `dnsx` incorpora o motor `valyala/fasttemplate` através da flag **`-ot` / `-output-template`**, que permite formatar cada linha de saída usando placeholders como **`{{host}}`**, **`{{a}}`**, **`{{aaaa}}`**, **`{{cname}}`**, **`{{ns}}`**, **`{{txt}}`**, **`{{mx}}`**, **`{{soa}}`**, **`{{ptr}}`** e **`{{status_code}}`**!

## Como funciona
E quando você exporta em JSON Lines (**`-j` / `-json`**), por padrão o `dnsx` inclui o pacote DNS bruto completo no campo `"raw_resp"`: adicionar a flag **`-or` / `-omit-raw`** remove o pacote bruto e reduz o tamanho do arquivo `.jsonl` em disco em mais de **70%**!

## Exemplo
```bash
# Exportar pares customizados com -ot e gravar JSONL enxuto sem o pacote DNS bruto (-json -omit-raw)
dnsx -l /cases/easm/raw_subdomains.txt \
  -a -cname \
  -ot "{{host}} -> A:{{a}} CNAME:{{cname}}" \
  -o /cases/easm/formatted_dns.txt

dnsx -l /cases/easm/raw_subdomains.txt -a -aaaa -cname -asn -cdn -json -omit-raw -o /cases/easm/compact_dns.jsonl
```

## Limites e trade-offs
Em pipelines contínuos onde o `subfinder` ou gerador de permutações envia milhões de linhas sem parar, passe a flag **`-stream`** para que o `dnsx` processe cada linha em streaming com consumo de memória RAM constante (`O(1)`).

## Como verificar
Compare o tamanho em bytes do arquivo `.jsonl` gerado com e sem `-omit-raw` para otimizar a ingestão no SIEM / Elasticsearch.

## Conexões
- [[dnsx-resolvedores-customizados-doh-dot-rate-limit-retry-timeout]] — Veja também: `dnsx`: Configuração de **Resolvedores DNS-over-HTTPS (`DoH`) e DNS-over-TLS (`DoT`)**, Controle de Taxa (`-rl`), `-retry` e `-timeout`.
- [[dnsx-descoberta-servicos-internos-srv-kerberos-ldap-sip-autodiscover]] — Veja também: `dnsx` **`-srv`**: Enumeração de Registros **`SRV` (RFC 2782)** para Descoberta de Controladores **Active Directory (`_ldap._tcp`, `_kerberos._tcp`)**, SIP e XMPP.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei]] — Referência cruzada direta com naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
