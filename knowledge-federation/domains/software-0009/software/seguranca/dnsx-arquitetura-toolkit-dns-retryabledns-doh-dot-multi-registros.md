---
id: software.seguranca.tranche09.000821
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

# ProjectDiscovery **`dnsx`**: Arquitetura do Toolkit DNS Multi-Propósito sobre `retryabledns`, Resolvers **UDP / TCP / DoH / DoT** e Modo **`-recon`**

## Em uma frase
**`dnsx`** (`projectdiscovery/dnsx`, licença MIT, escrito em Go sobre `miekg/dns` e `projectdiscovery/retryabledns`) é o canivete suíço de resolução, sondagem e força bruta DNS do ecossistema ProjectDiscovery.

## Por que importa
Quando ferramentas passivas (`subfinder`, `amass enum -passive`, Certificate Transparency logs) retornam dezenas de milhares de subdomínios históricos, uma grande fração desses nomes já expirou ou foi desativada (`NXDOMAIN` / `SERVFAIL`): passar a lista pelo **`dnsx`** valida em segundos quais FQDNs estão realmente ativos hoje e extrai seus registros DNS completos!

## Como funciona
Conforme documentado no `README.md` oficial, o `dnsx` consulta individualmente ou simultaneamente (**`-recon`**) **11 tipos de registros DNS**: **`-a`**, **`-aaaa`**, **`-cname`**, **`-ns`**, **`-txt`**, **`-srv`**, **`-ptr`**, **`-mx`**, **`-soa`**, **`-axfr`** (transferência de zona!) e **`-caa`**, suportando resolvedores customizados via **UDP, TCP, DNS-over-HTTPS (`https://...`) e DNS-over-TLS (`tls://...`)**!

## Exemplo
```bash
# Verificar a versao do dnsx e validar subdominios extraindo registros A, AAAA e CNAME com suas respostas (-resp)
dnsx -version
dnsx -l /cases/easm/raw_subdomains.txt -a -aaaa -cname -resp -silent -o /cases/easm/resolved_subdomains.txt
```

## Limites e trade-offs
Por padrão, sem `-resp` (`-re`) nem `-resp-only` (`-ro`), o `dnsx` imprime apenas os nomes de host que resolveram com sucesso (`NOERROR`); adicione **`-resp`** para imprimir `host [valor_do_registro]` ou **`-resp-only`** para imprimir exclusivamente os valores resolvidos (ex.: apenas a lista de IPs!).

## Como verificar
Use `-recon -e axfr` quando quiser consultar todos os registros DNS informativos de uma lista de domínios sem disparar tentativas de transferência de zona `AXFR`.

## Conexões
- [[dnsx-deteccao-asn-cdn-filtragem-wildcards-auto-wildcard-wd]] — Veja também: `dnsx`: Filtragem Automática de **DNS Wildcards (`-wd` / `-auto-wildcard`, `-wt`)** e Enriquecimento de **ASN (`-asn`) e CDN (`-cdn`)**.
- [[dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused]] — Referência cruzada direta com dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
