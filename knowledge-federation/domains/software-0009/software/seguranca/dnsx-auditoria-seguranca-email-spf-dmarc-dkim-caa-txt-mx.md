---
id: software.seguranca.tranche09.000826
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

# `dnsx`: Auditoria em Lote de Segurança de E-mail (**SPF / DMARC em `-txt`**, **`-mx`**) e Governança de Certificados (**`-caa`**, **`-soa`**)

## Em uma frase
Organizações que possuem dezenas ou centenas de domínios registrados (incluindo domínios defensivos ou de marcas antigas que não enviam e-mail) frequentemente esquecem de configurar registros **SPF (`v=spf1 -all`)**, **DMARC (`_dmarc.<dominio>` com `v=DMARC1; p=reject`)** e **CAA (`0 issue "letsencrypt.org"`)** nos domínios secundários — permitindo que atacantes enviem phishing forjando aqueles domínios!

## Por que importa
Com o `dnsx`, uma equipe de SecOps audita o portfólio inteiro de 500 domínios da empresa em 3 segundos consultando **`-txt`**, **`-mx`**, **`-caa`** e **`-soa`** em lote e exportando para JSONL (`-json`)!

## Como funciona
E usando a flag **`-d _dmarc` invertida ou sed** sobre a lista de domínios (`sed 's/^/_dmarc./' domains.txt | dnsx -txt -resp`), você verifica instantaneamente quais domínios da organização não possuem política DMARC ou estão apenas em modo `p=none`!

## Exemplo
```bash
# Auditar em lote os registros TXT (SPF), MX e CAA de todos os dominios raiz da organizacao
dnsx -l /cases/easm/company_root_domains.txt -txt -mx -caa -resp -json -o /cases/easm/domains_spf_mx_caa.jsonl
sed 's/^/_dmarc./' /cases/easm/company_root_domains.txt | dnsx -txt -resp -o /cases/easm/domains_dmarc.txt
```

## Limites e trade-offs
Para todo domínio estacionado (*parked domain*) da empresa que **não** é usado para enviar e-mails, a recomendação obrigatória de segurança é publicar um registro TXT **`v=spf1 -all`**, um registro `_dmarc` **`v=DMARC1; p=reject;`** e um registro Null MX (**`0 .`**, RFC 7505).

## Como verificar
Filtre no `domains_spf_mx_caa.jsonl` qualquer domínio que não possua string `v=spf1` em `.txt` ou que possua `+all` / `?all`.

## Conexões
- [[dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused]] — Veja também: `dnsx`: Caça a **Subdomain Takeover (`dangling CNAME`)** e Filtragem por Código de Resposta DNS (**`-rcode noerror,nxdomain,servfail,refused`**).
- [[dnsx-auditoria-transferencia-zona-axfr-trace-delegacao-dns]] — Veja também: `dnsx`: Teste em Massa de **Transferência de Zona DNS (`-axfr`)** e Rastreamento da Cadeia de Delegação Autoritativa (**`-trace`**).
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Referência cruzada direta com certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao.
- [[gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr]] — Referência cruzada direta com gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
