---
id: software.seguranca.tranche09.000825
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

# `dnsx`: Caça a **Subdomain Takeover (`dangling CNAME`)** e Filtragem por Código de Resposta DNS (**`-rcode noerror,nxdomain,servfail,refused`**)

## Em uma frase
Uma vulnerabilidade clássica de **Subdomain Takeover** ocorre quando um subdomínio da empresa (`promo.exemplo.com.br`) possui um registro **`CNAME`** apontando para um serviço em nuvem externo (`promo-exemplo.s3.amazonaws.com`, `promo.azurewebsites.net`, `promo.github.io`) ou para um servidor DNS delegado (`NS`) que foi **excluído/desprovisionado**: quando o resolvedor segue o `CNAME`, o destino retorna **`NXDOMAIN`** (ou `SERVFAIL` / `REFUSED` quando a zona DNS na AWS Route53 / Cloudflare foi apagada)!

## Por que importa
A maioria dos resolvedores simples descarta respostas `NXDOMAIN` e `SERVFAIL`, escondendo exatamente os subdomínios vulneráveis a Takeover!

## Como funciona
No `dnsx`, a flag **`-rcode` (`-rc`)** permite filtrar explicitamente por códigos de status DNS (**`-rcode nxdomain,servfail,refused`**) combinada com **`-cname -ns -resp`**: revelando instantaneamente todos os subdomínios que possuem um `CNAME` ou delegação `NS` pendurada (*dangling DNS record*) apontando para um destino morto!

## Exemplo
```bash
# Auditar uma lista de subdominios em busca de registros CNAME orfaos (NXDOMAIN/SERVFAIL) vulneraveis a Subdomain Takeover
dnsx -l /cases/easm/raw_subdomains.txt \
  -cname -ns -resp \
  -rcode nxdomain,servfail,refused \
  -o /cases/easm/dangling_dns_candidates.txt
```

## Limites e trade-offs
Sempre que o comando acima encontrar um subdomínio com `CNAME` retornando `[NXDOMAIN]` ou delegação `NS` retornando `[SERVFAIL]`/`[REFUSED]`, passe aquele subdomínio para **`nuclei -t http/takeovers/ -t dns/`** (ou reporte imediatamente à equipe de infraestrutura para remover o registro DNS órfão!).

## Como verificar
Verifique manualmente com `dig +trace <subdominio_suspeito>` em qual autoritativo a cadeia de resolução está falhando.

## Conexões
- [[dnsx-varredura-reversa-ptr-cidr-asn-descoberta-hosts-internos]] — Veja também: `dnsx` **`-ptr` (`-resp-only`)**: Varredura de **DNS Reverso (`PTR` / `in-addr.arpa`)** a partir de Blocos CIDR e Números de **ASN (`AS...`)**.
- [[dnsx-auditoria-seguranca-email-spf-dmarc-dkim-caa-txt-mx]] — Veja também: `dnsx`: Auditoria em Lote de Segurança de E-mail (**SPF / DMARC em `-txt`**, **`-mx`**) e Governança de Certificados (**`-caa`**, **`-soa`**).
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Referência cruzada direta com gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
